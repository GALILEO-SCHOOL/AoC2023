with open("Hrdy\Day11\Test.txt","r") as f:
    Universe = [x.strip() for x in f.readlines()]
Galaxies = []
xExpac = 0
yExpac = 0
for y in range(len(Universe)):
    for x in range(len(Universe[0])):
        if Universe[y][x] == "#":
            row = Universe[y]
            col = [i[x] for i in Universe]
            if "#" not in row:
                xExpac +=1
            if "#" not in col: yExpac += 1
            Galaxies.append([x+xExpac,y+yExpac])
print(Galaxies)
