#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 
# @Author   : wgh


"""
文件说明：
"""
import os

from tqdm import tqdm

from FourthDimension.parser.docx_parser import parse_docx


def get_file_paths_and_names(folder_path):
    file_paths_and_names = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths_and_names.append((file_path, file_name))
    return file_paths_and_names


def get_all_docx_contexts(doc_path):
    file_paths_and_names = get_file_paths_and_names(doc_path)
    all_contexts = []
    for i, d in enumerate(file_paths_and_names):
        file_path = d[0]
        file_name = d[1]
        doc_paras = parse_docx(file_path, file_name)
        for k, dd in enumerate(tqdm(doc_paras)):
            # Tokenize sentences
            sentence = dd
            all_contexts.append({
                "context": sentence,
                "filename": file_name,
            })
    return all_contexts
