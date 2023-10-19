n=int(input('enter the size of list T1 and T2 : '))
T1=[]
T2=[]
list=[]
#read the values ​​from the T1 list.
for i in range (n):
   value=int(input('Enter the value for T1['+str(i)+']:'))
   T1.append(value)

#read the values ​​from the T2 list.
for i in range (n):
   value=int(input('Enter the value for T2['+str(i)+']:'))
   T2.append(value)

for i in range (n):
   sum=T1[i]+T2[i]
   list.append(sum)   #this list is the result of the sum of T1 and T2 .

print('THE SUM OF T1 AND T2 IS ',list)
