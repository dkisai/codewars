def narcissistic(value):
    total = 0
    valuetxt = str(value)
    for d in valuetxt:
        total += int(d) ** len(valuetxt)
    if total == value:
        return(True)
    else:
        return(False)

