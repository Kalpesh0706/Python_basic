#nexted if
#WRITE A PROGRAMME TO  PROCESS PDF FILE FOR COPPER, GOLD AND IRONORE
'''file -->


copper.pdf  --> process

copper .excel --> '''

'''a = input("Enter the file name : ").lower()
if a.endswith(".pdf"):
    if a.startswith("copper"):
        print(f"processing {a}")
    elif a.startswith("gold"):
        print(f"processing {a}")
    elif a.startswith("ironore"):
        print(f"processing {a}")
    else:
        print(f"invalid file {a}")
else:
    print("enter the  valid filename")   #self

filename = input("Entert the filename:")

if filename.endswith('.pdf'):
    if filename.startswith('copper'):
        print(f"Processing {filename}")
    elif filename.startswith('gold'):
        print(f"Processing {filename}")
    elif filename.startswith('IronOre'):
        print(f"Processing {filename}")
    else:
        print("Invalid pdf file")
else:
    print("Please check file ")
'''
'''bonus:

sal
check
pune --> gen
M - - 5
F - 10

mumbai --> gen --> M - -15
F - 30

other --> gen -->  M - 25
F - 35'''

'''print("Welcome to  Bonus calculator")
salary = int(input("Enter your salary: "))
city = input("Enter your city: ").lower()
gender = input("Enter your gender M/F: ")[0].lower()

if city =='pune':
    if gender == 'm':
        bonus = '5%'
        totalsalary1 =salary/100*5
        bonus1 = totalsalary1+salary
        print(f"Your salary before bonus was {salary} and inculding {bonus} the total salary is {bonus1}")
    else:
        bonus = '10%'
        totalsalary2 = salary/100*10
        bonus2 = totalsalary2+salary
        print(f"Your salary before bonus was {salary} and inculding {bonus} the total salary is {bonus2}")
elif city=='mumbai':
    if gender=='m':
        bonus ='15%'
        totalsalary3=salary/100*15
        bonus3= totalsalary3+salary
        print(f"Your salary before bonus was {salary} and inculding {bonus} the total salary is {bonus3}")
    else:
        bonus='30%'
        totalsalary4=salary/100*30
        bonus4 = totalsalary4+salary
        print(f"Your salary before bonus was {salary} and inculding {bonus} the total salary is {bonus4}")
else:
    if gender=='m':
        bonus='25%'
        totalsalary5=salary/100*25
        bonus5 = totalsalary5+salary
        print(f"Your salary before bonus was {salary} and inculding {bonus} the total salary is {bonus5}")
    else:
        bonus ='35%'
        totalsalary6=salary/100*35
        bonus6 = totalsalary6+salary
        print(f"Your salary before bonus was {salary} and inculding {bonus} the total salary is {bonus6}")
print("Thank you for  using our service")  


#self

'''
'''if city=='pune':
    if gen=='m':
        bonus = (sal/100)*5
        gross_sal = sal+bonus
        print("Original Sal Before Bonus :",sal)
        print("Bonus:",bonus)
        print("Total Sal:",gross_sal)
    else:
        bonus = (sal/100)*10
        gross_sal = sal+bonus
        print("Original Sal Before Bonus :",sal)
        print("Bonus:",bonus)
        print("Total Sal:",gross_sal)
elif city=='mumbai':
    if gen=='m':
        bonus = (sal/100)*15
        gross_sal = sal+bonus
        print("Original Sal Before Bonus :",sal)
        print("Bonus:",bonus)
        print("Total Sal:",gross_sal)
    else:
        bonus = (sal/100)*30
        gross_sal = sal+bonus
        print("Original Sal Before Bonus :",sal)
        print("Bonus:",bonus)
        print("Total Sal:",gross_sal)
else:
    if gen=='m':
        bonus = (sal/100)*25
        gross_sal = sal+bonus
        print("Original Sal Before Bonus :",sal)
        print("Bonus:",bonus)
        print("Total Sal:",gross_sal)
    else:
        bonus = (sal/100)*35
        gross_sal = sal+bonus
        print("Original Sal Before Bonus :",sal)
        print("Bonus:",bonus)
        print("Total Sal:",gross_sal)'''




