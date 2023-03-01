#compression:

'''coding:
code
optimize
list
'''
import pandas as pd

'''compression --> list

dict - --> dict

tuple - --> not applicable in python --> generator
object'''

#loop + condition --> list c
#Q1 Need even number
'''
p = [45,86,35,97,35,976,459]
even = []
for  i in p:
    if i%2==0:
        even.append(i)

print(even)'''
#normal loop

#by using list compression
#if we need to  use  loop + condition we can use  list compression
'''
p = [45,86,35,97,35,976,459]
a = [i for i in p if i%2==0]
print(a)'''
#using list compression

#Q2 only pdf fetch?
'''
p = ['test.pdf','tert.xlsx','sample.pdf','sdafsd.txt']
a = [i for i in p if i.endswith(".pdf")]
print(a)'''
#self

#==================pandas========pandas=========pandas===============

'''
d = {'name':['redr','sdfsdf','sfsdf'],
    'id':[35,46,4],
     'sal':[64645,64646,3456456]}
import pandas as pd

df = pd.DataFrame(d)
print(df)'''
#import pandas as pd(alias) then take a variable and type pd.DataFrame(disct)

#jason into tabular format
'''
a = pd.read_json('https://api.sampleapis.com/wines/reds')
print(a)'''

#not get the  selected  colums  using  list  compression
'''
a = pd.read_json('https://api.sampleapis.com/wines/reds')    #get the jason link 
b = [colname for colname in a if colname in ['winery','wine','rating']]   #apply filter on column 
a[b]
print(a[b])'''


#Q3 output exp = [1,2,3,4,5,6,7,8,9]
'''
temp = [[1,2,3],[4,5,6],[7,8,9]]
list = []
for i in temp:
    for j in i:
        list.append(j)
print(list)'''
#self normal


#using list compression
'''
temp = [[1,2,3],[4,5,6],[7,8,9]]
a = [j for i in temp for j in i]
print(a)'''
#self


#Q4 need a  file name  using list  compression
'''
p=['test.pdf', 'tert.xlsx', 'sample.pdf', 'sdafsd.txt']
a = [i.split('.')[0] for i in p]
print(a)'''
#logic

#==================time taken================time taken===========================
'''
import time

temp = [[1,2,3],[4,5,6],[7,8,9]]
list = []
starttime= time.time()
for i in temp:
    for j in i:
        time.sleep(2)
        list.append(j)
print(list)
endtime= time.time()
print("time taken",endtime-starttime)'''

#============================================================================

#list compression --> script --> lambda ,list ,function,class,module,package

#=========================disct============disct==============================
#dict compression
#Q1 make into disct?
'''
p = {1,2,3,4}
a = {i:i for i in p}
print(a)'''

#Q2 need file name and extention example filename : extentoin
'''
p =['test.pdf', 'tert.xlsx', 'sample.pdf', 'sdafsd.txt']
a = { i.split(".")[0]:i.split(".")[1] for i in p}
print(a)'''
#self


#Q3 need file name and extention example filename : extentoin and only  pdf file

'''
p =['test.pdf', 'tert.xlsx', 'sample.pdf', 'sdafsd.txt']
a = {i.split(".")[0]:i.split(".")[1] for i in p if i.split(".")[1] in 'pdf'}   #self
b  = {i.split(".")[0]:i.split(".")[1] for i in p if i.endswith("pdf")}
print(a)
print(b)'''

#=====================================tuple=========tuple=====================================
'''
temp = [1,2,3]
p = (i for i in temp )
p'''
#<generator object <genexpr> at 0x0000026731B17F90>


#type(p)
#generator

