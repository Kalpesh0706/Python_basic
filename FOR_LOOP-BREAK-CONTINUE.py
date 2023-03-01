#LCS

'''break -- statement it will terminate loop

continue'''
#NEED ONLY INT PRISE
'''
prd_price = [54,46,75,235,7,'dsf',65,35,6756,'rry']
x = ()
for i in prd_price:
    if type(i)==int:
        print(f"processing {i}")
    else:
        break
print("out side loop")'''


#seq - data -->invalid --> loop terminate
#print even number and  break if found  odd
'''
p = [2,4,8,10,5,44,48]
for i in p:
    if i%2==0:
        print(f"even number  processing  {i}")
    else:
        break
print("loop break")'''

'''
p = [2,4,8,10,5,44,48]
odd = []
for  i in p:
    if i%2==0:
        print(f"even number {i}")
    else:
        odd.append(i)
        continue
print(odd)'''

#break statement --loop terminate
#continue -->skip the iteration

'''
account --> number --


data
500+ aircrafts

rent engine
data IOT data collect --> mistake

ML email,sms -push message

standard data --ML -- train

born -6 data --> fed-  train -- test
account -- name - break

invalid --> continue '''

#logic
for i in range(0,3): #row
    for j in range(0,3): #col
        print("*",end = ' ')
    print()
    for i in range(1,6):
        for j in range(i,0,-1):
            print("*",end=' ')
    print()
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

