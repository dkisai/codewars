def pig_it(text):
    pigit =''
    for x in text.split():
        if x.isalpha():
            x = x[1:] + x[0] + "ay"
            pigit += x + ' '
        else:
            pigit += x + ' '
    return pigit[:-1]

print(pig_it('Hello Diego Kisai'))