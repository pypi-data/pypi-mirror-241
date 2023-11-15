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

from FourthDimension.config.config import config_setting, tokenizer, model
from FourthDimension.utils.embddings import get_question_embeddings

top_k = config_setting['recall_config']['top_k']

# 获取当前脚本文件的路径
current_path = os.path.abspath(__file__)

# 获取当前脚本文件所在的目录
current_dir = os.path.dirname(current_path)


def faiss_search_topk_IndexFlatL2(question, embed_data):
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    index = faiss.read_index(current_dir + '/../cache/faiss_cache/index.index')
    index.nprobe = 10

    # 批量检索与问题最相关的上下文
    question_embedding = get_question_embeddings(question, tokenizer, model)
    query_embeddings = np.array([question_embedding], dtype=np.float32)
    distances, indices = index.search(query_embeddings, top_k)

    # 按照相关性从大到小排序上下文：
    sorted_indices = indices[0][np.argsort(distances[0])]
    top_k_context = [embed_data[i]["context"] for i in sorted_indices]
    return top_k_context
