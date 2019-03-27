"""Write a program that asks the user how  many  Fibonnaci  numbers to  generate and
then generates them. Take this opportunity  to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci  seqence is a  sequence of  numbers where the next number in the
sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""

def gen_fibonacci(length):
    list = [1]
    item = 0
    for i in range(1,length):
        if i==1:
            item = list[i-1]
        else:
            item = list[i-2]+list[i-1]
        list.append(item)

    return list

print("Please input the length to generate the Fibonnaci Series")

length = int(input())

print(gen_fibonacci(length))
