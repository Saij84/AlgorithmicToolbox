from operator import itemgetter

data = [(4, 7), (1, 3), (2, 5), (5, 6)]

sort_list = sorted(data, key=lambda tup: tup[1])
sort_list1 = sorted(data, key=itemgetter(1))

print(sort_list, sort_list1)