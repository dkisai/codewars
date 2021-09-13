def xo(s):
    contx = 0
    conto = 0
    s = s.lower()
    for x in s:
        if x == 'x':
            contx += 1
        elif x == 'o':
            conto += 1
    if conto == contx:
        return True
    else:
        return False

def xo2(s):
    s = s.lower()
    return s.count('x') == s.count('o')

#XO("ooxx") => true
#XO("xooxx") => false
#XO("ooxXm") => true
#XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
#XO("zzoo") => false