'''normal
repeatation
task
temp - - just
temporary
task

single
use

just in time

no
name
anonoumous
function

lambda input: output '''

#simple addition
'''a=(lambda x,y:x+y)(10,40)
print(a)'''

#ex
'''(x+y)^2 = x*x + 2*x*y + y*y
temp = (lambda x,y: x*x + 2*x*y + y*y)
temp(15,3)

324'''
#(a+b)^2 = a*a + 2*x*y + b*b

'''
lambda 


map
filter
'''

#Q1 square of each element present in  the list
'''
py_list = [2,8,6,9,34,8,3]
square= []
def sq():
    for i in py_list:
        q = i*i
        square.append(q)
sq()
print(square)'''
#self

'''
py_list = [2,8,6,9,34,8,3]
sqr = []
for i in py_list:
    sqr.append(i*i)
sqr
[4, 64, 36, 81, 1156, 64, 9]
'''
#notes

#using lambda (map) it interacts  with  each element
'''py_list = [2,8,6,9,34,8,3]
sq= []
def squ(i):     #function of square
  return i*i

a = list(map(squ,py_list))    #passed the  function and the sequence
print(a)'''


#Q2 square root using lambda
'''b =list(map(lambda x: x*x,py_list))
print(b)'''

#Q3 find the  length  of each  element in list
'''
py = ['java','python','hadoop','c']
a = list(map(lambda x : len(x),py))
print(a)
'''
#self

#Q4 need the  file name only not format?
'''pyfile = ['test.pdf','smaple.xlsx','test23.pdf','sdadsf.txt','asfsdf.pdf']
a = list(map(lambda x : x.split(".")[0],pyfile))
print(a)'''
#self


#Q5 only display  the  first  2 character from the  list
'''
p = ['px53454','pf46546','pt43654','px34534543']
a = list(map(lambda x:x[0:2],p))
print(a)
'''
#self

#seq --> element operation --> map /for
#========================FILTER================FILTER===============FILTER=================

#Q6 Find the  even  numbers
'''
p = [56,34,75,6354,75,45,75]
a= list(filter(lambda x: x%2==0,p))
print(a)'''
#self


#Q7 need only  pdf file
'''
pyfile=['test.pdf', 'smaple.xlsx', 'test23.pdf', 'sdadsf.txt', 'asfsdf.pdf']
a = list(filter(lambda x: x.endswith(".pdf"),pyfile))
print(a)'''
#self


#Q8 replace m with 1 and f with 0?   ========important interview important interview
'''
py = ['m','m','f','f','m','f']
a = list(map(lambda x: 1 if x=='m' else 0,py))
print(a)'''
#self


#Q9 Need only female?
'''
py = ['m','m','f','f','m','f']
a = list(filter(lambda x : x if x=="f" else False,py))
print(a)'''
#Self

#Q10 convert to  integer the below string
'''
p = ['3454','3454','67546','546547','3456346','4754756']
a = list(map(lambda x: int(x),p))
print(a)'''
#self


#pandas --> lambda ,map,filter  with example