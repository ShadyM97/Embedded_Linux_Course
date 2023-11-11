#!/usr/bin/python3
def vowelCheck(x):
    if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u'):
        print("Vowel")
    else:
        print("Consonant")

y = input("Please Enter an alphabet:")

vowelCheck(y)