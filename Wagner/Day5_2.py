#destination_start #source_start #range
with open("adventofcode2023/Day5/input.txt") as file:
    seeds = file.readline()[7:].strip().split()
    seeds = [[int(seeds[x]),int(seeds[x+1])] for x in range(0,len(seeds),2)]
    maps = [[x.split() for x in y if len(x) > 1 and "-" not in x] for y in [x.strip().split("\n") for x in file.read().split("map:") if x != "\n"] if len(y) > 1]
#print(maps)

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
                if (seed[0] <= source) and (top_map <= top_seed): #seed range encapsulates all of source
                    destinations.append([destination,range])
                    if (source - seed[0]) > 0:
                        destinations.append([seed[0],source-seed[0]])
                    if (top_seed - top_map) > 0:
                        destinations.append([top_map+1,top_seed - top_map])
                    #print(seeds)
                    #print(f"Map: {maps.index(map)} Line: {line} Transformation: {seed} -> {[destination,range]} Condition: 1")
                    #print(destinations,"\n")
                elif seed[0] <= source: #seed range over bottom of source range
                    destinations.append([destination,top_seed-source+1])
                    if (source - seed[0]) > 0:
                        destinations.append([seed[0],source-seed[0]])
                    #print(seeds)
                    #print(f"Map: {maps.index(map)} Line: {line} Transformation: {seed} -> {[destination,top_seed-source+1]} Condition: 2")
                    #print(destinations,"\n")
                elif top_map <= top_seed: #seed range over top of source range
                    destinations.append([destination+(seed[0]-source),top_map-seed[0]+1])
                    if (top_seed - top_map) > 0:
                        destinations.append([top_map+1,top_seed - top_map])
                    #print(seeds)
                    #print(f"Map: {maps.index(map)} Line: {line} Transformation: {seed} -> {[destination+(seed[0]-source),top_map-seed[0]+1]} Condition: 3")
                    #print(destinations,"\n")
                else: #seed range resides inside of source range
                    destinations.append([destination+(seed[0]-source),seed[1]])
                    #print(seeds)
                    #print(f"Map: {maps.index(map)} Line: {line} Transformation: {seed} -> {[destination+(seed[0]-source),seed[1]]} Condition: 4")
                    #print(destinations,"\n")
                not_in_map = False
        if not_in_map == True:
            destinations.append(seed)
            #print(seeds)
            #print(f"Map: {maps.index(map)} No Transformation {seed}")
            #print(destinations,"\n")

    seeds = [x for x in destinations]
print(min(seeds))
