"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of
different sizes."""

print("Please input the first list !!")
a = [int(i) for i in input().split()]

print("Please input the second list !!")
b = [int(i) for i in input().split()]

a = set(a)
b = set(b)
c = list(a.intersection(b))
print("The common elements in two lists are ",c)
