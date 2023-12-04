with open("day4.txt") as f:
    cards = [x.strip().split(":")[1].split("|") for x in f.readlines()]

total1 = 0
instances = [1 for i in cards]

for i, card in enumerate(cards):
    winning = [int(x) for x in card[0].split()]
    our_nums = [int(x) for x in card[1].split()]
    value = 0
    matching_nums = 0 

    for num in winning:
        if num in our_nums:
            matching_nums += 1
            if value == 0:
                value = 1
            else:
                value *= 2
    total1 += value

    for j in range(i, i+matching_nums):
        instances[j] += 1*instances[i-1]

print(total1)

total2 = sum(instances)

print(total2)
