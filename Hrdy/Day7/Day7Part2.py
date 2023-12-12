Hands = []
HighCard = []
Pair = []
TwoPair = []
Three = []
FullHours = []
Quad = []
Five = []
Values = {"T":10,"J":1,"Q":12,"K":13,"A":14}

with open("Hrdy\Day7\Day7.txt","r") as f:
    for line in f:
        Hands.append([[x for x in line.strip().split()[0]], int(line.strip().split()[1])])

for i,hand in enumerate(Hands):
    for j,c in enumerate(hand[0]):
        if c in Values:
            Hands[i][0][j] = Values[c]
        else:
            Hands[i][0][j] = int(Hands[i][0][j])

for index,hand in enumerate(Hands):
    Cards = {}
    Jokers = 0
    for card in hand[0]:
        if card == 1:
            Jokers += 1
        elif card not in Cards:
            Cards[card] = 1
        else:
            Cards[card] += 1     
    Cards = dict(sorted(Cards.items(),key = lambda item : item[1],reverse=True))
    if len(Cards) == 0: Five.append(hand)
    elif max(Cards.values()) + Jokers == 5:
        Five.append(hand)
    elif max(Cards.values()) + Jokers == 4:
        Quad.append(hand)
    elif max(Cards.values()) + Jokers == 3:
        if min(Cards.values()) == 2:
            FullHours.append(hand)
        else:
            Three.append(hand)
    elif max(Cards.values()) + Jokers == 2: 
        if len(Cards) == 3: 
            TwoPair.append(hand)
        else: Pair.append(hand)
    else: HighCard.append(hand)

HighCard.sort()
Pair.sort()
TwoPair.sort()
Three.sort()  
FullHours.sort()
Quad.sort()
Five.sort()  

Hands = [HighCard,Pair,TwoPair,Three,FullHours,Quad,Five]

Winnings = 0
rank = 1
for Type in Hands:
    for hand in Type:
        Winnings += hand[1]*rank
        rank += 1

print(Hands[6])
print(Winnings)


#254837398