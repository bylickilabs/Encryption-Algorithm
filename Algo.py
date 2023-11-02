from math import sqrt
from random import randint

def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def creation_keys():
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

def encoding(text, open_key):
    cipher_list = []
    e, n = open_key
    for letter in text:
        cipher_list.append(ord(letter) ** e % n)

    return cipher_list

def decoding(cipher_list, close_key):
    text = ""
    d, n = close_key
    for item in cipher_list:
        text += chr(int(item) ** d % n)

    return text

def encoding_mode():
    print("\n --> Verschlüsselung <-- (~˘▾˘)~")

    text = str(input("[+] Text Eingabe - "))
    open_key, close_key = creation_keys()
    print("[~] Offen - [{},{}].".format(open_key[0], open_key[1]))
    print("[~] Geschlossene - [{},{}].".format(close_key[0], close_key[1]))

    cipher_list = encoding(text, open_key)

    print("\n --> Ausgabe <--")
    print(cipher_list)

def decoding_mode():
    print("\n » Entschlüsselung « (~˘▾˘)~")

    cipher_list = eval(input("[+] Eingabe Liste - "))
    close_key = eval(input("[+] Eingabe des geschlossenen Key - "))

    text = decoding(cipher_list, close_key)

    print("\n --> Ausgabe <--")
    print(text)

def main():
    print("[x] Bylickilabs Encrypt Algorithm. [x]")
    print(" • 0. Verschlüsselung.\n • 1. Entschlüsselung.")

    mode = int(input("[?] Mode - "))

    if mode == 0:
        encoding_mode()
    elif mode == 1:
        decoding_mode()
    else:
        print("[x] Falsche Eingabe \"0, 1, 2\".")
        raise SystemExit

if __name__ == '__main__':
    main()