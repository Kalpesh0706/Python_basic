


# variable types:
#     1.local variable -> scope within the function only
#     2.global variable -> scope throught the program or script
'''

def test():
    a = 10
    b= 50
    print(a)
    print(b)
test()
10
50'''


'''
a = 100

def t1():
    x = 49849
    print(a)
    print(x)
    return x

def t2():
    y = 1616
    print(a)
    print(x)

def t3():
    z = 21616
    
t2()
100

'''

# within the function --> local only accessable within function only
#
# global -- variable access inside the program or anywhere in the program


'''
p = t1()
100
49849
p
49849'''


# real time python code standard
#
# shebang
#
# doc string
#
# import library
#
# global section:
# global variable define
#
# def function1():
#     body
#
# def function2():
#     body
#
#
# def mainfunction():
#     body
#
#
# if __name__=='__main__':
#     main()


# global keyword

'''def test():
    def m1():
        print("hi")
    

test()
m1()'''

# function --> secure


#global keyword
# 1.to access global variable inside function(when variable have same name)
# and to modify global variable with the function
# 2.to make local variable as global


'''course = 'Python'


def test():
    print(course)


def m1():
    print(course)


def m2():
    global course
    course = 'Hadoop'
    print(course)'''

#Answere
# test()
# Python
#
# m1()
# Python
#
# m2()
# Python
#
# m1()
# Python
#
# m2()
# Python
#
# test()
# m1()
# Hadoop
#
# m2()
# Hadoop
#
# course
# 'Hadoop'

'''def m4():
    global p1
    p1 = 450


def m5():
    global q
    q = 9491'''


# m4()
# p1
# 450
# p1
# 450
#
# m5()
# q
# 9491


'''a = 100
h = 4641
def t6():
    a = 500
    return a'''
# p9 = t6()
# p9
# 500


# global keyword
# globals()[var]

#function alicing
'''def test():
    print("Hi")
test123 = test'''
# test123()
# Hi



'''def sonali():
    print("Hi, How are You!")'''
# sonali()
# Hi, How are You!
#
# sona = sonali
#
# sona()
# Hi, How are You!


'''def add():
    x = 10
    y = 20
    print(x+y)'''
# add()
# 30
# sum1 = add
# sum1()
# 30


'''
def t1():
    def inner():
        print("Inside inner function")
    return inner
t = t1()
t()
Inside inner function
'''

'''
def temp():
    x = 100    
    return x
d = temp()
d
100
'''

