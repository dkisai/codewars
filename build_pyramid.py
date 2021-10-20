def build_pyramid(string, n):
    totesp = len(string)*n
    total = ''
    for x in range(1, n+1): #Las veces que va a crecer la piramide
        spaces = totesp - (len(string) - x) // 2
        total = ' ' * spaces + total
        for y in range(len(string)):
            total += (string[y] * x)
        total += '\n'
    return total


print(build_pyramid('XxX', 10))
