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
