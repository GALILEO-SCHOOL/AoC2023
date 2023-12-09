Schematic = []
SumOfPartNumbers = 0
numbers = "0123456789."

with open("Hrdy\Day3\Test.txt","r") as f:
    for line in f:
        Schematic.append(line.strip())
print(Schematic)

for y,row in enumerate(Schematic):
    for x,col in enumerate(row):
        if col not in numbers:
            
