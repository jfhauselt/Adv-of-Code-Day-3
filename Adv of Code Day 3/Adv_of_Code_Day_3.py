#I know this isnt the right way but ok



def slopeCount(down, right):
    path = r"C:\Users\jfhau\Documents\#code\Day3.txt"
    f = open(path,"r")
    count = down
    x = 0
    maxX = 0
    Trees = 0

    for line in f:
        if maxX == 0:
            maxX = len(line) -2 
        if count == down:
            if line[x] == "#":
                Trees +=1
            x += right
            count = 1
            if x > maxX:
                x -= maxX +1
        else:
            count +=1
    return Trees


print(slopeCount(1,1))
print(slopeCount(1,3))
print(slopeCount(1,5))
print(slopeCount(1,7))
print(slopeCount(2,1))
print(slopeCount(1,1)*slopeCount(1,3)*slopeCount(1,5)*slopeCount(1,7)*slopeCount(2,1))
