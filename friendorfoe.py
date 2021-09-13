def friend(x):
    newlist = [n for n in x if len(n) <= 4]
    return newlist

    #Code


print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man, Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))