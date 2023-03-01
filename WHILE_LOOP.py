
#for loop --> seq "group of values"

"condition based"
#while loop
#import pip
#import pyautogui
#import pywhatkit

'''while condition: # True - loop 
    body
'''

'''i=5 #start point

while i<=10: #condition
    print(i)
    i=i+1 #increament'''

#write a programe  to  add two numbers  from user input and ask do you  want to  add more

''''print("welcome to  addition programme")

while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    add = a+b
    print(f"The addition of {a} and {b} is {add}")
    choice = input("Do you want to  continue addition [Y,N]")[0].lower()
    if str(choice).isalpha():
        if choice=='n':
            print("Thank you for using our service")
            break
    else:
        print("Please enter in string")
        choice = input("Do you want to  continue addition [Y,N]")[0].lower()
        if str(choice).isalpha():
            if choice == 'n':
                print("Thank you for using our service")
                break
print("programe completed")
'''


#----------===========================--------------------------------------

'''file = 'asd.pdf'
while file.endswith('.pdf'):
    print(f"processing {file}")'''

'''
test = 'sample.pdf'

while test.endswith('pdf'):
    print("file process")
    test = 'sdfgsdfg'

file process
db -- data generator + while

Note : used within loop only --> loop control statement
break
continue 
'''

'''
file --> lines
file read --> file pointer --> EOF  reading terminate
data 1 M --> list memory --> Generator   while 
 

 
add 

no1 = int(input("Enter the number:"))
no2 = int(input("Enter the seconde number:"))
addition = no1+no2
print(f"Addition of {no1} and {no2} is {addition}")
1 .duplicate code
2.code mgmt
def function_name(arg/parameter):
    body
    return value/arg
 
def add():
    no1 = int(input("Enter the number:"))
    no2 = int(input("Enter the seconde number:"))
    addition = no1+no2
    print(f"Addition of {no1} and {no2} is {addition}")
add()
 
add()
Enter the number:45
Enter the seconde number:63
Addition of 45 and 63 is 108
 
add()
Enter the number:7996
Enter the seconde number:4496
Addition of 7996 and 4496 is 12492
 
 
 
 
def add(x,y): #formal arguemnt
    z = x+y
    print(z)
add(45,59) # actual argument
104


#difference print vs return
def add(x,y): 
    z = x+y
    print(z) 
 
add()
Enter the number:78
Enter the seconde number:64
Addition of 78 and 64 is 142

Note : once function created you can call it by no.of times



def grade_cal(per):
    
    if per<40:
        print("Sorry Please try again")
    elif per>=40 and per <=55:
        print("You are passed with C grade")
    elif per>55 and per<=65:
        print("You are passed with B grade")
    elif per>65 and per<=75:
        print("You are passed with A grade")
    elif per>75 and per<=100:
        print("You are passed with A+ grade")
    else:
        print("please enter valid per")
    print("Thanks for using our service")
grade_cal(96)
You are passed with A+ grade
Thanks for using our service
'''


'''
def file_test(filename):
    if filename.endswith('.pdf'):
        return True
    else:
        return False
'''
#make addition function

'''
def add():
    a=input("Enter the first number")
    b=input("Enter the second number")
    add= a + b
    print(f"the sum is {add}")
'''


'''
def add1(x,y):
    z = x+y
    return z
result = z
result
300
'''

#concatination function

'''def str_concat(firstname, lastname):
    s = firstname + "_" + lastname
    return s


result = str_concat('Test', 'pdf')
result
'Test_pdf'''''

#def function
'''def percent(a):
    #a = float(input("Please enter your grade:"))
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
    print("thanks for using our service")
    return a

per = percent(23)
print(per)



c = per
print(c)'''


#define a function to  pass the pdf  file

'''def filename(file):
    if file.endswith(".pdf"):
        #print(f"processing {file}")
        return True
    else:
        #print(f"invalid file {file}")
        return False

file = input("Enter the file  name ").lower()
a = filename(file)
if a == True:
    print(f"processing {file}")
else:
    print(f"invalid {file}")'''       #self


# script
#
#
# funct()
#
#
# funct()
#
#
# funct()
#
#
# main()
#
#
#
#
# if __name__=='__main__':
#     main()


# types of function :
#     strcture :
#         4
# types of parameter/arguments: