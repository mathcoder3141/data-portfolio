"""
program to calculate any given day using the Gregorian Calandar (1582 - XXXX) and the Doomsday Rule
"""

doomsday_NLY = { 
  'January': 31,
  'February': 28,
  'March': 35,
  'April': 32,
  'May': 37,
  'June': 34,
  'July': 32,
  'August': 36,
  'September': 33,
  'October': 31,
  'November': 35,
  'December': 33
}

doomsday_LY = { 
  'January': 32,
  'February': 29,
  'March': 35,
  'April': 32,
  'May': 37,
  'June': 34,
  'July': 32,
  'August': 36,
  'September': 33,
  'October': 31,
  'November': 35,
  'December': 33
}

import math
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days31 = ["January", "March", "May", "July", "August", "October", "December"]
days30 = ["April", "June", "September", "November"]

month = input('Enter a month: ')
while month not in months:
  month = input('Enter a valid month: ')

year = input('Enter a year greater than 1582: ')
while float(year) < 1582:
  year = input('Enter a valid year: ')

day = input('Enter a day: ')
if month == "February":
  if float(year) % 4 != 0:
    while float(day) > 28:
      day = input('Enter a valid day: ')
if month in days30:
  while float(day) > 30:
    day = input('Enter a valid day: ')
if month in days31:
  while float(day) > 31:
    day = input('Enter a valid day: ')

VA = ['NO', 'No', 'nO', 'no'] 
print ("You entered {} {}, {}? Is this correct?".format(month, day, year))
Y_N = input("")

while Y_N in VA:
  
  month = input('Enter a month: ')
  while month not in months:
    month = input('Enter a valid month: ')

  year = input('Enter a year greater than 1582: ')
  while float(year) < 1582:
      year = input('Enter a valid year: ')

  day = input('Enter a day: ')
  if month == "February":
    if float(year) % 4 != 0:
      while float(day) > 28:
        day = input('Enter a valid day: ')
  if month in days30:
    while float(day) > 30:
      day = input('Enter a valid day: ')
  if month in days31:
    while float(day) > 31:
      day = input('Enter a valid day: ')
  print ("You entered {} {}, {}? Is this correct?".format(month, day, year))
  Y_N = input("")

