with open("adventofcode2023/Day4/input.txt") as file:
    winning_numbers = []
    cards = []
    for line in file:
        temp = line[10:].strip().split("|")
        winning_numbers.append(temp[0].split())
        cards.append([temp[1].split(),1])

#Task1
result = 0
result2 = 0
for count,card in enumerate(cards):
    point_count = 0
    for number in card[0]:
        if number in winning_numbers[count]:
            point_count += 1
    if point_count > 0:  result += 2**(point_count - 1)
    #Task2
    for duplicates in range(1,point_count+1):
        cards[count+duplicates][1] += card[1]
    result2 += card[1]

print(f"Task1: {result}")
print(f"Task2: {result2}")
