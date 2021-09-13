import string


def is_pangram(s):
    s = s.lower()
    if s.count('a') != 0 and s.count('b') != 0 and s.count('c') != 0 and s.count('d') != 0 and s.count('e') != 0 and s.count('f') != 0 and s.count('g') != 0 \
            and s.count('h') != 0 and s.count('i') != 0 and s.count('j') != 0 and s.count('k') != 0 and s.count('l') != 0 and s.count('m') != 0\
            and s.count('n') != 0 and s.count('o') != 0 and s.count('p') != 0 and s.count('q') != 0 and s.count('r') != 0 and s.count('s') != 0\
            and s.count('t') != 0 and s.count('u') != 0 and s.count('v') != 0 and s.count('w') != 0 and s.count('x') != 0 and s.count('y') != 0\
            and s.count('z') != 0:
        return True
    else:
        return False


def is_pangram3(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

text = 'asdfkasjfsdnmvclkjiaijhfklgsjdañfsd'
print(is_pangram(text))
print(is_pangram3(text))
