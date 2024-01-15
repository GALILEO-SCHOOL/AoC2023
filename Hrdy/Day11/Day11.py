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
                Row.append([AmountOfGalaxies,y,x,0,0])
                Galaxies.append([AmountOfGalaxies,y,x,0,0])
                AmountOfGalaxies +=1
            else: Row.append(c)
            x+=1
        y+=1
        Universe.append(Row)


ExpansionRate = 999999

Horizont = [x[2] for x in Galaxies]
VerticalLimit = [x[1] for x in Galaxies]

Expansion = 0
for x in range(max(Horizont)):
    if x not in Horizont:
        for index,Gala in enumerate(Galaxies):
            if Gala[2] > x:
                Galaxies[index][4] += ExpansionRate
        Expansion += 1

Expansion = 0
for y in range(max(VerticalLimit)):
    if y not in VerticalLimit:
        for index,Gala in enumerate(Galaxies):
            if Gala[1] > y:
                Galaxies[index][3] += ExpansionRate
        Expansion += 1

# for line in Universe:
#      print(line)


Distance = 0
for i,Gal in enumerate(Galaxies):
    Galaxies[i][1] += Galaxies[i][3]
    Galaxies[i][2] += Galaxies[i][4]
#print(Galaxies)
for i in range(len(Galaxies)-1):
    for j in range(i+1,len(Galaxies)):
        Distance += abs((Galaxies[i][1]) - (Galaxies[j][1])) + abs((Galaxies[i][2]) - (Galaxies[j][2]))
print(Distance)
