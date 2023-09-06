
tLangEnglish = [
    ['Encryption', 'Decryption'],
    ['What do you want to do?'],
    ['Input text'],
    ['Open'],
    ['Closed'],
    ['Output'],
    ['Input list'],
    ['Input closed key'],
]

tLangGerman = [
    ['Verschlüsselung', 'Entschlüsselung'],
    ['Was möchten Sie tun?'],
    ['Text Eingabe'],
    ['Offen'],
    ['Geschlossene'],
    ['Ausgabe'],
    ['Eingabe Liste'],
    ['Eingabe des geschlossenen Key'],
]

tLangRussian = [
    ['Шифрование', 'Расшифровка'],
    ['Что вы хотите сделать?'],
    ['Ввод текста'],
    ['Открытый'],
    ['Закрытый'],
    ['Выход'],
    ['Ввод списка'],
    ['Ввод закрытого ключа'],
]

tLangFrench = [
    ['Cryptage', 'Décryptage'],
    ['Que voulez-vous faire?'],
    ['Entrée de texte'],
    ['Ouvert'],
    ['Fermé'],
    ['Sortie'],
    ['Entrée de liste'],
    ['Entrée de clé fermée'],
]

tLangSpanish = [
    ['Cifrado', 'Descifrado'],
    ['¿Qué quieres hacer?'],
    ['Entrada de texto'],
    ['Abierto'],
    ['Cerrado'],
    ['Salida'],
    ['Entrada de lista'],
    ['Entrada de clave cerrada'],
]

tLangHindi = [
    ['एन्क्रिप्शन', 'डिक्रिप्शन'],
    ['आप क्या करना चाहते हैं?'],
    ['टेक्स्ट इनपुट'],
    ['खुला'],
    ['बंद'],
    ['आउटपुट'],
    ['सूची इनपुट'],
    ['बंद कुंजी इनपुट'],
]


def language(lang) -> list:
    match lang:
        case 'en':
            return tLangEnglish
        case 'de':
            return tLangGerman
        case 'ru':
            return tLangRussian
        case 'fr':
            return tLangFrench
        case 'es':
            return tLangSpanish
        case 'hi':
            return tLangHindi
        case _:
            pass
