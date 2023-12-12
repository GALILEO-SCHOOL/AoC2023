with open("day8.txt") as f:
    x = [x.strip() for x in f.readlines()]

instructions = x[0]

positions = []
map = {}
for letter in x[2:]:
    i = letter.split(" = ")[0]
    j = letter.split("=")[1].split(", ")[0].replace(" (", "")
    k = letter.split("=")[1].split(", ")[1].replace(")", "")
    map[i] = (j, k)

    if i[-1] == "A":
        positions.append([i])

def part1(current):
    counter = 0
    while True:
        for step in instructions:
            counter += 1
            if step == "R":
                current = map[current][1]
            elif step == "L":
                current = map[current][0]
            if current == "ZZZ":
                return counter

def part2(current):
    counter = 0
    while True:
        for step in instructions:
            counter += 1
            if step == "R":
                current = map[current][1]
            elif step == "L":
                current = map[current][0]
            if current[-1] == "Z":
                return counter

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

total1 = part1("AAA")

print(total1)

for i, position in enumerate(positions):
    positions[i] = part2(position[0])

total2 = positions[0]

for i in range(len(positions[0:])):
    total2 = lcm(total2, positions[i])

print(total2)    

