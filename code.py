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
