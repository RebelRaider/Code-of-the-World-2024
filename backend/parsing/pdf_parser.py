import re

import pdfplumber

def pdf_to_string(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def clean_text(text: str) -> str:
    """
    Очищает текст от нежелательных символов и лишних пробелов.

    Parameters:
    - text (str): Текст для очистки.

    Returns:
    - str: Очищенный текст.

    Examples:
    >>> clean_text('Пример    текста, с   лишними пробелами.')
    """
    # Удаляем пробелы перед или после дефиса
    text = re.sub(r"-\s|\s-", "", text)

    # Удаляем пробелы перед знаками препинания
    text = re.sub(r"\s+([.,!?:;-])", r"\1", text)

    # Удаляем повторяющиеся знаки препинания
    text = re.sub(r"([.,!?:;-])([.,!?:;-])+", r"\1", text)

    text = re.sub(r"\t", " ", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ ]+", " ", text)
    text = re.sub(r"\n\s+", "\n", text)
    text = re.sub(r"\0", "", text)
    return text

