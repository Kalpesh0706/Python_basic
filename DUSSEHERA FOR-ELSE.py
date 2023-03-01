#Only  process xlsx file
'''py_list = ['test.xlsx','sample.txt','flate.xlsx','demo.txt','copper.xlsx']

for i in py_list:
    if i.endswith("xlsx"):
        print(f"processing {i}")
    else:
        continue

a = list(filter(lambda a : a.endswith("xlsx"),py_list))  #lambda
print(a)'''

#p = [23,45,56,34,23,'sdf',23,324,3,'df',34,76,2436,'s','et']

'''for  i in p:
    if type(i)==int:
        print(f"processing {i}")
    else:
        break
'''
'''for  i in p:
    if str(i).isnumeric():  #isnumeric
        print(f"processing {i}")
    else:
        break'''  #break

'''for  i in p:
    if type(i)==int:
        print(f"processing {i}")
    else:
        print(f"invalid {i}")
        continue'''

'''for id in py:
    if str(id).isnumeric():
        print(f"Processing {id}")
    else:
        break
Processing 56
Processing 35
Processing 86
Processing 2
Processing 86
Processing 3
Processing 586
Processing 45
Processing 86
'fg'.isnumeric()
False
a = 'test'
list,set,str,dict,frozenset,tuple --> DS
 
 
a  = 'dfsdf'
a.isalpha()
True
a = '3435dfd'
a.isnumeric()
False
'3535'  numeric
'ssadf' alpha
'sdaf5353' - alphanumeric
 
#if -else
for -else
try-else
for -else --close friend

break  --> else nahi execute'''


py = [56,35,86,2,86,3,586,45,86,54654,'sdfsdfds',234,86,365,'dsfsd','safsda',454,646]
#py = [56,35,86,2,86,3,586,45,86,54654,234,86,365,454,646]
'''for i in py:
    if str(i).isnumeric():
        print(f"processing {i}")
    else:
        print(f"invalid data {i}")
        break
else:
    print(f"data executed  successfully")'''

'''b = []
for i in py:
    if str(i).isnumeric():
        print(f"processing {i}")
    else:
        b.append(i)
        continue
else:
    print(f"data executed  successfully")
print("Number of invalid data ",len(b))
print('Invalid data are',b)'''   #self

'''
py = [56,35,86,2,86,3,586,45,86,54654,'sdfsdfds',234,86,365,'dsfsd','safsda',454,646]
count = 0
valid_item = []
for id in py:
    if str(id).isnumeric():
        valid_item.append(id)
        print(f"Processing {id}")
    else:
        print(f"invalid item {id}")
        count+=1
        continue
else:
    print("Loop executed successfully")
    print("Total number of iteration skipped:",count)
    
'''

'''valid_item = [56, 35, 86, 2, 86, 3, 586, 45, 86, 54654, 234, 86, 365, 454, 646]
non_dup=[]
dup= []
for i in valid_item:
    if i not in non_dup:
        non_dup.append(i)
    else:
        dup.append(i)
print("The duplicate values are ",dup," and the  count is" , len(dup))
print(non_dup)'''  #self

'''
unique = []
duplicate = []
for i in valid_item:
    if i not in unique:
        unique.append(i)
        
    else:
        if i in duplicate:
            continue
        else:
            duplicate.append(i)
'''

'''
valid_item = [54,75,25,586,36,85,367,56,36,96,36,68,36,58,36,58,23,686,5235,657,234]
unique = []
duplicate = []
for i in valid_item:
    if i not in unique:
        unique.append(i)
    else:
        if i in duplicate:
            continue
        else:
            duplicate.append(i)
'''


#important
valid_item =[23,23,23,45,45,33,33,76,76,87,33,25,35,2,3,4,5,25]
#INTERVIEW QUEST
#NEED THE  COUNT OF EACH  ELEMENT  IN DISCT
#OUTPUT
#DICT = {12:2,15:4}
dis={}
for  i in valid_item:
    if i in dis:
        dis[i]+=1
    else:
        dis[i]=1
print(dis)


