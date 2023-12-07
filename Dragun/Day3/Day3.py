with open("Dragun\Day3\Day3.txt") as f:
    schematic = [x.strip() for x in f.readlines()]

total1 = 0

def find_adjacents(x_range, y, bounds):
    possible = []
    bounds -= 1
    for x in range(x_range[0], x_range[1] + 1):
        for i in range(-1, 2):
            if x + i >= 0 and x + i <= bounds:
                for j in range(-1,2):
                    if y + j >= 0 and y + j <= bounds and [x+i,y+j] != [x, y] and [x+i,y+j] not in possible:
                        possible.append([x+i,y+j])
    return(possible)

bound = len(schematic) 

x_ranges = [[] for i in range(bound)]

for y in range(bound):
    for x in range(bound):
        if schematic[y][x].isdigit():    
            x_ranges[y].append(x)

full_cords = []
for j, ran in enumerate(x_ranges):
    pointer = 0
    if len(ran) > 0:
        for i in range(len(ran)):
            if i < len(ran)-1:
                if ran[i+1] - ran[i] > 1:
                    full_cords.append([ran[pointer:i+1][0], ran[pointer:i+1][-1], j])
                    pointer = i+1
        full_cords.append([ran[pointer:i+1][0], ran[pointer:i+1][-1], j])

for i in full_cords:
    for cord in find_adjacents([i[0], i[1]], i[2], bound):
        if schematic[cord[1]][cord[0]] != "." and schematic[cord[1]][cord[0]].isdigit() == False:
            total1 += int(schematic[i[2]][i[0] : i[1]+1])
            break

print(total1)

gears = [[x, y, []] for x in range(bound) for y in range(bound) if schematic[y][x] == "*"]

for i in full_cords:
    for cord in find_adjacents([i[0], i[1]], i[2], bound):
        if cord in [x[:2] for x in gears]:
            gears[[x[:2] for x in gears].index(cord)][2].append(int(schematic[i[2]][i[0] : i[1]+1]))

total2 = 0
for gear in gears:
    if len(gear[2]) == 2:
        total2 += gear[2][0] * gear[2][1]

print(total2)
