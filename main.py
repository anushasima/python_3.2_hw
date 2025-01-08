import math

my_list = [12, 3, 4, 10]
# my_list.append(33)
# my_list.insert(0, False)
# my_list.extend([111, 222])
# my_list.reverse()
my_list.pop(3)
my_list.insert(0, 10)
# k = 0
# my_list[-1], my_list[k] = my_list[k], my_list[-1]
print(my_list)

my_list = [1]
my_list.pop(0)
my_list.insert(0, 1)
print(my_list)

my_list = [12, 3, 4, 10, 8]
my_list.pop(4)
my_list.insert(0, 8)
print(my_list)


# з пустим списком складнощі адже нема чого переміщувати
my_list = []
my_list.pop()
my_list.insert(0)
print(my_list)