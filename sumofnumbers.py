def get_sum(a,b):
    suma = 0
    c = 0
    if a == b:
        suma = a
    elif a > b:
        for x in range(b,a+1):
            suma += x
    else:
        for x in range(a,b+1):
            suma += x
    return(suma)
    #good luck

print(get_sum(0,-1))
#get_sum(1, 0) == 1   // 1 + 0 = 1
#get_sum(1, 2) == 3   // 1 + 2 = 3
#get_sum(0, 1) == 1   // 0 + 1 = 1
#get_sum(1, 1) == 1   // 1 Since both are same
#get_sum(-1, 0) == -1 // -1 + 0 = -1
#get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2