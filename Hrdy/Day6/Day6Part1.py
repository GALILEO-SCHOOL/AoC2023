Races = []
MarginOfError = []

with open("Hrdy\Day6\Day6.txt","r") as f:
    for line in f:
        Races.append([int(x) for x in line.strip().split(" ")[1:] if x != ""])
#print(Races)

for i in range(len(Races[0])):
    Wins = 0
    for j in range(Races[0][i]):
        if j * (Races[0][i]-j) > Races[1][i]:
            Wins += 1
    MarginOfError.append(Wins)

print(MarginOfError)
Solution = 1
for num in MarginOfError:
    Solution *= num
print(Solution)
