import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    """
    Возвращает текст страницы не больше заданного размера и его размер в символах.
    
    Args:
        text (str): Полный текст, из которого нужно получить страницу.
        start (int): Номер первого символа в тексте, с которого должна начинаться страница.
        page_size (int): Максимальный размер страницы.
    
    Returns:
        (str, int): Текст страницы и ее размер в символах.
    """
    punctuation = [',', '.', '!', ':', ';', '?']
    
    # Получаем часть текста, начиная с указанного символа
    part_text = text[start:]
    
    # Если размер части текста меньше или равен максимальному размеру страницы, возвращаем ее
    if len(part_text) <= size:
        return part_text, len(part_text)
    
    # Ищем первый знак препинания, который может быть концом страницы
    for i in range(size, len(part_text)):
        if part_text[i] in punctuation:
            # Если следующий символ - многоточие, включаем его в страницу
            if i + 1 < len(part_text) and part_text[i + 1] in punctuation:
                i += 1
            return part_text[:i + 1], i + 1
    
    # Если не найден знак препинания, возвращаем максимальную длину страницы
    return part_text[:size], size


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    """
    Преобразует текст книги в словарь, где ключи - номера страниц, а значения - тексты этих страниц.
    """
    with open(path, 'r', encoding='utf-8') as file:
        book_text = file.read()

    page_start = 0
    page_num = 1

    while page_start < len(book_text):
        page_text, page_size = _get_part_text(book_text, page_start, PAGE_SIZE)
        book[page_num] = page_text.lstrip()
        page_start += page_size
        page_num += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))