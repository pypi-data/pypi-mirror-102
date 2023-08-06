# -*- coding: utf-8 -*-
from nn_sdk.py_tf_csdk import csdk_object
'''
    python 推理demo
    支持 python (demo.py) , c (nn_sdk.h) , java (nn_sdk.java)
    python 使用如下
    支持多子图,支持图多输入多输出.
    支持tensorflow 1 pb , tensorflow 2 pb , tensorflow ckpt
    net_stage 推理子图序号0-n
'''
config = {
    "model_dir": r'./model.ckpt',
    "log_level": 4, # 0 fatal , 2 error , 4 info , 8 debug
    "model_type": 1,  # 0 pb format   if 1 ckpt format
    "ConfigProto": {
        "log_device_placement": False,
        "allow_soft_placement": True,
        "gpu_options": {
            "allow_growth": True
        },
    },
    "graph_inf_version": 1,  # the format of tensorflow pb model [1,2]
    "graph": [
        {
            #tf 1 node sample "input_ids:0" ,  tf2 sample "input_ids"  data_type  int int64 long longlong float double
            #python 接口可以忽视 data_type,shape字段,在 c接口会使用，例子 python {"node":"input_ids:0"}
            "input": [
                {"node":"input_ids:0", "data_type":"float", "shape":[1, 256]},
                {"node":"input_mask:0", "data_type":"float", "shape":[1, 256]}
            ],
            "output": [
                {"node":"input_ids:0", "data_type":"float", "shape":[1, 256]},
            ],
        }
    ]}

seq_length = 256
input_ids = [[10.] * seq_length]
input_mask = [[1] * seq_length]
sdk_inf = csdk_object(config)
if sdk_inf.valid():
    net_stage = 0
    ret, out = sdk_inf.process(net_stage, input_ids,input_mask)
    print(ret)
    print(out)
    sdk_inf.close()