def high(x):
    texto_separado = x.split(' ')
    alto = 0
    valores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
               'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
               'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, }
    for palabra in texto_separado:
        peso = 0
        for caracter in palabra:
            peso += valores[caracter]
            if peso > alto:
                alto = peso
                pala = palabra
    return pala


def high2(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

