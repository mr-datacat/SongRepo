russian_symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
czech_symbols = 'aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzž'
english_symbols = 'abcdefghijklmnopqrstuvwxyz'


def clear_string(text: str) -> str:
    text = text.replace(' ', '')
    for d in '1234567890':
        text = text.replace(d, '')
    for s in '!@#$%^&*()-_=+[]\\|/?\'\"`,.~<>;}:{':
        text = text.replace(s, '')
    text = text.lower()
    return text


def is_russian(text: str) -> bool:
    text = clear_string(text)
    result = True
    for char in text:
        if char not in russian_symbols:
            result = False
            break
    return result


def is_english(text: str) -> bool:
    text = clear_string(text)
    result = True
    for char in text:
        if char not in english_symbols:
            result = False
            break
    return result


def is_czech(text: str) -> bool:
    text = clear_string(text)
    result = True
    for char in text:
        if char not in czech_symbols:
            result = False
            break
    return result
