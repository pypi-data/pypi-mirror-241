#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 
# @Author   : wgh
import json
import os
import re
import logging

from FourthDimension.model.model_init import init_model


"""
文件说明：项目初始化
"""

patterns = []
question_template = []

# 获取当前脚本文件的路径
current_path = os.path.abspath(__file__)

# 获取当前脚本文件所在的目录
current_dir = os.path.dirname(current_path)

# 获取项目根目录的路径
root_dir = os.path.dirname(current_dir)

# 读取配置文件
with open('config.json') as f:
    config_setting = dict(json.load(f))

# 读取问句模板
with open(current_dir + '/question_regex.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        question_template.append(line)

for i, line in enumerate(question_template):
    patterns.append(re.compile(line))

patternsLen = len(patterns)
logging.warning('模型初始化...')
tokenizer, model = init_model(config_setting['embedding_model'])
