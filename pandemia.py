def infected(s):
    newmap = s.split('X')
    infected = 0
    for x in newmap:
        if x.count('1')>0:
            infected += len(x)
    total = len(s) - s.count('X')
    if infected == 0:
        return 0
    else:
        return 100*infected/total


print(infected('XXXXX'))