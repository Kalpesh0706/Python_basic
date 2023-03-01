#
# def test(name,age):
#     print("name:",name)
#     print("age:",age)
# test('Python',32)
# name: Python
# age: 32
# def cal_fact(no):
#     i = no
#     fact =1
#     while i>=1:
#         fact = fact*i
#         i-=1
#     return fact
# temp = cal_fact(0)
# temp
# 1

'''def test(name,age):
    print("name:",name)
    print("age:",age)
test('Python',32)
name: Python
age: 32'''
import mouseinfo

'''def cal_fact(no):
    i = no
    fact =1
    while i>=1:
        fact = fact*i
        i-=1
    return fact
temp = cal_fact(5)
print(temp)'''

# Types of function:
#
# No arguments and No return values
# With arguments and No return values
# With arguments and with return values ----> IMP
# No arguments and with return values


# No arguments and No return values
'''
def test():
    a = 45
    b = 95
    print(a+b)
test()
140'''


# With arguments and No return values
'''
def test(a,b,c):
    print(a,b,c)
test(45,90,63)
45 90 63
'''

# With arguments and with return values   important
'''
def test(a,b,c):
    return a+b+c
r = test(49,1,64189)
r
64239
'''

#No arguments and with return values
'''def test():
    a=3
    b=4
    return a+b
result = test()
print(result)'''


mouseinfo.getPixel(23,45)
