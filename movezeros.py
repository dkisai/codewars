def move_zeros(array):
    if len(array) == 0 or array.count(0) == 0:
        return array
    else:
        zero = array.count(0)
        array.remove(0)
        while array.count(0) != 0:
            array.remove(0)
        for x in range(zero):
            array.append(0)
        return array




print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))