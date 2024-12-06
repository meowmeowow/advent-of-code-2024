from collections import OrderedDict
import itertools


file=open('5.txt')
file1=open('5-1.txt')

data= [r.split('|') for r in [r for r in file.read().split("\n")]]
data1= [r.split(',') for r in [r for r in file1.read().split("\n")]]
dictT = {}
correctLists = []
incorrectLists = []

for dataPoint in data:

    if dataPoint[1] in dictT:
        dictT[dataPoint[1]].append(dataPoint[0])
    else:    
        dictT[dataPoint[1]] = [(dataPoint[0])]

for lists in data1:
    alreadIN = []
    for i in range(len(lists)):
        dataPoint = lists[i]
        if dataPoint in alreadIN:
            incorrectLists.append(lists)
            break
        
        
        if dataPoint in dictT:
            for index in dictT.get(dataPoint):
                alreadIN.append(index)

        if(i == len(lists)-1):
            correctLists.append(lists)

summ = 0
for lists in correctLists:
    index = len(lists)//2
    summ += int(lists[index])
print(summ)

summ2= 0




for lists in incorrectLists:
    dictProblem2 = {}
    for element in lists:
        needtobebefore = dictT[element]
        count = 0
        for thing in needtobebefore:
            if(thing in lists):
                count +=1
        dictProblem2[element] = count
    dictProblem2 = dict(sorted(dictProblem2.items(), key=lambda item: item[1]))

    listOfKeys = list(dictProblem2.keys())

    summ2 += int(listOfKeys[len(listOfKeys)//2])

print(summ2)

