"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

print("Please input the string !!")
str = input()
flag = 0
back_count = 0;
for i in range(int(len(str)/2)+1):
    back_count -= 1
    # print("str[i]!=str[-1*i]",str[i],str[back_count])
    if str[i]!=str[back_count]:
        flag=1

if flag==1:
    print("Not a Palindrome")
else:
    print("Palindrome")
