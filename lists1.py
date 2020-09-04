last_semester_gradebook = [
    ("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]
subjects.append('computer science')
grades.append(100)
# append is used to add something to the end of a list

gradebook = list(zip(subjects, grades))
# zip will create and object of pairs combining both lists. (physics, 98) (calculus, 97)
# list will take the zipped object and turn it back into a list [('physics', 98), ('calculus', 97)]
gradebook.append(('visual arts', 93))
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
# we can also combine two lists together with + this also works for [98, 97, 85, 88] + [10] = [98, 97, 85, 88, 10]
print(full_gradebook)


my_range = range(11)
# makes a range object from 0 up to but not including 11
print(list(my_range))
# turns the range object into a list and prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_range_two = range(5, 101, 10)
# range can take up to 3 arguments 5 is where we start, 101 is where we end and 10 is by how much we increment each time
print(list(my_range_two))
# this will output [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
