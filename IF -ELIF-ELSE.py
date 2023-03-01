

#FLOW  CONTROL  STATEMENT
'''
print("hi")
print("bye")
print("hi welcome again")'''

#THE  ABOVE  IS  PRINT IN SEQUENCE
#WE CAN CHNAGE THE  FLOW  EXECUTION DEPENDING ON CONDITION

'''
IF simple 
IF - ELSE
IF - ELSE (LADDER)
NESTED IF - ELSE 
'''

#syntax
'''
if condition:
   body
'''

'''
if condition:
    sdgdfgdf
    gdf
    h
    dfsh
    fgsh
    sh
print()''' #this is not a part of if it should be inside the  if
'''
print("welcome to dose checking programe.")
age = int(input("Enter the  age:"))
if age > 50:
    print(f"As your age is  {age} please take  your  booster dose")
else:
    print(f"You are not eligible")
print("Thanks for visiting")'''

'''
print("welcome to dose checking program")
age = int(input("Enter the age:"))
if age>50:
    print("Please take booster on priority")
print("Thanks")

welcome to dose checking program
Enter the age:75
Please take booster on priority
Thanks

print("statement 1")
print("statement 2")
a = 56
if a>10:
    print("statement 3")
print("statement 4")

statement 1
statement 2
statement 3
statement 4
'''

'''email = input("Enter your email:")
if email.endswith('gmail.com'):
    print(f" {email} is a valid Email")
else:
    print("Not a valid email")
print("thanks for checking")'''

#if we have only one condition we use simple if

'''
if--- else
'''
#when we have more then  one  condition then we can use  if -else

#syntax
'''
if condition:
    body
else:
    body
'''

#if -else
'''
two condition --> if -else
if condition: True #Fasle
    body
else: #False True
    body'''

'''a = int(input("enter the  number:"))
if a%2==0:
    print(f" {a} is even number")
else:
    print(f"{a} is an odd number")
print("Thanks for checking")'''

#display 'addition of 10 and 20 is 30
'''a = 20
b = 20
c = a+b

print(f"Addition of {a} and {b} is {c}")
print( 'Addition of {} and {} is {}'.format(a,b,c))'''

'''dynamic content insert str -- format'''

#only  process the  pdf and txt  file

'''print("welcome to  file  check system")
a = input("Enter the  file name ")
if a.endswith(".pdf") or a.endswith(".txt"):
    print(f"Processing your {a} file")
else:
    print("Enter the  valid file name")
print("Thanks  for checking")'''

#if the  requirement increases

'''print("welcome to  file  check system")
a = input("Enter the  file name ")
if a.split('.')[1] in ['pdf','txt']:
    print(f"Processing your {a} file")
else:
    print("Enter the  valid file name")
print("Thanks  for checking")'''

'''a = 'sas.xlsx'
print(a.split('.')[1])'''

#simple if

'''
only one condition

if-else 

two condition'''

#if - elif - else
'''
if condition1:
    body1
elif condition2:
    body2
elif condition3:
    body3
elif condition4:
    body4
    |
    |
    |
    elif condition
    n:
    bodyn

else:
    default
'''

'''Note:else never having condition.
switch statement: No 
standard code 

Task :
    PEP8 documentation
grade :: calculation'''

#40-55 C
#56 - 65 B
#65 - 75 A
#75 - 100 A+
#40 below fail



'''a = float(input("Please enter your grade:"))
if a < 40:
    print(f'{a} fail')
elif a >= 40 and a<=55:     #strict block
    print(f"{a} c grade")
elif a > 55 and a<=65:
    print(f"{a} b grade")
elif a > 65 and a<=75:
    print(f"{a} a grade")
elif a > 75 and a<=100:
    print(f"{a} a+ grade")
else:
    print("enter valid grade")
print("thanks for using our service")'''


#LICENSE CALCULATOR
'''
BELOW 7 NOT A LOGICAL AGE
7 - 17 NOT ELIGIBLE
18 WE WILL DECIDE 
19 - 100 CAN  HAVE THE  LICENSE

'''
'''print("welcome to driving license department")
a = int(input("Enter your Age:"))
if a <7:
    print(f"{a} not a logical age")
elif a>=7 and a<=17:
    print("You  are not eligible for  driving license ")
elif a==18:
    print("At this  age you  need to  visit the office and  give  a  driving test")
elif a>18 and a<=100:
    print("You are eligible for driving license")
else:
    print("enter the  valid  age")
print("Thank you for using our service")'''

# write a programme to  calculate bonus  for  pune, mumbai and  other , if  pune  then  for  male
# 5% female 10%, mumbai  male 15% female 30% and  for other male 25% and  female 35%

print('Welcome to  bonus  calculation: ')
city = input('Enter your  city: ').lower()
gender = input(' Enter your Gender: ').lower()
salary = float(input("Enter your  salary: "))

if city == "pune":
    if gender == "male":
        bonus = salary / 100 * 5
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 5% bonus the total salary is : {totalsalary}')
    else:
        bonus = salary / 100 * 10
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 10% bonus the total salary is : {totalsalary}')
elif city == "mumbai":
    if gender == "male":
        bonus = salary / 100 * 15
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 15% bonus the total salary is : {totalsalary}')
    else:
        bonus = salary / 100 * 30
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 5% bonus the total salary is : {totalsalary}')
else:
    if gender == "male":
        bonus = salary / 100 * 25
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 15% bonus the total salary is : {totalsalary}')
    else:
        bonus = salary / 100 * 35
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 5% bonus the total salary is : {totalsalary}')

# write a programme to  calculate bonus  for  pune, mumbai and  other , if  pune  then  for  male
# 5% female 10%, mumbai  male 15% female 30% and  for other male 25% and  female 35%

print('Welcome to  bonus  calculation: ')
city = input('Enter your  city: ').lower()
gender = input(' Enter your Gender: ').lower()
salary = float(input("Enter your  salary: "))

if city == "pune":
    if gender == "male":
        bonus = salary / 100 * 5
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 5% bonus the total salary is : {totalsalary}')
    else:
        bonus = salary / 100 * 10
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 10% bonus the total salary is : {totalsalary}')
elif city == "mumbai":
    if gender == "male":
        bonus = salary / 100 * 15
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 15% bonus the total salary is : {totalsalary}')
    else:
        bonus = salary / 100 * 30
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 5% bonus the total salary is : {totalsalary}')
else:
    if gender == "male":
        bonus = salary / 100 * 25
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 15% bonus the total salary is : {totalsalary}')
    else:
        bonus = salary / 100 * 35
        totalsalary = salary + bonus
        print(f'Your old salary is : {salary} and after 5% bonus the total salary is : {totalsalary}')









