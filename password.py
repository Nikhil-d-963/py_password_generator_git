"""
Created by: Nikhil D
code name: Password Genarator
"""

import  random

a = input("Enter the site for genarate your passward: ")
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
sybles = "[]{}()*;:/,.-_"

all = lower+upper+numbers+sybles
length = 16
password = "".join(random.sample(all, length))
print("Your ",a," passwaord is ",password)
