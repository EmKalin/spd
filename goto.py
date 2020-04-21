import os
import math
import copy
import heapq
import itertools



tab = [[2,3,4],[4,3,3],[1,4,5],[3,2,2]]
n = len(tab)
x = 2**n-1
print(x)

y=[]
while x>0:
    y.append(int(x % 2))
    x=int(x/2)

print(y)
#-----------------------------------------------------------
for i in range(0, len(y)):
    F=copy.deepcopy(y)
    F[i]=0
    print(F)
    result=F.index(0)
    print(result)

#for i in range(0, len(y)):
#    F = copy.deepcopy(y)
#    F[i] = '0'

#    print(F)


#def binarn(tablica):
#n = 2**len(tab)-1
#print(F)


#for i in range(0, n):
#    x=bin(n-i)
#    y=x[2:]
#    print(y)
#    f=[]
#    for  j in range(0, len(y)):
#        if y[j] == "1":
#            f.append(1)
#            #print("gówno")
#        else:
#            f.append(0)
#            #print("cipa")
#
#    if len(tab)>len(f):
#        for i in range(0,len(tab))
#    print(f)

#def binarn(y):
#    for i in range(0,len(y)):
#        F = copy.deepcopy(y)
#        F[i]=1

#        print(F)
#        if len(F)>0:
#            binarn(F)

#    return F



#binarn(y)
