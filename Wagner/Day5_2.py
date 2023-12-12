def line_check():
    if (seed[0] <= source) and (top_map <= top_seed): #seed range encapsulates all of source
        return [destination,range]
    elif seed[0] <= source: #seed range over bottom of source range
        return [destination,top_seed-source+1]
    elif top_map <= top_seed: #seed range over top of source range
        return [destination+(seed[0]-source),top_map-seed[0]+1]
    else: #seed range resides inside of source range
        return [destination+(seed[0]-source),seed[1]]
            
with open("adventofcode2023/Day5/hrdy.txt") as file:
    seeds = file.readline()[7:].strip().split()
    seeds = [[int(seeds[x]),int(seeds[x+1])] for x in range(0,len(seeds),2)]
    maps = [[x.split() for x in y if len(x) > 1 and "-" not in x] for y in [x.strip().split("\n") for x in file.read().split("map:") if x != "\n"] if len(y) > 1]

for map in maps:
    destinations = []
    for seed in seeds:
        not_in_map = True
        top_seed = seed[0] + seed[1] - 1
        for line in map:
            destination = int(line[0])
            source = int(line[1])
            range = int(line[2])
            top_map = source + range - 1
            if (not(top_seed < source)) and (not(top_map < seed[0])):
                destinations.append(line_check())
                not_in_map = False
        if not_in_map == True:
            destinations.append(seed)
    seeds = [x for x in destinations]

print(min(seeds))
