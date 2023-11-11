#!/usr/bin/python3

import calendar

#Get Year and Month from User
year = int(input("Enter Year (YYYY):"))
month = int(input("Enter Month (MM):"))
print(calendar.month(year, month))