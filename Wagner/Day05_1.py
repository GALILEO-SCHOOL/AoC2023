with open("adventofcode2023/Day5/input.txt") as file:
    seeds = file.readline()[7:].strip().split()
    maps = [[x.split() for x in y if len(x) > 1 and "-" not in x] for y in [x.strip().split("\n") for x in file.read().split("map:") if x != "\n"] if len(y) > 1]
print(maps)

for map in maps:
    destinations = []
    for seed in seeds:
        not_in_map = True
        for line in map:
            if int(seed) >= int(line[1]) and int(seed) <= (int(line[1]) + int(line[2]) -1):
                destinations.append(int(line[0]) + (int(seed) - int(line[1])))
                not_in_map = False
        if not_in_map == True:
            destinations.append(seed)
    seeds = [x for x in destinations]
    
print(min(seeds))
