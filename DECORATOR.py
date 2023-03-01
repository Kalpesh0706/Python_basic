
'''def m1():
    def m2():
        print("Hi")
    return  m2()

t2 = m1()

m1()'''
#function alising
import time

'''
Why function are using function alising?
'''


'''def decor(fun):
    def inner():
        print('*'*10)
        fun()
        print("*"*10)
    return inner


@decor
def show():
    print("kalpesh")

show()    #call'''


# tem=decor(name)
# tem()

#NEW DECORATOR

'''def x(a):
    def y():
        print("*"*20)
        a()
        print("*"*20)
    return y'''

'''@x
def fun():
    print("kalpesh")
fun()'''

#decorator of addition
'''@x
def add():
    a =10
    b = 20
    c = a + b
    print(f"Addition of {a} and {b} is  {c}")
add()'''

'''def proc(a):
    def inner():
        time.sleep(1)
        print("Connecting DB...")
        time.sleep(1)
        print("Establishing Connetion...")
        time.sleep(1)
        print("Connected to server")
        time.sleep(1)
        print("Import the file:")
        time.sleep(1)
        a()
        time.sleep(1)
        print("Thank you for using our service")

    return inner

@proc
def file():
    global g
    g=input("Enter the file Name: ").lower()
    if g.endswith(".pdf"):
        time.sleep(1)
        print(f"Processing {g}")
        time.sleep(1)
        print("Successfully Uploaded")
    else:
        time.sleep(1)
        print(f"The {g} file format is not supported")
        time.sleep(1)
        print("Upload Failed")




file()'''


#=================================================================

#connection --> cred --> read

#data fetch data base


#dump local database

'''def decor2(f):
    def inner():
        print("#"*15)
        f()
        print("#"*15)
    return inner





def decor1(f):
    def inner():
        print("*"*15)
        f()
        print("*"*15)
    return inner

def decor(f):
    def inner():
        print("read cred from file code")
        f()
        print("data dump code")
    return inner
@decor2
@decor1
@decor
def data_fetch():
    print("Actual data fetch code")


data_fetch()
###############
***************
read cred from file code
Actual data fetch code
data dump code
***************
###############

requirement

actual

task

@decor2
@decor1
@decor
def m1():
    print("darta sdfsdafs")
[14]
m1()
###############
***************
read cred from file code
darta sdfsdafs
data dump code
'''