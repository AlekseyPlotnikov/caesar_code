def encryption_ru(str, shfr):
    text = []
    for i in str.lower():
        if i.isalpha():
            if ord(i) + shfr < 1104:
                text.append(chr((ord(i) + shfr)))
            else:
                text.append(chr((ord(i) + shfr - 32)))
        else:
            text.append(i)
    return ''.join(text).capitalize()


def encryption_ru2(str, shfr):
    text = []
    for i in str.lower():
        if i.isalpha():
            text.append(chr(((ord(i) + shfr - 1072)) % 32 + 1072))
        else:
            text.append(i)
    return ''.join(text).capitalize()


def encryption_eng(str, shfr):
    text = []
    for i in str.lower():
        if i.isalpha():
            if ord(i) + shfr < 123:
                text.append(chr((ord(i) + shfr)))
            else:
                text.append(chr((ord(i) + shfr - 26)))
        else:
            text.append(i)
    return ''.join(text).capitalize()


def encryption_eng2(str, shfr):
    text = []
    for i in str.lower():
        if i.isalpha():
            text.append(chr(((ord(i) + shfr - 97) % 26 + 97)))
        else:
            text.append(i)
    return ''.join(text).capitalize()


def decryption_ru(str, shfr):
    text = []
    for i in str.lower():
        if i.isalpha():
            if ord(i) - shfr < 1072:
                text.append(chr((ord(i) - shfr + 32)))
            else:
                text.append(chr((ord(i) - shfr)))
        else:
            text.append(i)
    return ''.join(text).capitalize()


def decryption_ru2(str, shfr):
    text = []
    for i in str.lower():
        if i.isalpha():
            text.append(chr(((ord(i) - shfr - 1072) % 32 + 1072)))
        else:
            text.append(i)
    return ''.join(text).capitalize()


def decryption_eng(str, shfr):
    text = []
    for i in str.lower():
        if i.isalpha():
            if ord(i) - shfr < 97:
                text.append(chr((ord(i) - shfr + 26)))
            else:
                text.append(chr((ord(i) - shfr)))
        else:
            text.append(i)
    return ''.join(text).capitalize()


def decryption_eng2(str, shfr):
    text = []
    for i in str.lower():
        if i.isalpha():
            text.append(chr((ord(i) - shfr - 97) % 26 + 97))
        else:
            text.append(i)
    return ''.join(text).capitalize()


def caesar_code():
    print('Приветсявую в программе шифр Цезаряю')
    while True:
        choice = input('Вы желаете зашифровать [ш] или дешифровать текст [д]?\n').lower() == 'д'
        language = input('На каком языке будет ваш текст? [ру/eng]\n').lower() == 'ру'
        shfr = int(input('На какой сдвиг вправо?\n'))
        text = input('Ведите текст:\n')
        if choice:
            if language:
                print(decryption_ru2(text, shfr))
            else:
                print(decryption_eng2(text, shfr))
        else:
            if language:
                print(encryption_ru2(text, shfr))
            else:
                print(encryption_eng2(text, shfr))
        a = input('Будет ли ещё текст?[да/нет]\n')
        if a.lower() != 'да':
            print('Пока!')
            break


caesar_code()
