file=open('3.txt')
data = str(file.read())

doStarts = [i for i in range(len(data)) if data.startswith("do()", i)] 
dontStarts = [i for i in range(len(data)) if data.startswith("don't()", i)] 


mappedStartsDo = [{x : 'do'} for x in doStarts]

mappedStartsDont = [{x : 'dont'} for x in dontStarts]



newString = ""

j = 0
starting = True

while (j < len(data)):
    if(starting == True and (j not in dontStarts)):
        newString = newString+ data[j:j+1]
    elif(starting == False and (j in doStarts)):
        newString = newString+ data[j:j+1]

        starting = True
    elif(j in dontStarts):
        starting = False


    j+=1



data = list(newString)





#convert to list

goal = ["m","u","l","(","x",",","x",")"]

spot = 0

numbers = []

numbersList = []
i = 0

while(i < len(data)):
    char = data[i]
    #if last spot
    if(spot == 8):
        spot = 0
        i = i-1
        numbers.append([numbersList[len(numbersList)-1],numbersList[len(numbersList)-2]])
    elif(spot == 4 or spot == 6):
        #number detection
        testNumber = []
        j = i
        while j< len(data) and data[j].isdigit() == True:
            testNumber.append(data[j])
            j+=1

        numberTemp = ''.join(testNumber)
        numbersList.append(numberTemp)
        
        i = j-1
        spot +=1
    elif(char==goal[spot]):
        spot+=1
    else:
        spot = 0

    i+=1

numbers = [list( map(int,i) ) for i in numbers]
finalNumber = 0
for i in range(len(numbers)):
    finalNumber += numbers[i][0]*numbers[i][1]

print(finalNumber)
