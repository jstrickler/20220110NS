#!/usr/bin/env python

list1 = list()  # <1>
list2 = ['apple', 'banana', 'mango']  # <2>
list3 = []  # <3>
list4 = 'apple banana mango'.split()  # <4>

print("list1:", list1)
print("cities:", list2)
print("list3:", list3)
print("list4:", list4)

print("cities[0]:", list2[0])  # <5>
print("list4[2]:", list4[2])  # <6>

print("list4[-1]:", list4[-1])  # <7>
