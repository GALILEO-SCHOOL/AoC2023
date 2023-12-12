with open("day7.txt") as f:
    hands = [[[y for y in x.strip().split()[0]], int(x.strip().split()[1])] for x in f.readlines()]

conversion_table = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
map = {}
ranking = [[] for i in range(7)]

for hand in hands:
    cards = {}

    for i, card in enumerate(hand[0]):
        if card in conversion_table:
            hand[0][i] = conversion_table[card]
        else: hand[0][i] = int(card)
        
        if card not in cards:
            cards[card] = 1
        else: cards[card] += 1
    
    map[str(hand[0])] = hand[1] 

    if max(cards.values()) == 5:
        ranking[6].append(hand)
    elif max(cards.values()) == 4:
        ranking[5].append(hand)
    elif max(cards.values()) == 3 and 2 in cards.values():
        ranking[4].append(hand)
    elif max(cards.values()) == 3:
        ranking[3].append(hand)
    elif max(cards.values()) == 2 and len(cards.values()) == 3:
        ranking[2].append(hand)
    elif max(cards.values()) == 2:
        ranking[1].append(hand)
    else: ranking[0].append(hand)

ranking = [[y[0] for y in x] for x in ranking if x != []]
counter = 0
total = 0

for rank in ranking:
    rank.sort()
    for hand in rank:
        counter += 1
        total += map[str(hand)] * counter

print(total)
    
    