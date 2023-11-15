#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 
# @Author   : wgh


"""
文件说明：模型初始化
"""
import os
import logging
import torch

os.environ['HF_ENDPOINT'] = "https://hf-mirror.com"
from transformers import AutoTokenizer, AutoModel


def init_model(model_name):
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if torch.cuda.is_available():
        model.cuda()
    print("模型初始化成功，参数量为：", sum([param.nelement() for param in model.parameters()]))
    model.eval()
    return tokenizer, model
