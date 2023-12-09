Races = []
MarginOfError = []

with open("Hrdy\Day6\Day6.txt","r") as f:
    for line in f:
        Races.append([x for x in line.strip().split(" ")[1:] if x != ""])
#print(Races)

Time  = ""
Distance = ""
for t in Races[0]:
    Time+=t
for d in Races[1]:
    Distance+=d


for j in range(int(Time)):
    if j * (int(Time)-j) > int(Distance):
        WinsBot = j
        break

for j in range(int(Time),0,-1):
    if j * (int(Time)-j) > int(Distance):
        WinsTop = j
        break
    

print(WinsTop-WinsBot+1)