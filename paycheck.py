# program using Python3 to prompt the user for their name, hourly wage, and the hours they worked each day for a pay period and calculates the user's take home pay!
# 
DoW = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# Introduction
name = input("Time to begin calculating your net pey! May I have your name please? ")

print ("Ah! So your name is {} and you want to calculate your net pay. Please follow the following prompts".format(name))

while True: 
  try:
    wage = float(input("May I have your hourly wage please? "))
    break
  except:
    print("Please type in a number!")
print("\n")    
# STEP 1: Prompt for how many hours worked on each day of the week
# Begin week 1 prompting
W1L = [] #W1L is list which holds all hours worked each day
print("Enter hours of week 1")
for i in range(7):
    while True: 
      try:
        day = float(input("How many hours did you work {}? ".format(DoW[i])))
        W1L.append(day)
        break

      except:
        print("Please type in a number!")
W1HT = sum(W1L) #W1HT = Week 1 Hourly Total
print ("Your total hours for week 1 of this pay period is {} hours".format(W1HT))
print("\n")

# Begin week 2 prompting:
W2L = [] # W2L is a list which holds all hours worked each day
print("Enter hours of week 2")

for i in range(7):
    while True: 
      try:
        day = float(input("How many hours did you work {}? ".format(DoW[i])))
        W2L.append(day)
        break

      except:
        print("Please type in a number!")
W2HT = sum(W2L) #W2HT = Week 2 Hourly Total
print ("Your total hours for week 2 of this pay period is {} hours".format(W2HT))

# STEP 3: Calculate hours per week:
if W1HT > 40:
  OTH1 = W1HT - 40
  W1SG = round(400 + (OTH1 * (wage*1.5)), 2)
	
else:
  W1SG = round(W1HT * wage, 2)
  
if W2HT > 40:
  OTH2 = W2HT - 40
  W2SG = round(400 + (OTH2 * (wage*1.5)), 2)
	
else:
  W2SG = round(W2HT * wage, 2)
PPHT = round(W1HT + W2HT, 2) #PPHT = Pay Period Hours Total
TWSG = W1SG + W2SG #TWSG = Total Wage Salary Gross
print ("\n")
print ("{}, your total hours for this pay period is {} hours".format(name, PPHT))
print ("{}, your gross wages for this pay period is ${}".format(name, TWSG))

# STEP 4: Calculate Fed Witholding.
print("\n")

if TWSG > 0 and TWSG < 9275:
  HOL = round(TWSG * .10)
elif TWSG > 9276 and TWSG <= 37650:
  HOL = round(TWSG - (927.50 + ((TWSG - 9275)(0.15 * TWSG))))
elif TWSG > 37651 and TWSG <= 91150:
  HOL = round(TWSG - (5183.75 + ((TWSG - 37650)(0.25 * TWSG))))
elif TWSG > 91151 and TWSG <= 190150:
  HOL = round(TWSG - (18558.75 + ((TWSG - 91150)(0.28 * TWSG))))
elif TWSG > 190151 and TWSG <= 413350:
  HOL = round(TWSG - (46278.75 + ((TWSG - 190150)(.33 * TWSG))))
elif TWSG > 413351 and TWSG <= 415050:
  HOL = round(TWSG - (119934.75 + ((TWSG - 413350)(.35 * TWSG))))
else:
  HOL = round(TWSG - (120527.75 + ((TWSG - 415000)(.396 * TWSG))))
print ("Federal income tax is ${}".format(HOL))  

# STEP 5: Calculate Fed MED/EE
MED = round(0.0145 * TWSG, 2)
print ("Medicare tax is ${}".format(MED))

# Step 6: Calculate Fed OASDI/EE
OAS = round(0.062 * TWSG, 2)
print ("Social Secuity tax is ${}".format(OAS))

# Step 7: Calculate Net Pay
WNP = round(TWSG - (HOL + MED + OAS),2)
print ("{}, your net pay is ${}".format(name, WNP))
