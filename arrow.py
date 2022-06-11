def arrow(my_char, max_length):
    for line in range(max_length+1):
        for chars in range(line):
            print("*", end="")
        print("\n")
    for line in range(max_length):
        for chars in range(max_length - line - 1):
            print("*", end="")
        print("\n")


arrow("*", 6)