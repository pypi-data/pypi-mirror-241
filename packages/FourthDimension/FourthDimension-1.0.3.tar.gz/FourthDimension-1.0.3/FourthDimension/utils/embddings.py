#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 
# @Author   : wgh


"""
文件说明：
"""

import torch
from tqdm import tqdm


def get_context_embeddings(contexts, tokenizer, model):
    all_doc_embeddings = []
    device = next(model.parameters()).device
    for k, dd in enumerate(tqdm(contexts)):
        # Tokenize sentences
        filename = dd['filename']
        context = dd['context']
        encoded_input = tokenizer([context], padding=True, truncation=True, max_length=512, return_tensors='pt')
        # Compute token embeddings
        with torch.no_grad():
            model_output = model(input_ids=encoded_input['input_ids'].to(device),
                                 token_type_ids=encoded_input['token_type_ids'].to(device),
                                 attention_mask=encoded_input['attention_mask'].to(device))
            # Perform pooling. In this case, cls pooling.
            sentence_embeddings = model_output[0][:, 0]
        # normalize embeddings
        sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
        embeddings_str = sentence_embeddings.tolist()[0]
        all_doc_embeddings.append({
            "filename": filename,
            "context": context,
            "context_embeddings": embeddings_str
        })
    return all_doc_embeddings


def get_question_embeddings(question, tokenizer, model):
    encoded_input = tokenizer([question], padding=True, truncation=True, max_length=512, return_tensors='pt')
    device = next(model.parameters()).device
    # Compute token embeddings
    with torch.no_grad():
        model_output = model(input_ids=encoded_input['input_ids'].to(device),
                             token_type_ids=encoded_input['token_type_ids'].to(device),
                             attention_mask=encoded_input['attention_mask'].to(device))
        # Perform pooling. In this case, cls pooling.
        sentence_embeddings = model_output[0][:, 0]
    # normalize embeddings
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
    question_embeddings_str = sentence_embeddings.tolist()[0]
    return question_embeddings_str
