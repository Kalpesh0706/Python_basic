'''loop statement

for loop
while loop'''


#Note: do while is not present in python


#FOR LOOP

'''for loop variable in seq:  # seq/list/tuple/set/dict/str
    body 
'''

'''
py_list = ['Python','Java','ML','Hadoop','DS','SQL']
for i in py_list:
    print(i)   #in row

for i in py_list:
    print(i,end=' ')  #in one line'''

'''
print('Hi',end=' ')
print('Bye',end = ' ')
print('Welcome',end = ' ')
print("Again")

Hi Bye Welcome Again

for element in py_list:
    print(element,end=' ')
py = [1,5,9,3,9,3,9,4]
'''
'''
py = [1,5,9,3,9,3,9,4]
for i in py:
    if i%9==0:
        print(i)'''
'''
for i in py:
    print(i)
1
5
9
3
9
3
9
4

py = [1,2,3,4,5,6,7,8,9,10]
for komal in py:
    print(komal*9)
9
18
27
36
45
54
63
72
81
90

p = {3,8,3,9,3,8945,'python','java'}

p
{3, 8, 8945, 9, 'java', 'python'}

for i in p:
    print(i)
8945
3
8
9
java
python'''

#loop+control statement -->
#need gmail id
'''emails = ['afsdaf@gmail.com','asdfsdf@yahoo.com','asfsdf@gmail.com','abc','asfsadf','asfsd@gmail.com']
for  i in emails:
    if i.endswith('gmail.com'):
        print(f"valid ID {i}")'''
#need gmail, yahoo
#emails = ['afsdaf@gmail.com','asdfsdf@yahoo.com','asfsdf@gmail.com','abc','asfsadf','asfsd@gmail.com']

'''
for email in emails:
    if email.endswith('gmail.com') or email.endswith('yahoo.com'):
        print(f"Valid email : {email}")
    else:
        print(f"Invalid email : {email}")'''

'''
py_list = [34,86,24,83,86,24,90,24,782,546,8,7,34,97,23,86,24,756,35,57]

even= []
odd = []
for i in py_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)'''     #self

#access only  pdf
files = ['test.pdf','sample.xlsx','test.txt','test1.pdf']

'''
pdf = []
for i in files:
    if i.endswith(".pdf"):
        pdf.append(i)
print(pdf)'''

#range(start,stop,step)
'''
default:
    start=0
    step = 1
for i in range(1,11):
    print(i)
1
2
3
4
5
6
7
8
9
10
'''
'''for i in range(-1,5,-1):
    print(i)'''  #blank

