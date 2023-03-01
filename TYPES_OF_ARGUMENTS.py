#Types of Arguments
# 1.positional arguments
# 2.default arguments
# 3.variable length arguments(*args)
# 4.keyword arguments
# 5.variable length keyword arguements(**Kwargs)

# 1.positional arguments

'''def car_details(name,price,color,mil,a,b):
    print("Name:",name)
    print("Price:",price)
    print("Color:",color)
    print("Mil:",mil)
car_details('BMW',75151,"Red",848,2,4)'''

'''
def car_details(name,price,color,mil,a,b):
    print("Name:",name)
    print("Price:",price)
    print("Color:",color)
    print("Mil:",mil)
car_details('BMW',75151,"Red",848,2,4)
'''

#default argument
'''def personal_details(name,age,sal,*marks,pan='-',aadhar="-"):
    print("Name:",name)
    print("Age:",age)
    print("Sal:",sal)
    print("Marks:",marks)
    print("PAN:",pan)
    print("Aadhar:",aadhar)
personal_details('Jon',25,75000,10,20,30,40)
Name: Jon
Age: 25
Sal: 75000
Marks: (10, 20, 30, 40)
PAN: -
Aadhar: -'''


'''

personal_details('justin',26,15616,None,161616)
Name: justin
Age: 26
Sal: 15616
PAN: None
Aadhar: 161616

personal_details(None,None,None,None,1616)
Name: None
Age: None
Sal: None
PAN: None
Aadhar: 1616
'''


# variable length argument
'''def test(*arg):# maths
    print(arg)
test(10,161,156,156,1,6,16,16,16,16,16,1,61,61,616,16)
(10, 161, 156, 156, 1, 6, 16, 16, 16, 16, 16, 1, 61, 61, 616, 16)'''


#addition function for  a given list
'''def addi(*n):
    total = 0
    for i in n:
        total = total + i
    print(f"Addition {total}")
addi(2,3)  '''  #self


#keyword arguemnts
'''def personal_details(name,age,sal,city,pan,aadhar='----'):
    print("Name:",name)
    print("Age:",age)
    print("Sal:",sal)  
    print("PAN:",pan)
    print("Aadhar:",aadhar)
    print("city:",city)'''


'''personal_details(pan='156156',name='Jacky',age=25,city='Pune',sal= 7161616)
Name: Jacky
Age: 25
Sal: 7161616
PAN: 156156
Aadhar: ----
city: Pune
'''


# positional --> arguments less
#
# keyword --> arguemnt more than
'''
def personal_details(**kwargs):
    print(kwargs)
personal_details(name='akash',age=6,city='Pune')
{'name': 'akash', 'age': 6, 'city': 'Pune'}'''

'''personal_details(username='Admin',password='Admin')
{'username': 'Admin', 'password': 'Admin'}'''


# interview question:
#
# *arg --> variable length arguments --> tuple
# **kwargs --> variable length keyword arguments --dict




