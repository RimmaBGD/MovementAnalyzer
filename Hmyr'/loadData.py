'''
Created on 26 дек. 2014 г.

@author: Римма
'''
data= open('sensor 1.txt')
dataX = []
for line in data.readlines():
    a=line.split(';')
    dataX.append(a[2])

print(dataX)
