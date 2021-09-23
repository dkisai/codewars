def encode(message, key):
    key = str(key)
    cnl = 0
    tot = []
    llave = list(key)
    valores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
               'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
               'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, }
    for char in message:
        test = valores[char]
        if cnl < len(key) - 1:
            cypher = test + int(llave[cnl])
            cnl +=1
            tot.append(cypher)
        else:
            cypher = test + int(llave[cnl])
            cnl = 0
            tot.append(cypher)
    return tot



print(encode("diegokisaialbagallart", 1989))