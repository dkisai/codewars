def scramble(s1, s2):
    s2 = list(s2)
    s3 = [elem for elem in s1 if elem in s2]
    s3 = list(set(s3))
    print(s3)
    s2.sort()
    s3.sort()
    print(s2)
    print(s3)
    return s3 == s2

print(scramble('katas', 'steak'))