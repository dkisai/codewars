def duplicate_count(text):
    text = text.lower()
    rep = 0
    for char in 'abcdefghijklmnopqrstuvwxyz0123456789':
        if text.count(char) > 1:
            rep += 1
    return rep


print(duplicate_count('Indivisibilities'))