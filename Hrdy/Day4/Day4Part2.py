CardList = []
ValueList = []
with open("Hrdy\Day4\Day4.txt","r") as f:
    for line in f:
        CardList.append([[int(x) for x in line.split(": ")[1].split(" | ")[0].split(" ") if x !=""], [int(x) for x in line.split(": ")[1].split(" | ")[1].strip().split(" ") if x !=""]])
        ValueList.append(1)
for index,Card in enumerate(CardList):
    Value = 0
    for num in Card[1]:
        if num in Card[0]:
            Value +=1
    for i in range(Value):
        ValueList[index+i+1] += ValueList[index]
print(sum(ValueList))