if int(year) % 400 == 0 and int(year) % 4 == 0:
  #Calculation of Doomsday
  LTD = year[2:]
  FTD = year[:2]
  mil = FTD + "00"

  if int(mil) % 400 == 0:
    coeff = 2
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 100:
    coeff = 0
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 200:
    coeff = 5
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 300:
    coeff = 3
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7

  doom = doomsday_LY[month]
  day = int(day)

  #Declaration of Doomsday
  if Doomsday == 0:
    print ("Doomsday for {} {} was a Sunday".format(month, year))
    while day < doom:
      print ("{} is a Sunday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)

    if daydiff == 0:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Saturday".format(month, day, year))
    
  elif Doomsday == 1:
    print ("Doomsday for {} {} was a Monday".format(month, year))
    while doom > day:
      print ("{} is a Monday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Sunday".format(month, day, year))
    
  elif Doomsday == 2:
    print ("Doomsday for {} {} was a Tuesday".format(month, year))
    while doom > day:
      print ("{} is a Tuesday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Monday".format(month, day, year))

    elif Doomsday == 3:
      print ("Doomsday for {} {} was a Wednesday".format(month, year))
      while doom > day:
        print ("{} is a Wednesday".format(doom))
        doom -= 7
      daydiff = abs(doom - day)
  
      if daydiff == 0:
        print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    
  elif Doomsday == 4:
    print ("Doomsday for {} {} was a Thursday".format(month, year))
    while doom > day:
      print ("{} is a Thursday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    
  elif Doomsday == 5:
    print ("Doomsday for {} {} was a Friday".format(month, year))
    while doom > day:
      print ("{} is a Friday".format(doom))
      doom -= - 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Sunday".format(month, day, year))

  else:
    print ("Doomsday for {} {} was a Saturday".format(month, year))
    while doom > day:
      print ("{} is also a Saturday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Friday".format(month, day, year))
elif int(year) % 4 == 0:
  #Declaration of Doomsday
  #Calculation of Doomsday
  LTD = year[2:]
  FTD = year[:2]
  mil = FTD + "00"

  if int(mil) % 400 == 0:
    coeff = 2
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 100:
    coeff = 0
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 200:
    coeff = 5
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 300:
    coeff = 3
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7

  doom = doomsday_LY[month]
  day = int(day)
  
  if Doomsday == 0:
    print ("Doomsday for {} {} was a Sunday".format(month, year))
    while day < doom:
      print ("{} is a Sunday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Saturday".format(month, day, year))
    
  elif Doomsday == 1:
    print ("Doomsday for {} {} was a Monday".format(month, year))
    while doom > day:
      print ("{} is a Monday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Sunday".format(month, day, year))
    
  elif Doomsday == 2:
    print ("Doomsday for {} {} was a Tuesday".format(month, year))
    while doom > day:
      print ("{} is a Tuesday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Monday".format(month, day, year))

    elif Doomsday == 3:
      print ("Doomsday for {} {} was a Wednesday".format(month, year))
      while doom > day:
        print ("{} is a Wednesday".format(doom))
        doom -= 7
      daydiff = abs(doom - day)
  
      if daydiff == 0:
        print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    
  elif Doomsday == 4:
    print ("Doomsday for {} {} was a Thursday".format(month, year))
    while doom > day:
      print ("{} is a Thursday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    
  elif Doomsday == 5:
    print ("Doomsday for {} {} was a Friday".format(month, year))
    while doom > day:
      print ("{} is a Friday".format(doom))
      doom -= - 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Sunday".format(month, day, year))

  else:
    print ("Doomsday for {} {} was a Saturday".format(month, year))
    while doom > day:
      print ("{} is also a Saturday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Friday".format(month, day, year))
else:
#Calculation of Doomsday
  LTD = year[2:]
  FTD = year[:2]
  mil = FTD + "00"

  if int(mil) % 400 == 0:
    coeff = 2
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 100:
    coeff = 0
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 200:
    coeff = 5
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7
  elif int(mil) % 400 == 300:
    coeff = 3
    Doomsday = (coeff + int(LTD) + math.floor(int(LTD)/4)) % 7

  doom = doomsday_NLY[month]
  day = int(day)
#Declaration of Doomsday
  if Doomsday == 0:
    print ("Doomsday for {} {} was a Sunday".format(month, year))
    while day < doom:
      print ("{} is a Sunday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
    if daydiff == 0:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Saturday".format(month, day, year))
    
  elif Doomsday == 1:
    print ("Doomsday for {} {} was a Monday".format(month, year))
    while doom > day:
      print ("{} is a Monday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Sunday".format(month, day, year))
    
  elif Doomsday == 2:
    print ("Doomsday for {} {} was a Tuesday".format(month, year))
    while doom > day:
      print ("{} is a Tuesday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Monday".format(month, day, year))

    elif Doomsday == 3:
      print ("Doomsday for {} {} was a Wednesday".format(month, year))
      while doom > day:
        print ("{} is a Wednesday".format(doom))
        doom -= 7
      daydiff = abs(doom - day)
  
      if daydiff == 0:
        print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    
  elif Doomsday == 4:
    print ("Doomsday for {} {} was a Thursday".format(month, year))
    while doom > day:
      print ("{} is a Thursday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    
  elif Doomsday == 5:
    print ("Doomsday for {} {} was a Friday".format(month, year))
    while doom > day:
      print ("{} is a Friday".format(doom))
      doom -= - 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Friday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Sunday".format(month, day, year))

  else:
    print ("Doomsday for {} {} was a Saturday".format(month, year))
    while doom > day:
      print ("{} is also a Saturday".format(doom))
      doom -= 7
    daydiff = abs(doom - day)
  
    if daydiff == 0:
      print ("{} {} {} was a Saturday".format(month, day, year))
    elif daydiff == 1:
      print ("{} {} {} was a Sunday".format(month, day, year))
    elif daydiff == 2:
      print ("{} {} {} was a Monday".format(month, day, year))
    elif daydiff == 3:
      print ("{} {} {} was a Tuesday".format(month, day, year))
    elif daydiff == 4:
      print ("{} {} {} was a Wednesday".format(month, day, year))
    elif daydiff == 5:
      print ("{} {} {} was a Thursday".format(month, day, year))
    elif daydiff == 6:
      print ("{} {} {} was a Friday".format(month, day, year))