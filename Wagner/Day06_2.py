with open("adventofcode2023\Day6\input.txt") as file:
    time = int("".join(file.readline()[10:].strip().split()))
    distance = int("".join(file.readline()[10:].strip().split()))

down_time = 1
while True:
    if down_time*(time - down_time) > distance:
        print(time - ((down_time)*2) +1)
        break
    down_time += 1
