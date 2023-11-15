import io
import re

from fastapi import UploadFile
from langchain.document_loaders import Docx2txtLoader

from FourthDimension.parser.files import File
from .common import process_file


def replace_multiple_newlines(text):
    pattern = r'\n{1,}'  # 匹配连续一个以上的换行符
    replacement = '\n'  # 替换为一个换行符
    updated_text = re.sub(pattern, replacement, text)
    return updated_text


def process_docx(file: File):
    process_paras = process_file(
        file=file,
        loader_class=Docx2txtLoader
    )

    for i, d in enumerate(process_paras):
        process_paras[i] = replace_multiple_newlines(d)
    return process_paras


def parse_docx(file_path, file_name):
    print('正在处理：' + file_name)

    with open(file_path, "rb") as f:
        file_content = f.read()

    # Create a file-like object in memory using BytesIO
    file_object = io.BytesIO(file_content)
    upload_file = UploadFile(
        file=file_object, filename=file_name, size=len(file_content)
    )
    file_instance = File(file=upload_file)
    file_instance.content = file_content

    # 调用process_docx方法，并传递参数
    enable_summarization = True
    doc_parse_result = process_docx(file_instance)
    return doc_parse_result
