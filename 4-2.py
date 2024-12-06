file=open('4.txt')
import re 
data_hor= [list(r) for r in [r for r in file.read().split("\n")]]

count = 0


for i in range (1, len(data_hor)-1):
    for j in range(1,len(data_hor[0])-1):
        if(data_hor[i][j] == "A"):
            if(data_hor[i-1][j-1] == "M" and data_hor[i+1][j+1] == "S" and data_hor[i+1][j-1] == "M" and data_hor[i-1][j+1]=="S"):
                count +=1
            elif(data_hor[i-1][j-1] == "S" and data_hor[i+1][j+1] == "M" and data_hor[i+1][j-1] == "S" and data_hor[i-1][j+1]=="M"):
                count +=1
            elif(data_hor[i-1][j-1] == "M" and data_hor[i+1][j+1] == "S" and data_hor[i+1][j-1] == "S" and data_hor[i-1][j+1]=="M"):
                count +=1
            elif(data_hor[i-1][j-1] == "S" and data_hor[i+1][j+1] == "M" and data_hor[i+1][j-1] == "M" and data_hor[i-1][j+1]=="S"):
                count +=1
print(count)