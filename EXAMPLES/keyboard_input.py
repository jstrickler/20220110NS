#!/usr/bin/env python

name = input("What is your name: ")
quest = input("What is your quest? ")
print(name, "seeks", quest)

raw_num = input("Enter number: ")  # <1>   # int(input("...")

try:
    num = int(raw_num)  # <2>
except ValueError as err:
    print(err)
    print("Please enter an integer")
    exit(1)

print("2 times", num, "is ", 2 * num)

print("2 times " + str(num) + " is " + str(2 * num))

a = "John"
b = 123
print(a, b)

x = "2 times " + str(num) + " is " + str(2 * num)
print(x)







