Seeds = []
Map = []
SeedToSoil = []
SoilToFertilizer = []
FertiliserToWater = []
WaterToLight = []
LightToTemperature = []
TemperatureToHumidity = []
HumidityToLocation = []
Manual = []

with open("Hrdy\Day5\Day5.txt","r") as f:
    Seeds = [int(x) for x in f.readline().split(": ")[1].strip().split(" ")]
    for line in f:
        if line.strip() == "":
            if len(Map) > 0 :
                Manual.append(Map)
                Map = []
        else: Map.append(line.strip())
    Manual.append(Map)
FinalManual = []
for i in range(1,len(Manual[0])):
    SeedToSoil.append([int(x) for x in Manual[0][i].split(" ")])
for i in range(1,len(Manual[1])):
    SoilToFertilizer.append([int(x) for x in Manual[1][i].split(" ")])
for i in range(1,len(Manual[2])):
    FertiliserToWater.append([int(x) for x in Manual[2][i].split(" ")])
for i in range(1,len(Manual[3])):
    WaterToLight.append([int(x) for x in Manual[3][i].split(" ")])
for i in range(1,len(Manual[4])):
    LightToTemperature.append([int(x) for x in Manual[4][i].split(" ")])
for i in range(1,len(Manual[5])):
    TemperatureToHumidity.append([int(x) for x in Manual[5][i].split(" ")])
for i in range(1,len(Manual[6])):
    HumidityToLocation.append([int(x) for x in Manual[6][i].split(" ")])
Manual = [SeedToSoil,SoilToFertilizer,FertiliserToWater,WaterToLight,LightToTemperature,TemperatureToHumidity,HumidityToLocation]
#print(Seeds)
#print(SeedToSoil,SoilToFertilizer,FertiliserToWater,WaterToLight,LightToTemperature,TemperatureToHumidity,HumidityToLocation)
NewSeeds = []
while len(Seeds) > 0:
    NewSeeds.append(Seeds[:2])
    Seeds = Seeds[2:]
NewSeeds = sorted(NewSeeds,key=lambda x:x[0])

print(NewSeeds)

Seed = 0
Location = 0
Working = True
while Working:
    Seed += 1
    Location = Seed
    for m in Manual[::-1]:
        for r in m:
            if Location in range(r[0],r[0]+r[2]):
                Location = Location-(r[0]-r[1])
                break
    for ran in NewSeeds:
        if Location >= ran[0] and Location < (ran[0]+ran[1]):
            Working = False
            break
print(Seed,Location)

#34039469 3751501334