"""Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates."""

list = [int(i) for i in input("Please input the list(elements separated by commas(,))\n").split(',')]
set1 = set(list)
new_list = [i for i in set1]

print(new_list)
