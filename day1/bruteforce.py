curval = 50
count = 0

with open("day1/input1.txt", "r") as file:
    for line in file:
        instruction = line.replace("L","-").replace("R","")
        move = int(instruction)

        for i in range(abs(move)):
            if(move>0):
                curval = (curval+1)%100
                if(curval==0):
                    count+=1
            elif(move<0):
                curval = (curval-1)%100
                if(curval==0):
                    count+=1
print(count)