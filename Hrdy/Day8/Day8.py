Map = {}
Position = ("AAA")
Goal = ("ZZZ")
Steps = 0
with open("Hrdy\Day8\Day8.txt","r") as f:
    Instruction = [x for x in f.readline().strip()]
    f.readline()
    for line in f:
        Map[line.split(" = ")[0]] = [x for x in line.strip().split(" = ")[1].replace("(","").replace(")","").split(", ")]

while Position != Goal:
    for command in Instruction:
        if command == "R":
            Position = Map[Position][1]
        elif command == "L":
            Position = Map[Position][0]
        Steps += 1

#print(Instruction,Map)
print(Steps)

                