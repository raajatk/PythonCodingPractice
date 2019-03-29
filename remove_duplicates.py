"""Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""

def remove_duplicates_using_loop(list):
    new_list = []
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    return new_list

def remove_duplicates_using_set(list):
    set1 = set(list)
    new_list = [i for i in set1]

    return new_list

list = [int(i) for i in input("Please input the list(elements separated by commas(,))\n").split(',')]

print("The output using sets ",remove_duplicates_using_set(list))
print("The output using loops ",remove_duplicates_using_loop(list))
