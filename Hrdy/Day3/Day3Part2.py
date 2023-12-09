from copy import deepcopy
Schematic = []
Values = "*"
Numbers = "0123456789"
GearsRatio = 0

with open("Hrdy\Day3\Day3.txt","r") as f:
    for line in f:
        if len(Schematic) == 0:
            Schematic.append("."*(2+len(line.strip())))
        Schematic.append(["."]+[x for x in line.strip()]+["."])
    Schematic.append("."*(2+len(line.strip())))

CopySchematic = deepcopy(Schematic)
for y,row in enumerate(Schematic):
    for x,col in enumerate(row):
        if col in Values:
            Gears = []
            for i in range(y-1,y+2):
                for j in range(x-1,x+2):
                    test = CopySchematic[i][j]
                    if CopySchematic[i][j] in Numbers:
                        Num = CopySchematic[i][j]
                        CopySchematic[i][j] = "."
                        grad = 1
                        while CopySchematic[i][j-grad] in Numbers:
                            Num = CopySchematic[i][j-grad] + Num
                            CopySchematic[i][j-grad] = "."
                            grad += 1
                        grad = 1
                        while CopySchematic[i][j+grad] in Numbers:
                            Num += CopySchematic[i][j+grad]
                            CopySchematic[i][j+grad] = "."
                            grad += 1
                        Gears.append(Num)
            if len(Gears) == 2:
                GearsRatio += int(Gears[0]) * int(Gears[1])

print(GearsRatio)


