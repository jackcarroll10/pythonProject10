


def swap_pairs(list):
    for i in list[:]:
        if (i % 2 == 0) and (i != list[-1]):
            list[i], list[i+1] = list[i+1], list[i]

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
swap_pairs(my_list)
print(my_list)
