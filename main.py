
def last_to_first(lst):
    if not lst:
        return lst
    if len(lst) == 1:
        return lst

    last_element = lst.pop()
    lst.insert(0, last_element)
    return lst

my_list = [1,2,3,4,9]
# a = int(input("create list and print some mumbers: "))
result = last_to_first(my_list)
print(result)

