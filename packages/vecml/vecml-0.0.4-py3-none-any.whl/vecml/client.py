import warnings
warnings.filterwarnings("ignore")

import grpc
import vdb_pb2
import vdb_pb2_grpc
import numpy as np
from tqdm import tqdm
import time

class vecml:
  channel = 0
  stub = 0
  host = ''
  port = 0
  MAX_MESSAGE_LENGTH = 1024 * 1024 * 1024
  step = 25
  api_key = 'empty';

  def init(api_key, region):
#    if region == 'us-east':
#      vecml.host = '18.217.188.7'
#    el
    if region == 'us-west':
      vecml.host = '35.247.90.126'
    else:
      #print('Unsupported region [{}]. Current choices are [us-west, us-east].'.format(region))
      print('Unsupported region [{}]. Current choices are [us-west].'.format(region))
      return;
    vecml.api_key = api_key;
    channel = grpc.insecure_channel(vecml.host + ':80',
      options=[
        ('grpc.max_send_message_length', vecml.MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', vecml.MAX_MESSAGE_LENGTH),
      ], compression=grpc.Compression.Gzip)
    stub = vdb_pb2_grpc.VectorDBStub(channel)
    response = stub.request_port(vdb_pb2.Request(api_key=api_key))
    vecml.port = response.dest_port
    time.sleep(0.500)
    vecml.channel = grpc.insecure_channel(vecml.host + ':' + str(vecml.port),
      options=[
        ('grpc.max_send_message_length', vecml.MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', vecml.MAX_MESSAGE_LENGTH),
      ], compression=grpc.Compression.Gzip)
    vecml.stub = vdb_pb2_grpc.VectorDBStub(vecml.channel)

  def close():
    vecml.channel.close()
    vecml.channel = 0
    vecml.stub = 0

  def check_init():
    if vecml.stub == 0:
      raise Exception("Shoreline is not initialized. Please run vecml.init.")

  def filter_validation(filter_str):
    return True

  def insert(namedim, data, ids, **kwargs):
    vecml.check_init()
    name, dim = namedim
    data = np.array(data)
    n_data = len(ids)

    attributes = []
    if 'attributes' in kwargs:
      dicts = kwargs['attributes']
      for d in dicts:
        converted_map = dict()
        for key, value in d.items():
          tmp = vdb_pb2.GeneralType(float_value = float(value),int_value = int(value))
          converted_map[key] = tmp
        attributes.append(vdb_pb2.AttributeRow(attr=converted_map))

    step = max(1, n_data // vecml.step)
    pbar = tqdm(total=n_data)

    for i in range(0, n_data, step):
      begin = i
      end = min(i + step, n_data)
      if len(attributes) != 0:
        response = vecml.stub.insert(vdb_pb2.Request(table_name=name,vectors=vdb_pb2.Vectors(len=end - begin, dim=dim, data=data[begin:end,:].flatten().tolist(), ids=ids[begin:end], attribute_row=attributes[begin:end])))
      else:
        response = vecml.stub.insert(vdb_pb2.Request(table_name=name,vectors=vdb_pb2.Vectors(len=end - begin, dim=dim, data=data[begin:end,:].flatten().tolist(), ids=ids[begin:end])))

      if response.code != 0:
        print("[Warning]: Insertion failed. Error code:", response.code)
        return
      pbar.update(step)
    pbar.close()
  
  def insert_sparse(namedim, data, ids, **kwargs):
    vecml.check_init()
    name, dim = namedim
    n_data = len(ids)

    attributes = []
    if 'attributes' in kwargs:
      dicts = kwargs['attributes']
      for d in dicts:
        converted_map = dict()
        for key, value in d.items():
          tmp = vdb_pb2.GeneralType(float_value = value,int_value = value)
          converted_map[key] = tmp
        attributes.append(vdb_pb2.AttributeRow(attr=converted_map))
    
    step = max(1,n_data // vecml.step)
    pbar = tqdm(total=n_data)
    
    for i in range(0, n_data, step):
      begin = i
      end = min(i + step, n_data)
      subdata = data[begin:end,:]
      response = vecml.stub.insert_sparse(vdb_pb2.Request(table_name=name,vectors=vdb_pb2.Vectors(len=end - begin, dim=dim, data=subdata.data.tolist(), offset=subdata.indptr.tolist(), idx=subdata.indices.tolist(), ids=ids[begin:end], attribute_row=attributes[begin:end])))
      if response.code != 0:
        print("[Warning]: Insertion failed. Error code:", response.code)
        return
      pbar.update(step)
    pbar.close()

  def query(namedim, data, budget, topk, **kwargs):
    vecml.check_init()
    name, dim = namedim
    data = np.array(data)
    if len(data.shape) == 1:
      data = data.reshape([1, -1])
    n_data = len(data.flatten()) // dim
    filter_str = ''
    if 'filter' in kwargs:
      filter_str = kwargs['filter']
      if vecml.filter_validation(filter_str) == False:
        raise Exception("filter string (" + filter_str + ") is invalid")
    
    step = max(1,n_data // vecml.step)
    pbar = tqdm(total=n_data)
    ids = []
    dis = []
    for i in range(0, n_data, step):
      begin = i
      end = min(i + step, n_data)
      response = vecml.stub.query(vdb_pb2.Request(table_name=name,query_info=vdb_pb2.QueryInfo(topk=topk, budget=budget),vectors=vdb_pb2.Vectors(len=end - begin, dim=dim, data=data[begin:end,:].flatten().tolist(),filter=filter_str)))
      ids.append(response.ids)
      dis.append(response.dis)
      pbar.update(step)
    pbar.close()
    return np.concatenate(ids).reshape([-1,topk]), np.concatenate(dis).reshape([-1,topk])
  
  def query_sparse(namedim, data, budget, topk, **kwargs):
    vecml.check_init()
    name, dim = namedim
    if len(data.shape) == 1:
      data = data.reshape([1, -1])
    n_data = data.shape[0]
    filter_str = ''
    if 'filter' in kwargs:
      filter_str = kwargs['filter']
      if vecml.filter_validation(filter_str) == False:
        raise Exception("filter string (" + filter_str + ") is invalid")
    
    step = max(100,max(1, n_data // vecml.step))
    pbar = tqdm(total=n_data)
    ids = []
    dis = []
    for i in range(0, n_data, step):
      begin = i
      end = min(i + step, n_data)
      subdata = data[begin:end,:]
      response = vecml.stub.query_sparse(vdb_pb2.Request(table_name=name,query_info=vdb_pb2.QueryInfo(topk=topk, budget=budget),vectors=vdb_pb2.Vectors(len=end - begin, dim=dim, data=subdata.data.tolist(), offset=subdata.indptr.tolist(),idx=subdata.indices.tolist(),filter=filter_str)))
      ids.append(response.ids)
      dis.append(response.dis)
      pbar.update(step)
    pbar.close()
    return np.concatenate(ids).reshape([-1,topk]), np.concatenate(dis).reshape([-1,topk])

  def index(name, dim, measure, **kwargs):
    vecml.check_init()
    index_type = 0
    schema = dict()
    if 'schema' in kwargs:
      if isinstance(kwargs['schema'],dict) == False:
        raise Exception("The schema argument has to be a dict")
        return
      schema = kwargs['schema']
    if 'sparse' in kwargs:
      use_sparse = int(kwargs['sparse'])
      if use_sparse == 1:
        index_type = 1
    if 'gpu' in kwargs:
      use_gpu = int(kwargs['gpu'])
      if use_gpu == 1:
        index_type = 2
    bits = 0
    oporp_repeat = -1
    if 'rp' in kwargs:
      bits = int(kwargs['rp'])
      index_type = 3
    if 'oporp_repeat' in kwargs:
      oporp_repeat = int(kwargs['oporp_repeat'])


    idp_beta = 1.0
    idp_eps = 10.0
    use_idp = 0
    if measure == 'idp':
      index_type = 4
      use_idp = 1
      if 'idp_beta' in kwargs:
        idp_beta = float(kwargs['idp_beta'])
      if 'idp_eps' in kwargs:
        idp_eps = float(kwargs['idp_eps'])

    try:
      response = vecml.stub.index(vdb_pb2.Request(table_name=name,similarity=measure,vectors=vdb_pb2.Vectors(dim=dim,schema=schema),index_type=index_type,hash_bits=bits,oporp_repeat=oporp_repeat,use_idp=use_idp,idp_beta=idp_beta,idp_eps=idp_eps))
    except:
      pass
    return name, dim
  
  def train(namedim, label_attr, num_class):
    vecml.check_init()
    name, dim = namedim
    for res_str in vecml.stub.train(vdb_pb2.Request(table_name=name,vectors=vdb_pb2.Vectors(dim=dim),num_class=num_class,valid_table_name=name,label_name=label_attr,model_type=3,use_kernel=0)):
      print(res_str.str, end='')
    return name, dim
  
  def train_custom(namedim, label_attr, num_class, model_type, use_kernel, use_kernel_full):
    vecml.check_init()
    name, dim = namedim
    for res_str in vecml.stub.train(vdb_pb2.Request(table_name=name,vectors=vdb_pb2.Vectors(dim=dim),num_class=num_class,valid_table_name=name,label_name=label_attr,model_type=model_type,use_kernel=use_kernel,use_kernel_full=use_kernel_full)):
      print(res_str.str, end='')
    return name, dim
  
  def predict(namedim, test_data):
    vecml.check_init()
    name, dim = namedim
    response = vecml.stub.predict(vdb_pb2.Request(table_name=name,vectors=vdb_pb2.Vectors(dim=dim),valid_table_name=test_data))
    return np.array(response.label)
