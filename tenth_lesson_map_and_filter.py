my_list = ["Kolya", 10, True, 25, False, 30.5, "Python", 5, True, 3.2, False, 100, 33.3]

# map
my_list_str = list(map(lambda s: str(s), my_list))

# filter
my_list_int = list(filter(lambda i: type(i) is int, my_list))
