"""Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5."""

print("Please input the comma(,) separated list")
list = [int(i) for i in input().split(',')]
print("The input list is ",list)
list_less_than_5 = []
for i in list:
    if i<5:
        list_less_than_5.append(i)

print("The new list is ",list_less_than_5)
