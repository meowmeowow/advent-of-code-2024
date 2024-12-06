file=open('6.txt')
data= [list(r) for r in [r for r in file.read().split("\n")]]

pos = [0,0]
dict_pos= {}

for i in range (len(data)):
    for j in range(len(data[i])):
        if(data[i][j]==">" or data[i][j]=="^" or data[i][j]=="<" or data[i][j]=="v"):
            pos[0] = i
            pos[1] = j
            break
        
dict_pos[str(pos[0])+" "+str(pos[1])] = 0

while(pos[0] > 0 and pos[0] < (len(data)-1) and pos[1] > 0 and pos[1] < (len(data[0])-1)): 

    i = pos[0]
    j = pos[1]
    point = data[i][j]
    new_pos = [0,0]

    if_turn_new = ""
    if(point == "^"):
        new_pos[0] -= 1
        if_turn_new = ">"
    elif(point == "<"):
        new_pos[1] -= 1
        if_turn_new = "^"
    elif(point == ">"):
        new_pos[1] += 1
        if_turn_new = "v"
    elif(point == "v"):
        new_pos[0] += 1
        if_turn_new = "<"

    newCord = data[i+new_pos[0]][j+new_pos[1]]
    if(newCord == "#"):
        data[i][j] = if_turn_new
    else:
        pos[0] = i+new_pos[0]
        pos[1] = j+new_pos[1]

        data[pos[0]][pos[1]] = point

        data[i][j] = "."
    if(str(pos[0])+" "+str(pos[1]) not in dict_pos):
        dict_pos[str(pos[0])+" "+str(pos[1])] = 0




print(len(dict_pos))