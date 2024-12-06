file=open('4.txt')
import re 

#horizontal
data_hor= [list(r) for r in [r for r in file.read().split("\n")]]
data_hor_reversed = []
for data in data_hor:
    data_hor_reversed.append(data[::-1])

#vertical
data_ver = []
for j in range(len(data_hor[0])):

    for i in range(len(data_hor)):
        if(i == 0):
            data_ver.append(list(data_hor[i][j]))
        else:
            data_ver[j].append(data_hor[i][j])

data_ver_reversed = []
for data in data_ver:
    data_ver_reversed.append(data[::-1])

#diagonal
data_diag_1 = [[] for _ in range(2 * len(data_hor) - 1)]
data_diag_2 = [[] for _ in range(2 * len(data_hor) - 1)]

for i in range(len(data_hor)):
    for j in range(len(data_hor[i])):
        data_diag_1[i + j].append(data_hor[i][j])

for i in range(len(data_hor)):
    for j in range(len(data_hor[i])):
        data_diag_2[i - j + (len(data_hor) - 1)].append(data_hor[i][j])

data_diag_1_reversed = []
for data in data_diag_1:
    data_diag_1_reversed.append(data[::-1])

data_diag_2_reversed = []
for data in data_diag_2:
    data_diag_2_reversed.append(data[::-1])


amount = 0
complete = data_ver+ data_hor_reversed + data_ver_reversed+data_hor+data_diag_2_reversed+data_diag_2+data_diag_1+data_diag_1_reversed

for string in complete:
    stringS = ''.join(string)

    res = [i.start() for i in re.finditer("XMAS", stringS)] 
    amount += len(res)

print(amount)
