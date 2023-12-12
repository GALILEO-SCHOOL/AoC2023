with open("day5.txt") as f:
    almanac = [[k.split() for k in [j for j in i if j != '' and j[-1].isdigit()]] for i in [x.split("\n") for x in f.read().split("map:")]]

seeds = [int(x) for x in almanac[0][0][1:]]
seed_ranges = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]

for map in almanac[1:]:
    for i, seed in enumerate(seeds):
        for ran in map:
            destination, source, distance = [int(x) for x in ran]
            if seed in range(source, source + distance):
                seeds[i] = destination + seed - source
                break

total1 = min(seeds)

print(total1)

for map in almanac[1:]:
    new_ranges = []
    for i, seed_range in enumerate(seed_ranges):
        found = False
        for range in map:
            destination, start, length = [int(i) for i in range]
            seed_start, seed_length = seed_range
            difference = destination - start
            end = start + length -1
            seed_end = seed_start + seed_length -1
            
            if seed_start + seed_length -1 >= start and seed_start <= start + length - 1: 
                found = True
                if seed_start >= start and seed_end <= end:
                    new_ranges.append([seed_start + difference, seed_length])

                elif seed_start <= start and seed_end <= end:
                    new_ranges.append([destination, seed_length - (start - seed_start)])

                elif seed_start >= start and seed_end >= end:
                    new_ranges.append([seed_start + difference, end - seed_start + 1])
    
                elif seed_start <= start and seed_end >= end:
                    new_ranges.append([destination, length])
        
        if not found:
            new_ranges.append(seed_range)
    seed_ranges = new_ranges

total2 = min([x[0] for x in seed_ranges if x[0] != 0])

print(total2)
