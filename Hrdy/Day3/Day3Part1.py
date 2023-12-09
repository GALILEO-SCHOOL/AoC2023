from copy import deepcopy
Schematic = []
Values = "0123456789."
Numbers = "0123456789"
SumOfPartNumbers = 0

with open("Hrdy\Day3\Day3.txt","r") as f:
    for line in f:
        if len(Schematic) == 0:
            Schematic.append("."*(2+len(line.strip())))
        Schematic.append(["."]+[x for x in line.strip()]+["."])
    Schematic.append("."*(2+len(line.strip())))

CopySchematic = deepcopy(Schematic)
print(Schematic)
for y,row in enumerate(Schematic):
    for x,col in enumerate(row):
        if col not in Values:
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
                        SumOfPartNumbers += int(Num)
print(SumOfPartNumbers)


