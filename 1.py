import math
#read file
file=open('1.txt')
data= [r.split() for r in [r for r in file.read().split("\n")]]
data = [list(map(int, i)) for i in data]
data = ([*zip(*data)])

data = [list(data[0]),list(data[1])]

data[0].sort()
data[1].sort()

totalDistance = 0
totalSim = 0

elementMap = {}

for i in range(len(data[1])):
    if data[1][i] in elementMap:
        elementMap[data[1][i]] = elementMap.get(data[1][i])+1
    else:
        elementMap[data[1][i]] = 1


for i in range(len(data[0])):
    totalDistance+=abs(data[0][i]-data[1][i])
    currentElement = data[0][i]

    if(data[0][i] in elementMap):
        totalSim += elementMap.get(data[0][i])*data[0][i]



print(totalDistance)
print(totalSim)
