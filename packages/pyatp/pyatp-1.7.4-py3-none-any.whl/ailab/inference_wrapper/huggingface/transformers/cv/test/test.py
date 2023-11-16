from aiges.dto import Response, ResponseData, DataListNode, DataListCls

"""personal param"""
model_name = 'vit_patch16_224_in21k'
# /home/sdk_models/vit_base_patch16_224_in21k
# /data1/cgzhang6/ailab_sdk/src/test/ailabmodel/my_vit_patch16
full_path = '/data1/cgzhang6/ailab_sdk/src/test/ailabmodel/my_vit_patch16'
module_name = 'image_classification'
""""""

import sys
print(sys.path)

import importlib
module_path = f'ailab.inference_wrapper.huggingface.transformers.cv.{module_name}.wrapper.wrapper'
wrapper_module = importlib.import_module(module_path)
Wrapper = getattr(wrapper_module, 'Wrapper')
wrapper = Wrapper()

def Init():
    import os
    os.environ['FULL_MODEL_PATH'] = full_path
    wrapper.wrapperInit({})

def Once(key, text):
    http_node = DataListNode()
    http_node.key = 'image'
    with open(text, 'rb') as file:
        # 读取文件内容
        image_data = file.read()
    http_node.data = image_data
    http_data = DataListCls()
    http_data.list.append(http_node)
    wrapper.wrapperOnceExec({"atp_patch_id":key}, http_data, key)

if __name__ == '__main__' :
    Init()
    Once(1, '/data1/cgzhang6/images/test_pic/sunflower01.jpg')
    Once(1, '/data1/cgzhang6/images/test_pic/peony04.jpg')
    Once(1, '/data1/cgzhang6/images/test_pic/rose03.jpg')
    Once(1, '/data1/cgzhang6/images/test_pic/lily05.jpg')
    Once(1, '/data1/cgzhang6/images/test_pic/peony01.jpg')
    Once(1, '/data1/cgzhang6/images/test_pic/sakura01.jpg')


