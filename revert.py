def reverse_words(text):
    list = text.split(' ')
    total = ''
    for x in list:
        total += x[::-1] + ' '
    return total[0:len(total)-1]



print(reverse_words('double  spaced  words'))





#test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
#test.assert_equals(reverse_words('apple'), 'elppa')
#test.assert_equals(reverse_words('a b c d'), 'a b c d')
#test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')