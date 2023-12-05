Seeds = []
SeedToSoil = []
SoilToFertilizer = []
FertiliserToWater = []
WaterToLight = []
LightToTemperature = []
TemperatureToHumidity = []
HumidityToLocation = []
a = []
with open("Hrdy\Day5\Test.txt","r") as f:
    Seeds = [int(x) for x in f.readline().split(": ")[1].strip().split(" ")]
    for line in f:
        a.append(line.strip())

print(Seeds)
print(a)