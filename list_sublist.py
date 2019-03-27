"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function."""

def fetch_sublist(list):
    new_list = [list[0],list[-1]]
    return new_list

print("Please input the list of numbers separated by commas(,)")

list = [int(i) for i in input().split(',')]
sub_list = fetch_sublist(list)
print(sub_list)
