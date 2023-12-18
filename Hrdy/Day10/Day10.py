PipeMap = []
StartPos = []
with open("Hrdy\Day10\Test.txt","r") as f:
    for row,line in enumerate(f):
        PipeMap.append(line.strip())
        if "S" in line:
            StartPos = [line.index("S"),row]


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
Steps = 1
Done = False
while not Done:
    Done = True
    for Index,Pos in enumerate(Positions):
        Pipe = PipeMap[Pos[1]][Pos[0]]
        
    Steps += 1

print(Steps)


        



# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
