from aiges.dto import Response, ResponseData, DataListNode, DataListCls

"""personal param"""
model_name = 'baichuan_7b'
pretrain_model_name = '/home/sdk_models/baichuan_7b/'
token_path = '/home/sdk_models/baichuan_7b/'
zip_path = '/home/finetuned_models/my_baichuan_model/adapter.zip'
stream = 1
module_name = 'efficient'
finetune_type = 'lora'
""""""

import sys
print(sys.path)

import importlib
module_path = f'ailab.inference_wrapper.huggingface.lora.nlp.{module_name}.wrapper.wrapper'
wrapper_module = importlib.import_module(module_path)
Wrapper = getattr(wrapper_module, 'Wrapper')
wrapper = Wrapper()

def Init():
    import os
    os.environ['PRETRAINED_MODEL_NAME'] = model_name
    os.environ['FULL_MODEL_PATH'] = pretrain_model_name
    os.environ['TOKENIZER_PATH'] = token_path
    config = {}
    if stream:
        config['common.lic'] = 1
    wrapper.wrapperInit(config)

def LoadRes(key):
    zip_file_path = zip_path
    with open(zip_file_path, 'rb') as zip_file:
        # 读取压缩包的二进制数据
        zip_data = zip_file.read()
        # 计算数据长度
        zip_data_length = len(zip_data)

    list_node = DataListNode()
    list_node.key = str(key)
    list_node.data = zip_data
    list_node.len = zip_data_length

    req_data = DataListCls()
    req_data.list.append(list_node)
    wrapper.wrapperLoadRes(req_data, key)

def Once(key, text):
    http_node = DataListNode()
    http_node.key = 'text'
    text_data = text
    text_data = text_data.encode('utf-8')
    http_node.data = text_data 
    http_data = DataListCls()
    http_data.list.append(http_node)

    import os
    os.environ['PetrainedModel'] = model_name
    wrapper.wrapperOnceExec({"atp_patch_id":key}, http_data, key)

def UnloadRes(key):
    wrapper.wrapperUnloadRes(key)

def StreamCreate(patch_id):
    s = wrapper.wrapperCreate({}, 'presid',patch_id)
    return s.handle

def StreamWrite(handle,text):
    http_node = DataListNode()
    http_node.key = 'text'
    text_data = text
    text_data = text_data.encode('utf-8')
    http_node.data = text_data 
    http_data = DataListCls()
    http_data.list.append(http_node)

    wrapper.wrapperWrite(handle,http_data,'sessionid')

def StreamDestroy(handle):
    wrapper.wrapperDestroy(handle)

if __name__ == '__main__' :
    Init()
    LoadRes('1')
    if stream:
        handle_0 = StreamCreate('1')
        StreamWrite(handle_0,'what is NLP')
    else:
        Once('0', 'what is NLP')
        Once('1', 'what is NLP')
    #UnloadRes('1')


