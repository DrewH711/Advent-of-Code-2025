curpos = 50
count = 0

#using R+, L-
with open("day1\input1.txt", "r") as input:
    for line in input:
        instruction = line
        #print(f"raw_instruction: {instruction}")
        instruction = instruction.replace("L", "-")
        instruction = instruction.replace("R", "")
        #print(f"instruction: {instruction}")
        move = int(instruction)
        curpos = (curpos+move) % 100
        #print(curpos)
        if(curpos==0):
            count+=1


print(count)
