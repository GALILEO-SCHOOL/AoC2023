with open("day7.txt") as f:
    hands = [[x.strip().split()[0], int(x.strip().split()[1])] for x in f.readlines()]

card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

ranking = [[] for i in range(7)]

for i, hand in enumerate(hands):
    temp = []

    for card in hand[0]:
        if card in card_values:
            temp.append(card_values[card])
        else:
            temp.append(int(card))
    hands[i][0] = temp

    cards = {}

    for card in hand[0]:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

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
    elif 2 in cards.values():
        ranking[1].append(hand)
    else: ranking[0].append(hand)

ranking = [x for x in ranking if x != []]

total1 = 0

counter = 1
for rank in ranking:
    rank.sort()
    for hand in rank:
        total1 += hand[1]*counter
        counter += 1

print(total1)

ranking = [[] for i in range(7)]

for hand in hands:
    
    cards = {}
    for i, card in enumerate(hand[0]):
        if card == 11:
            card = 1
            hand[0][i] = 1
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    
    if 1 in cards:
        if max(cards.values()) == 5 or len(cards.values()) == 2:
            ranking[6].append(hand)
        elif max([cards[x] for x in cards.keys() if x != 1]) + cards[1] == 4 or cards[1] == 3:
            ranking[5].append(hand)
        elif max(cards.values()) == 2 and len(cards.values()) == 3:
            ranking[4].append(hand)
        elif max(cards.values()) + cards[1] == 3 or cards[1] == 2:
            ranking[3].append(hand)
        else: ranking[1].append(hand)
    
    else:
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
        elif 2 in cards.values():
            ranking[1].append(hand)
        else: ranking[0].append(hand)

ranking = [x for x in ranking if x != []]

total2 = 0
counter = 1
for rank in ranking:
    rank.sort()
    for hand in rank:
        total2 += hand[1]*counter
        counter += 1

print(total2)
