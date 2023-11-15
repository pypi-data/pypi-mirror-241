#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 
# @Author   : wgh
import json
import time

from FourthDimension.config.config import config_setting
from FourthDimension.es.es_client import ElasticsearchClient
from FourthDimension.faiss_process.faiss_index import faiss_search_topk_IndexFlatL2
from FourthDimension.faiss_process.faiss_storage import embeddings_storage
from FourthDimension.model.chatGPT import answer_generate
from FourthDimension.utils.file_parse import get_all_docx_contexts
from FourthDimension.utils.mix_sort import rerank

word_storage = config_setting['word_storage']
embedding_storage = config_setting['embedding_storage']
search_select = config_setting['search_select']
index_name = config_setting['elasticsearch_setting']['index_name']

elasticsearch = 'elasticsearch'
faiss = 'faiss'
elasticsearch_faiss = 'elasticsearch+faiss'


def parse_data(doc_path):
    """
    数据解析
    :param doc_path: 文档路径
    :return:
    """
    print('文档解析中...')
    all_contexts = get_all_docx_contexts(doc_path)
    if search_select == elasticsearch:
        return all_contexts
    elif search_select == faiss or search_select == elasticsearch_faiss:
        all_doc_embeddings = embeddings_storage(all_contexts)
        return [all_contexts, all_doc_embeddings]


def query_entrance(question):
    """
    查询入口
    :param question: 问题
    :return:
    """
    if search_select == elasticsearch:
        top_k_context = es_query(question)
        return top_k_context
    elif search_select == faiss:
        print('目前单检索模式仅支持elasticsearch，请重试')
        return None


def query_storage_entrance(question, data):
    """
    存储及查询入口
    :param question: 问题
    :param data: 段落数据
    :return:
    """
    print('数据存储中...')
    if search_select == elasticsearch:
        top_k_context = es_storage_query(question, data)
        return top_k_context
    elif search_select == faiss:
        top_k_context = faiss_query(question, data[1])
        return top_k_context
    elif search_select == elasticsearch_faiss:
        es_client = ElasticsearchClient()
        es_client.insert_data(index_name, data[0])
        top_k_rerank_result = es_faiss_query(question, data[1])
        return top_k_rerank_result
    else:
        print(f"参数search_select无法匹配：f{search_select}")


def es_query(question):
    """
    es查询
    :param question: 问题
    :return:
    """
    es_client = ElasticsearchClient()
    top_k_context = es_client.es_search(question, index_name)
    return top_k_context


def es_storage_query(question, contexts):
    """
    es存储查询
    :param question: 问题
    :param contexts: 段落
    :return:
    """
    es_client = ElasticsearchClient()
    es_client.create_index(index_name)
    es_client.insert_data(index_name, contexts)
    top_k_context = es_client.es_search(question, index_name)
    return top_k_context


def faiss_query(question, embed_data):
    """
    faiss查询
    :param question: 问题
    :param embed_data: embedding结果
    :return:
    """
    top_k_context = faiss_search_topk_IndexFlatL2(question, embed_data)
    return top_k_context


def es_faiss_query(question, embed_data):
    """
    es+faiss重排查询
    :param question: 问题
    :param embed_data: embedding结果
    :return:
    """
    es_client = ElasticsearchClient()
    es_top_k_contexts = es_client.es_search(question, index_name)
    faiss_top_k_contexts = faiss_search_topk_IndexFlatL2(question, embed_data)
    merged_top_k = list(set(es_top_k_contexts + faiss_top_k_contexts))
    rerank_result = rerank(question, merged_top_k)
    return rerank_result


def generate_answers(question, data):
    """
    答案生成
    :param question: 问题
    :param data: 召回结果
    :return:
    """
    if data is not None:
        print('答案生成中...')
        answer = answer_generate(question, data)
        return answer
    else:
        return None


def query_storage(question, doc_path):
    """
    存储文档并查询接口
    :param question: 问题
    :param doc_path: 文档路径
    :return:
    """
    all_contexts = parse_data(doc_path)
    top_k_contexts = query_storage_entrance(question, all_contexts)
    answer = generate_answers(question, top_k_contexts)
    return answer


def query(question):
    """
    存储文档并查询接口
    :param question: 问题
    :return:
    """
    top_k_contexts = query_entrance(question)
    answer = generate_answers(question, top_k_contexts)
    return answer
