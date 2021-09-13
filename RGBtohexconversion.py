def rgb(r, g, b):
    list = [r,g,b]
    rgb = ''
    for i in list:
        if i <= 0:
            i = '00'
        elif i > 255:
            i = 'FF'
        elif len(str(i)) < 2:
            i = '0' + str(i)
        else:
            i = hex(i).upper()[2:4]
        rgb = rgb + i
    print(rgb)


def rgb2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    print(("{:02X}" * 3).format(round(r), round(g), round(b)))

rgb(174 ,14 ,142)

