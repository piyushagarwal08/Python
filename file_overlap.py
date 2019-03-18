def make_a_list(file):
    list_ = []
    fhand = open(file)
    line = fhand.readline().rsplit()
    while line:
        list_.append(line)
        line = fhand.readline().rsplit()
    return list_

prime_list = make_a_list('primenumbers.txt')
happy_list = make_a_list('happynumbers.txt')

overlaplist = [elem for elem in prime_list if elem in happy_list]
print(overlaplist)

