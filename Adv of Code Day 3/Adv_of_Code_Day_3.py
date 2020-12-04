#I know this isnt the right way but ok
path = r"C:\Users\jfhau\Documents\#code\Day3.txt"
f = open(path,"r")
x = 0
maxX = 0

Trees = 0

def slopeCount(down, right):
    pass
for line in f:
    
    if maxX == 0:
        maxX = len(line) -2 

    if line[x] == "#":
        Trees +=1
    x +=3
    if x > maxX:
        x -= maxX +1



print(Trees)
