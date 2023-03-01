
'''Types of Operator
1.Arithmetic Operator --> +,-,*,/,%,//,**
2.Comparision Operator /conditional operator ,<>=<=,!= ==
3.Logical Operator  and or not
4.Membership Operator in not in
5.Assigment Operator =,+=,-=,*=,/=
6.Identity Operator is ,not is
7.Bitwise Operator &  |  symbolic
8.ternary Operator --> abhi nahi  control statement'''


#membership
'''member ---> group----> list,tuple,set,dict,str'''
#IN and NOT IN
'''
li = [12,34,6,342,56,3,225,6,22,4]
print(12 in li)  #true
print(52 in li)  #false

print(12 not in li)  #false
print(52 not in li)  #true
'''

#Assignment

'''a = 10''' #it is storing the  value  10 in a it is assigning
'''a == 10''' #this is not assigining it is a comparison

#increment & decrement
'''a = 10
#increment 10 by 1
a = a +1  #increment
print(a)  #11

#we can  also  increment by  this
a += 1  #this is also increment
print(a)  #12
'''
'''we can use 
+=
-=
*=
/=
'''

#identity
'''a = 10
b = 10

print(id(a))  #1428820197904
print(id(b))  #1428820197904

print(id(10))  #1428820197904

print(a is b)  #true memory location
print(a==b)  #value compare'''

'''a = 5000
b = 5000

a is b
False

a==b
True

id(a)
2640747130512

id(b)
2640744632368

a=b=5000
id(a)
2640744632432

id(b)
2640744632432

a is b
True

a==b
True'''

'''#interview
is vs ==

memory location comparision vs value comparision'''

#Bitwise Operator

'''
AND (&) #SYMBOL
OR (|)  #SYMBOL
'''
'''45 & 6
4

8 & 10
8

8 | 10
10

7 | 14
15

bin(15)
'0b1111'

bin(7)
'0b111'

int(0b111)
7

oct(45)
'0o55'

int(0b11111111111111111111111111111111)
4294967295

int(0b111111)
63'''


