#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 
# @Author   : wgh


"""
文件说明：
"""
import os

import faiss
import numpy as np

from FourthDimension.utils.embddings import get_context_embeddings
from FourthDimension.config.config import tokenizer, model

# 获取当前脚本文件的路径
current_path = os.path.abspath(__file__)

# 获取当前脚本文件所在的目录
current_dir = os.path.dirname(current_path)


def embeddings_storage(contexts):
    all_doc_embeddings = get_context_embeddings(contexts, tokenizer, model)
    context_embeddings = np.array([item["context_embeddings"] for item in all_doc_embeddings], dtype=np.float32)
    index = faiss.IndexFlatL2(context_embeddings.shape[1])  # 创建Faiss索引
    index.add(context_embeddings)  # 添加上下文嵌入向量到索引
    faiss.write_index(index, current_dir + '/../cache/faiss_cache/index.index')
    return all_doc_embeddings
