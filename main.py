from math import sqrt
from random import randint
import lang


def is_prime(n) -> bool:
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def creation_keys() -> tuple:
    p, q, e = 10, 10, 4
    while not is_prime(p):
        p = randint(500, 700)
    while not is_prime(q):
        q = randint(500, 700)
    n, f, d = p * q, (p - 1) * (q - 1), 0
    while (not is_prime(e)) or (e > f) or (f % e == 0):
        e += 1
    while (d * e) % f != 1:
        d += 1
    return (e, n), (d, n)


def encoding(text, open_key) -> list:
    cipher_list = []
    e, n = open_key
    for letter in text:
        cipher_list.append(ord(letter) ** e % n)

    return cipher_list


def decoding(cipher_list, close_key) -> str:
    text = ""
    d, n = close_key
    for item in cipher_list:
        text += chr(int(item) ** d % n)

    return text


def encoding_mode(lang):
    print(f"\n --> {lang[0][0]} <-- (~˘▾˘)~")

    text = str(input(f"[+] {lang[2][0]} - "))
    open_key, close_key = creation_keys()
    print("[~] {} - [{},{}].".format(lang[3][0], open_key[0], open_key[1]))
    print("[~] {} - [{},{}].".format(lang[4][0], close_key[0], close_key[1]))

    cipher_list = encoding(text, open_key)

    print(f"\n --> {lang[5][0]} <--")
    print(cipher_list)


def decoding_mode(lang):
    print(f"\n » {lang[0][1]} « (~˘▾˘)~")

    cipher_list = eval(input(f"[+] {lang[6][0]} - "))
    close_key = eval(input(f"[+] {lang[7][0]} - "))

    text = decoding(cipher_list, close_key)

    print(f"\n --> {lang[5][0]} <--")
    print(text)


def main():
    print("[x] Bylickilabs Encrypt Algorithm. [x]")
    print(" • 0. English.\n • 1. German.\n • 2. Russian.\n • 3. French.\n • 4. Spanish.\n • 5. Hindi. ")

    language = (input("[?] Language - "))
    match language:
        case '0':
            print("[x] English. [x]")
            langData = lang.language('en')
        case '1':
            print("[x] German. [x]")
            langData = lang.language('de')
        case '2':
            print("[x] Russian. [x]")
            langData = lang.language('ru')
        case '3':
            print("[x] French. [x]")
            langData = lang.language('fr')
        case '4':
            print("[x] Spanish. [x]")
            langData = lang.language('es')
        case '5':
            print("[x] Hindi. [x]")
            langData = lang.language('hi')
        case _:
            print("[x] Incorrect entry. Please choose from: \"0, 1, 2, 3, 4, 5\".")
            raise SystemExit

    print(f" • 0. {langData[0][0]}.\n • 1. {langData[0][1]}.")

    mode = (input(f"[?] {langData[1][0]}  "))

    if mode == '0':
        encoding_mode(langData)
    elif mode == '1':
        decoding_mode(langData)
    else:
        print("[x] Incorrect entry. Please choose from \"0, 1\".")
        raise SystemExit


if __name__ == '__main__':
    main()
