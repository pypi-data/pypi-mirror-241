import time

from FourthDimension.parser.files import File
from FourthDimension.utils.upload_file import DocumentSerializable


def process_file(
        file: File,
        loader_class
):
    file.compute_documents(loader_class)
    ll_part = []
    for doc in file.documents:  # pyright: ignore reportPrivateUsage=none
        ll_part.append(doc.page_content)

    return ll_part