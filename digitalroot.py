def digital_root(n):
    if (n < 10):
        return n
    n = str(n)
    sum = 0
    while len(n) > 1:
        sum = 0
        for x in n:
            sum += int(x)
        n = str(sum)
    return sum


def digital_root2(n):
    return n % 9 or n and 9

n=4936540165416541654156412348657193
print("Test 1",digital_root2(n))
print("Test 2",digital_root2(n))
#    16  -->  1 + 6 = 7
#   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
