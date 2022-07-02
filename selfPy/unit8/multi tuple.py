first_tuple = (1, 2)
second_tuple = (4, 5)


def mult_tuple(tuple1, tuple2):
    list_of_tuple = []
    for t1 in tuple1:
        for t2 in tuple2:
            list_of_tuple.append((t1, t2))
    print(tuple(list_of_tuple))






mult_tuple(first_tuple, second_tuple)