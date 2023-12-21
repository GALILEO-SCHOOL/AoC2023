with open("Hrdy\Day11\Day11.txt","r") as f:
    Universe = []
    Galaxies = []
    AmountOfGalaxies = 1
    y = 0
    for line in f:
        Row = []
        Gala = False
        x = 0
        for c in line.strip():
            if c == "#":
                Gala = True
                Row.append([AmountOfGalaxies,y,x])
                Galaxies.append([AmountOfGalaxies,y,x])
                AmountOfGalaxies +=1
            else: Row.append(c)
            x += 1
        Universe.append(Row)
        if not Gala: y+=2
        else: y+=1

Horizont = [x[2] for x in Galaxies]
Expansion = 0
for x in range(max(Horizont)):
    if x not in Horizont:
        for index,Gala in enumerate(Galaxies):
            if Gala[2] > x+Expansion:
                Galaxies[index][2] += 1
        Expansion += 1

# for line in Universe:
#     print(line)
# print(Galaxies)

Distance = 0
for i in range(len(Galaxies)-1):
    for j in range(i+1,len(Galaxies)):
        Distance += (abs(Galaxies[i][1] - Galaxies[j][1]) + abs(Galaxies[i][2] - Galaxies[j][2]))
print(Distance)
