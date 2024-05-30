# Объединение парсеров в один.

# TODO: .doc, .odt
# TODO: remove character filtering from pdf_parser (clean_text), because we need latin letters

import re
from pdf_parser import extract_text_from_pdf, clean_text
from pathlib import Path
from docx_parser import DocumentParser # docx_parser
import docx # python-docx
from striprtf.striprtf import rtf_to_text # striprtf


def extract_text_from_rtf(file_path: Path) -> str:
    with open(file_path) as f:
        text = rtf_to_text( f.read())
        text = re.sub(r"\|", "", text)
        return text

def extract_text_from_docx(file_path: Path) -> str:
    res = []
    doc = DocumentParser(file_path)
    for _type, item in doc.parse():
        if 'text' in item:
            res.append(item['text'])
        elif 'data' in item:
            res.extend(' '.join(row) for row in item['data'])

    return '\n'.join(res)


def extract_text_from_docx_2(file_path: Path) -> str:
    document = docx.Document(file_path)
    text = '\n'.join([paragraph.text for paragraph in document.paragraphs])
    tables = '\n'.join(' '.join(map(str, row.cells))
                       for table in document.tables for row in table.rows)

    return f'{text}\n{tables}'


def read_any_doc(path: Path) -> str:
    extention = path.suffix
    text = None

    if extention == '.pdf':
        text = extract_text_from_pdf(path)
    elif extention == '.rtf':
        text = extract_text_from_rtf(path)
    else:
        try:
            text = extract_text_from_docx(path)
        except Exception as e:
            text = extract_text_from_docx_2(path)
    return clean_text(text)
