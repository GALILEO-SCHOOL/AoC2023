with open("adventofcode2023\Day6\input.txt") as file:
    time = file.readline()[10:].strip().split()
    distance = file.readline()[10:].strip().split()
    table = []
    for i in range(len(time)):
        table.append([int(time[i]),int(distance[i])])

result = 1
for cell in table:
    down_time = 1
    while True:
        if down_time*(cell[0] - down_time) > cell[1]:
            result *= (cell[0] - ((down_time)*2) +1)
            break
        down_time += 1

print(result)
