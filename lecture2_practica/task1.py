from string import *

def language_detect(text):
    for ch in text.lower():
        if ch in alf_english:
            return "en"
        if ch in alf_russian:
            return "ru"
    return "other"

def caesar_cipher(text, index, mode):
    language = language_detect(text)
    if language == "en":
        alf = alf_english
    elif language == "ru":
        alf = alf_russian
    else:
        return "Не удалость распознать поддерживаемый язык"

    result = ""
    for ch in text:
        lw_ch = ch.lower()
        if lw_ch in alf:
            old_index = alf.find(lw_ch)
            if mode.upper() == 'Ш':
                new_index = (old_index + index) % len(alf)
            elif mode.upper() == 'Д':
                new_index = (old_index - index) % len(alf)
            else:
                return "Не удалось разпознать режим"

            new_ch = alf[new_index]
            if ch.isupper():
                new_ch = new_ch.upper()

            result += new_ch
        else:
            result += ch
    return result


alf_english = ascii_lowercase
alf_russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

index = int(input("Какой требуется сдвиг?"))
text = input("Введите текст")
mode = input("Шифровать(Ш)/Дешифровать(Д)")

print(caesar_cipher(text, index, mode))

