
#generator
#it is  used to  generate  sequence of number

#range
#it is  also  used for  generating sequence of number

#Q1 What  is  difference between  range  and  generator ?
'''
range when generate  elements it is store in a list
'''
#Ex
'''
p = list(range(15))
print(p)
'''
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#program logic
#data process

#generator

'''
def temp():
    yield
'''
#syntax

'''
def temp():
    yield "A"

p = temp()
print(type(p))
'''
#<class 'generator'>

'''
def temp():
    return "A"

p = temp()
print(type(p))
'''
#<class 'str'>

'''
object---> pointer
'''
'''def temp():
    yield "A"
    yield "b"
    yield "c"

p = temp()
print(type(p))
print(next(p))
print(next(p))
print(next(p))'''

#huge amount rows iterate

#files---read---line by line

#stopiteration--> EOF

#object
'''for i in range(999999999999999999999999999999)  this range actually store the values then execute one by  one 
       print(i)                                     '''
    #SyntaxError: expected memory error ':'

'''
def temp(n):
    i = 0
    while i<=n:
        yield i
        i=i+1'''
'''obj = temp(999999999999999999999)'''  #in this  case object is  getting  create start point is 0 and  end 9999999999  point
'''for i in obj:
    print(i)'''

#at atime it generates one  element

#Q1 generate  50 rec and have to iterate one by one by generator?

'''def a(n):
    i = 0
    while i<=n:
        yield i
        i = i+ 1

obj = a(50)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print("loop")
for i in obj:
    print(i)'''

#yield is  oly use in generator it act as a retun as  well in generator
# in return whatever the  values is there it will return  once and can be called out of the  function in  generator  it  cannot be  called  out of the  function
#we use yield  to  optimise the  memory


#iterator
#q2 in iterator  and  generator which  memory  is efficient ?
#generator is  more  efficient  then iterator


'''
iterator applies  on sequence list tuple  set  
'''
'''
p = [23,34,45,5,323,34]
obj = iter(p)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
'''
#StopIteration  list iterator

#set iterator
'''p = {21,34,34,5,23,23}
obj = iter(p)
print(type(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))'''
#<class 'set_iterator'>


#generator is used to generate element-->file read --->dataframe---to fetch one row  at a time
#iterator  is a wrapper  on list, tuple set




