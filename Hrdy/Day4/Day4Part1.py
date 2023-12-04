CardList = []
Points = 0
with open("Hrdy\Day4\Day4.txt","r") as f:
    for line in f:
        CardList.append([[int(x) for x in line.split(": ")[1].split(" | ")[0].split(" ") if x !=""], [int(x) for x in line.split(": ")[1].split(" | ")[1].strip().split(" ") if x !=""]])
for Card in CardList:
    Value = 0
    for num in Card[1]:
        if num in Card[0]:
            if Value == 0:
                Value = 1
            else: Value *=2
    Points += Value
print(Points)