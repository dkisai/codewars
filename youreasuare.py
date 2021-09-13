def is_square(n):
    if n < 0:
        return False
    x = n // 2
    seen = set([x])
    while x * x != n:
        if n == 0:
            break
            return True
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True