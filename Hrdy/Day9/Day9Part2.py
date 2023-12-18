Oasis = []
with open("Hrdy\Day9\Day9.txt","r") as f:
    for line in f:
        Oasis.append([int(x) for x in line.strip().split(" ")])

SumOfExtrapolated = 0

for Sequence in Oasis:
    Prediction = [Sequence]
    while sum(Prediction[-1]) != 0:
        NewSequence = []
        for i in range(1,len(Prediction[-1])):
            NewSequence.append(Prediction[-1][i] - Prediction[-1][i-1])
        Prediction.append(NewSequence)
    Sum = 0
    for index,Pred in reversed(list(enumerate(Prediction))):
        Prediction[index].insert(0,Sum)
        Sum = Prediction[index-1][0] - Sum
    SumOfExtrapolated += Prediction[0][0]
      
print(SumOfExtrapolated)