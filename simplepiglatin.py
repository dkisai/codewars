def pig_it(text):
    pigit =''
    splt = text.split(' ')
    for x in splt:
        if x == '!' or x == '?':
            pigit += x + ' '
        else:
            x = x[1:len(x)]+x[0]+"ay"
            pigit += x+' '
    return pigit[:-1]
