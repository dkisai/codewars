def sumas(list):
    salto = 0
    total = 0
    for x in range(len(list)):
        if salto == x:
            salto += 1
            continue
        else:
            salto += 1
            total *= list[x]
    return total



lista = [1,2,3,4,5]
print(sumas(lista))