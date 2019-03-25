"""
Q. Create a program that asks the user to enter their name and their age. Print
out a message addressed to them that tells them the year that they
will turn 100 years old."""

import datetime as dt
name = input("Please enter your name..")
# print("The name entered is ",name)
age = input("Please enter your age...")
age = int(age)
# print("The age entered is ",age)
current_time = dt.datetime.now()
# print(current_time.year)
current_year = current_time.year;
year_100 = current_year-age+100
print("Hi "+name+"! You will be 100 years old in the year of "+str(year_100))

"""Successfully Completed the Coding Problem"""
