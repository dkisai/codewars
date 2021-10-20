def solution(number):
    sumatotal = 0
    for x in range(0, number):
        if x % 3 == 0 or x % 5 == 0:
            sumatotal += x
    return sumatotal


print(solution(15))
