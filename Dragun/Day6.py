with open("day6.txt") as f:
    x = [x.strip().split()[1:] for x in f.readlines()]

total1 = 1

for i in range(len(x[0])):
    time = int(x[0][i])
    distance = int(x[1][i])
    possible = 0

    for speed in range(1,time+1):
        if speed * (time - speed) > distance:
            possible += 1
    total1 *= possible

print(total1)

x = [int("".join(x)) for x in x]

time = x[0]
distance = x[1]

for speed in range(1,time+1):
    if speed * (time - speed) > distance:
        total2 = time - 2*speed + 1
        break

print(total2)
