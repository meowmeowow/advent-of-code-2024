file=open('6.txt')
x= [list(r) for r in [r for r in file.read().split("\n")]]
pos = [0,0]

listOfPossibleData = []


for i in range (len(x)):
    for j in range(len(x[i])):
        if(x[i][j]==">" or x[i][j]=="^" or x[i][j]=="<" or x[i][j]=="v"):
            pos[0] = i
            pos[1] = j
        elif( x[i][j] != "#"):
            dataCopy = list(map(list, x))
            dataCopy[i][j] = "#"
            listOfPossibleData.append(dataCopy)
            #pass



        
loop = 0
startingPos = pos.copy()

print(len(listOfPossibleData))

#listOfPossibleData.append(x)


for data in listOfPossibleData:
    pos = startingPos.copy()
    dict_pos = {}
    dict_pos[str(pos[0])+" "+str(pos[1])] = x[startingPos[0]][startingPos[1]]
    while(1): 
        i = pos[0]
        j = pos[1]
        point = data[i][j]
        new_pos = [0,0]

        if_turn_new = ""
        if(point == "^"):
            if(i == 0):
                break
            new_pos[0] -= 1
            if_turn_new = ">"
        elif(point == "<"):
            if(j == 0):
                break
            new_pos[1] -= 1
            if_turn_new = "^"
        elif(point == ">"):
            if(j == len(data[0])-1):
                break
            new_pos[1] += 1
            if_turn_new = "v"
        elif(point == "v"):
            if(i == len(data)-1):
                break
            new_pos[0] += 1
            if_turn_new = "<"

        newCord = data[i+new_pos[0]][j+new_pos[1]]
        if(newCord == "#"):
            data[i][j] = if_turn_new
            point = if_turn_new
        else:
            pos[0] = i+new_pos[0]
            pos[1] = j+new_pos[1]

            data[pos[0]][pos[1]] = point

            data[i][j] = "."
        if(str(pos[0])+" "+str(pos[1]) not in dict_pos):
            
            dict_pos[str(pos[0])+" "+str(pos[1])] = point
        else:
            if(dict_pos[str(pos[0])+" "+str(pos[1])] == point):
                loop+=1
                break
#print(len(dict_pos))

print(loop)


