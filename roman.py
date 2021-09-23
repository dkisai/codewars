def solution(n):
    umi = n // 1000
    cen = n % 1000 // 100
    dec = n % 100 // 10
    uni = n % 10

    if 0 < uni < 4:
        unirom = 'I'*uni
    elif uni == 4:
        unirom = 'IV'
    elif uni == 5:
        unirom = 'V'
    elif 5 < uni < 9:
        unirom = 'V'+ ('I'* (uni-5))
    elif uni == 9:
        unirom = 'IX'
    else:
        unirom = ''

    if 0 < dec < 4:
        decrom = 'X'*dec
    elif dec == 4:
        decrom = 'XL'
    elif dec == 5:
        decrom = 'L'
    elif 5 < dec < 9:
        decrom = 'L'+ ('X'* (dec-5))
    elif dec == 9:
        decrom = 'XC'
    else:
        decrom = ''

    if 0 < cen < 4:
        cenrom = 'C'*cen
    elif cen == 4:
        cenrom = 'CD'
    elif cen == 5:
        cenrom = 'D'
    elif 5 < cen < 9:
        cenrom = 'D'+ ('C'* (cen-5))
    elif cen == 9:
        cenrom = 'CM'
    else:
        cenrom = ''

    if 0 < umi < 4:
        umirom = 'M'*umi
    else:
        umirom = ''

    return umirom+cenrom+decrom+unirom


units = " I II III IV V VI VII VIII IX".split(" ")
tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
thousands = " M MM MMM".split(" ")

def solution2(n):

    print(n//1000)
    print(n%1000//100)
    print(n%100//10)
    print(n%10)
    return thousands[n // 1000] + hundreds[n % 1000 // 100] + tens[n % 100 // 10] + units[n % 10]


print(solution(1889))
