with open("adventofcode2023/Day11/input.txt") as file:
    universe = []
    for line in file:
        universe.append(line.strip())

galaxies = []
y_expansion = 0
x_expansion = 0

for y in range(len(universe)): #y expansion
    if "#" not in universe[y]:
            y_expansion += 1
    for x in range(len(universe[0])):
        if universe[y][x] == "#":
            galaxies.append([y,x,y_expansion,0])

for x in range(len(universe[0])): #x expansion
    x_condition = True
    for y in range(len(universe)):
        if universe[y][x] == "#":
            x_condition = False
            for i in range(len(galaxies)): 
                if galaxies[i][0] == y and galaxies[i][1] == x:
                    galaxies[i][3] = x_expansion
        
    if x_condition == True:
        x_expansion += 1

total_distance = 0
for i in range(len(galaxies)-1):
    for j in range(i+1,len(galaxies)):
        y_difference = abs((galaxies[i][0] + galaxies[i][2]) - (galaxies[j][0] + galaxies[j][2]))
        x_difference = abs((galaxies[i][1] + galaxies[i][3]) - (galaxies[j][1] + galaxies[j][3]))
        total_distance += y_difference + x_difference
           
print(universe)
print(galaxies)
print(total_distance)
