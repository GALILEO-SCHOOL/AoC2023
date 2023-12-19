PipeMap = []
StartPos = []
with open("Hrdy\Day10\Day10.txt","r") as f:
    for row,line in enumerate(f):
        PipeMap.append([x for x in line.strip()])
        if "S" in line:
            StartPos = [line.index("S"),row]

PipeMap[StartPos[1]][StartPos[0]] = 0

Positions = []
Right = ["-","J","7"]
Left = ["-","L","F"]
Up = ["|","F","7"]
Down = ["|","L","J"]
if PipeMap[StartPos[1]][StartPos[0]+1] in Right:
    Positions.append([StartPos[1],StartPos[0]+1,"R"])
if PipeMap[StartPos[1]][StartPos[0]-1] in Left:
    Positions.append([StartPos[1],StartPos[0]-1,"L"])
if PipeMap[StartPos[1]-1][StartPos[0]] in Up:
    Positions.append([StartPos[1]-1,StartPos[0],"U"])
if PipeMap[StartPos[1]+1][StartPos[0]] in Down:
    Positions.append([StartPos[1]+1,StartPos[0],"D"])


Steps = 0
Done = False
while True:
    Steps += 1
    Done = True
    for Index,Pos in enumerate(Positions):
        if PipeMap[Pos[0]][Pos[1]] == "-":
            if Pos[2] == "R":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0],Pos[1]+1,"R"]
                Done = False
            elif Pos[2] == "L":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0],Pos[1]-1,"L"]
                Done = False
        elif PipeMap[Pos[0]][Pos[1]] == "|":
            if Pos[2] == "U":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0]-1,Pos[1],"U"]
                Done = False
            elif Pos[2] == "D":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0]+1,Pos[1],"D"]
                Done = False

        elif PipeMap[Pos[0]][Pos[1]] == "L":
            if Pos[2] == "D":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0],Pos[1]+1,"R"]
                Done = False
            elif Pos[2] == "L":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0]-1,Pos[1],"U"]
                Done = False

        elif PipeMap[Pos[0]][Pos[1]] == "J":
            if Pos[2] == "D":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0],Pos[1]-1,"L"]
                Done = False
            elif Pos[2] == "R":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0]-1,Pos[1],"U"]
                Done = False

        elif PipeMap[Pos[0]][Pos[1]] == "7":
            if Pos[2] == "R":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0]+1,Pos[1],"D"]
                Done = False
            elif Pos[2] == "U":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0],Pos[1]-1,"L"]
                Done = False   
        elif PipeMap[Pos[0]][Pos[1]] == "F":
            if Pos[2] == "U":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0],Pos[1]+1,"R"]
                Done = False
            elif Pos[2] == "L":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0]+1,Pos[1],"D"]
                Done = False   
        elif PipeMap[Pos[0]][Pos[1]] == "J":
            if Pos[2] == "D":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0],Pos[1]-1,"L"]
                Done = False
            elif Pos[2] == "R":
                PipeMap[Pos[0]][Pos[1]] = Steps
                Positions[Index] = [Pos[0]-1,Pos[1],"U"]
                Done = False   
    if Done: break     


for l in PipeMap:
    print(l)


print(Steps -1)



# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Contained = 0
for y,row in reversed(list(enumerate(PipeMap))):
    XInside = False
    for x,col in reversed(list(enumerate(row))):
        if isinstance(col,int):
            if not XInside:
                XInside = True
            else:
                XInside = False
        elif XInside:
            PipeMap[y][x] = "X"


for x in range(len(PipeMap[0])-1,-1,-1):
    YInside = False
    for y in range(len(PipeMap)-1,-1,-1):
        if isinstance(PipeMap[y][x],int):
            if YInside: YInside = False
            else: YInside = True
        elif YInside:
            if PipeMap[y][x] == "X":
                PipeMap[y][x] = "XY"
                Contained += 1
            else: PipeMap[y][x] = "Y"




print(Contained)   


with open("Hrdy\Day10\Solution.txt","w") as f:
    for l in PipeMap:
        line = ""
        for c in l:
            if isinstance(c,int):
                line += "0"
            else:
                line += c
        f.writelines(line + "\n")

#509 is too low