import math
#read file
file=open('2.txt')
data= [r.split() for r in [r for r in file.read().split("\n")]]
data = [list(map(int, i)) for i in data]

safe_counter = 0

for report in data:
    if(len(report) == 1 or len(report) == 0):
        safe_counter+=1
        continue
    if(report[len(report)-1] == report[0]):
        direction = -1
    else:
        direction = int((report[len(report)-1]-report[0])/abs((report[len(report)-1]-report[0]))) 

    unsafe_level= 0
    unsafe_level_start = -1;
    special_case = False

    unsafe_level_flipped = 0
    unsafe_level_start_flipped = -1
    for i in range(1,len(report)):
        difference = report[i]-report[i-1];
        if(abs(difference) < 1 or abs(difference) > 3 or int(difference/abs(difference)!= direction)):
            if(unsafe_level_start ==(i-2) and unsafe_level == 1):
                special_case = True

            unsafe_level +=1;
            unsafe_level_start = i-1
        elif(i == len(report)-1 and unsafe_level == 0):
            safe_counter +=1


        if(abs(difference) < 1 or abs(difference) > 3 or int(difference/abs(difference) == direction)):
            unsafe_level_flipped +=1
            unsafe_level_start_flipped = i-1
            
    
    if(unsafe_level == 1):
        #3 cases, beg , reg, end node
        if(unsafe_level_start == 0 or unsafe_level_start == len(report)-2):
            safe_counter +=1;

        else:# must be reg-> two cases remove start or start+1
            #check unsafe_level_start-+1

            #remove start+1
            difference = report[unsafe_level_start+2]-report[unsafe_level_start];
            if (not(abs(difference) < 1 or abs(difference) > 3 or int(difference/abs(difference)!= direction))):
                safe_counter +=1;
                continue;
            
            #remove start
            difference = report[unsafe_level_start+1]-report[unsafe_level_start-1];
            if (not(abs(difference) < 1 or abs(difference) > 3 or int(difference/abs(difference)!= direction))):
                safe_counter +=1;
                continue;

    elif((unsafe_level==2 and special_case == True)):
        difference = report[unsafe_level_start+1]-report[unsafe_level_start-1];
        if (not(abs(difference) < 1 or abs(difference) > 3 or int(difference/abs(difference)!= direction))):
            safe_counter +=1;
            continue;

    elif(unsafe_level_flipped == 1):
        safe_counter +=1

print(safe_counter)