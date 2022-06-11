# the shortest solution
def arrow(my_char, max_length):
    for line in range(max_length+1):
            print("*" * line)
    for line in range(max_length):
            print("*" * (max_length - line - 1))


arrow("*", 9)