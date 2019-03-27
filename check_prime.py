print("Please input the number")
num = int(input())

flag = 0
for i in range(2,num):
    if num%i==0:
        flag=1

if flag==0:
    print("The input number is PRIME")
else:
    print("The input number is NON-PRIME")
