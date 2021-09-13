def diamond(n):
    limite = n
    vueltas = n * 2
    cont_vueltas = 0
    cont = 1
    while cont_vueltas < vueltas:
        if cont < limite:
            limite = n
            print('*' * cont , '\n')
        else:
            limite = 1
            print('*' * cont , '\n')
            cont -= 1
        cont_vueltas -= 1


diamond(5)
