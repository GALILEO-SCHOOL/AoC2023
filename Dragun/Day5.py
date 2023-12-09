with open("day5.txt") as f:
    x = [x.split("\n") for x in f.read().split("map:")]

almanac = []
for i in x:
    i = [k.split() for k in [j for j in i if j != ''][:-1]]
    almanac.append(i)
almanac[-1].append(x[-1][-1].split())

seeds = [int(x) for x in almanac[0][0][1:]]
s = seeds.copy()
almanac.pop(0)

for map in almanac:
    for i, seed in enumerate(seeds):
        for ran in map:
            destination, source, distance = [int(x) for x in ran]
            if seed in range(source, source+distance):
                seeds[i] = destination + seed - source
                break

total1 = min(seeds)

print(total1)

seeds = []
while len(s) > 0:
    seeds.append(s[:2])
    s = s[2:]


found = False
num = 0
counter = 1485889

while not found:
    num = counter

    for map in almanac[::-1]: 
        for ran in map:
            destination, source, distance = [int(x) for x in ran]
            if num in range(destination, destination+distance):
                num = source + num - destination
                break

    for r in seeds:
        if num >= r[0] and num <= r[0] + r[1] - 1:
            found = True
            break
            
    counter += 1

total2 = counter-1

print(total2)
