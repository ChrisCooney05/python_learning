my_info = ('chris', 24, 'programmer')
# this is a tuple, like a list but immutable
# my_info[0] = 'dave'
# this throws an error as we cant change element at index 0
print(my_info[0], my_info[-1])
# I can still access my info,justt not change it

name, age, job = my_info
print(name)
print(age)
print(job)
# this is called unpacking a tuple, chris is stored in name and so on.

one_element_tuple = (4)
print(one_element_tuple)
# we get 4 not a tuple as () can be used for order of opperation in math
one_element_tuple = (4, )
print(one_element_tuple)
# we need a trailing comma to create a one element tuple
