from math import lcm
Map = {}
Steps = 0


with open("Hrdy\Day8\Day8.txt","r") as f:
    Instruction = [x for x in f.readline().strip()]
    f.readline()
    for line in f:
        Map[line.split(" = ")[0]] = [x for x in line.strip().split(" = ")[1].replace("(","").replace(")","").split(", ")]

StartingPositions = [x for x in Map.keys() if x[2] == "A"]
Exits = [[] for x in StartingPositions]
print(Exits)
Done = False
while not Done:
    Done = True
    for command in Instruction:
        for index,Position in enumerate(StartingPositions):
            if command == "R":
                StartingPositions[index] = Map[Position][1]
            elif command == "L":
                StartingPositions[index] = Map[Position][0]
        Steps += 1
    for index,Position in enumerate(StartingPositions):
        if Position[2] == "Z":
            if len(Exits[index]) == 0: Exits[index].append(Steps)
    for Exit in Exits:
        if Exit == []:
            Done = False

Solution = 1
for Exit in Exits:
    Solution = lcm(Solution,Exit[0])

print(Solution)
#BRUTE FORCE IS NOT THE WAY!