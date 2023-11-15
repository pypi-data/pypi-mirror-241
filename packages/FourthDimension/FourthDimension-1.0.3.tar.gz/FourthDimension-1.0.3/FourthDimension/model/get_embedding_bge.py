#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 
# @Author   : wgh


"""
文件说明：
"""
import json
import os

import torch
from tqdm import tqdm

from FourthDimension.parser.docx_parser import parse_docx
from FourthDimension.config.config import tokenizer, model


# 获取数据集context的embedding结果
def embedding_context(data_path):
    with open(data_path, 'r', encoding='utf-8') as fr:
        ld_data = json.load(fr)
    for k, v in enumerate(tqdm(ld_data)):
        # Tokenize sentences
        sentence = v['context']
        encoded_input = tokenizer([sentence], padding=True, truncation=True, max_length=512, return_tensors='pt')
        # Compute token embeddings
        with torch.no_grad():
            model_output = model(input_ids=encoded_input['input_ids'].cuda(0),
                                 token_type_ids=encoded_input['token_type_ids'].cuda(0),
                                 attention_mask=encoded_input['attention_mask'].cuda(0))
            # Perform pooling. In this case, cls pooling.
            sentence_embeddings = model_output[0][:, 0]
        # normalize embeddings
        sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
        ld_data[k]['context_embedding'] = sentence_embeddings.tolist()[0]
    # with open('../data/230703_test160v1.1_embed.json', 'w', encoding='utf-8') as fw:
    #     json.dump(ld_data, fw, indent=4, ensure_ascii=False)
    return ld_data


# 对问题做embedding
def embedding_question(question):
    encoded_input = tokenizer([question], padding=True, truncation=True, max_length=512, return_tensors='pt')
    with torch.no_grad():
        model_output = model(input_ids=encoded_input['input_ids'].cuda(0),
                             token_type_ids=encoded_input['token_type_ids'].cuda(0),
                             attention_mask=encoded_input['attention_mask'].cuda(0))
        # Perform pooling. In this case, cls pooling.
        sentence_embeddings = model_output[0][:, 0]
    # normalize embeddings
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
    question_embeddings = sentence_embeddings.tolist()[0]
    return question_embeddings


def get_file_paths_and_names(folder_path):
    file_paths_and_names = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths_and_names.append((file_path, file_name))
    return file_paths_and_names


def embedding_context_docs(data_path):
    file_paths_and_names = get_file_paths_and_names(data_path)
    all_doc_context = []
    all_doc_embeddings = []
    for i, d in enumerate(file_paths_and_names):
        file_path = d[0]
        file_name = d[1]
        doc_paras = parse_docx(file_path, file_name)
        for k, dd in enumerate(tqdm(doc_paras)):
            # Tokenize sentences
            sentence = dd
            encoded_input = tokenizer([sentence], padding=True, truncation=True, max_length=512, return_tensors='pt')
            # Compute token embeddings
            with torch.no_grad():
                model_output = model(input_ids=encoded_input['input_ids'].cuda(0),
                                     token_type_ids=encoded_input['token_type_ids'].cuda(0),
                                     attention_mask=encoded_input['attention_mask'].cuda(0))
                # Perform pooling. In this case, cls pooling.
                sentence_embeddings = model_output[0][:, 0]
            # normalize embeddings
            sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
            embeddings_str = sentence_embeddings.tolist()[0]
            if {
                "context": sentence
            } not in all_doc_context:
                all_doc_context.append({
                    "context": sentence
                })
                all_doc_embeddings.append({
                    "context_embeddings": embeddings_str
                })
            # all_doc_embeddings.append({
            #     "context": sentence,
            #     "context_embeddings": embeddings_str
            # })
    return all_doc_context, all_doc_embeddings
    # return all_doc_embeddings


def embedding_contexts(context_list):
    all_doc_embeddings = []
    for k, dd in enumerate(tqdm(context_list)):
        # Tokenize sentences
        sentence = dd
        encoded_input = tokenizer([sentence], padding=True, truncation=True, max_length=512, return_tensors='pt')
        # Compute token embeddings
        with torch.no_grad():
            model_output = model(input_ids=encoded_input['input_ids'].cuda(0),
                                 token_type_ids=encoded_input['token_type_ids'].cuda(0),
                                 attention_mask=encoded_input['attention_mask'].cuda(0))
            # Perform pooling. In this case, cls pooling.
            sentence_embeddings = model_output[0][:, 0]
        # normalize embeddings
        sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
        embeddings_str = sentence_embeddings.tolist()[0]
        all_doc_embeddings.append({
            "context_embeddings": embeddings_str
        })
    return all_doc_embeddings


def embedding(embedding_str):
    # Tokenize sentences
    encoded_input = tokenizer([embedding_str], padding=True, truncation=True, max_length=512, return_tensors='pt')
    # Compute token embeddings
    with torch.no_grad():
        model_output = model(input_ids=encoded_input['input_ids'].cuda(0),
                             token_type_ids=encoded_input['token_type_ids'].cuda(0),
                             attention_mask=encoded_input['attention_mask'].cuda(0))
        # Perform pooling. In this case, cls pooling.
        sentence_embeddings = model_output[0][:, 0]
    # normalize embeddings
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
    embeddings_result = sentence_embeddings.tolist()[0]
    return embeddings_result
