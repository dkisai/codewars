def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return '{} likes this'.format(names[0])
    elif len(names) == 2:
        return '{} and {} likes this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    elif len(names) > 3:
        return '{}, {} and {} others like this'.format(names[0], names[1],(len(names)-2))


name = ['Alex', 'Jacob', 'Mark', 'Max']
print(likes(name))

#   test.assert_equals(likes([]), 'no one likes this')
#   test.assert_equals(likes(['Peter']), 'Peter likes this')
#   test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
#   test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
#   test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')-