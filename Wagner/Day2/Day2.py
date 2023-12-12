with open("adventofcode2023\Day2\input.txt") as file:
    games = []

    #reformatting file into nested list
    for line in file: 
        games.append(line.strip().split(";"))

skip = 0
results = []

for cell in games:

    game_counter = []

    #strip gameIDs from games list
    if len(str(games.index(cell) + 1)) ==  1:
        cell[0] = cell[0][8:]
    elif len(str(games.index(cell) + 1)) == 2:
        cell[0] = cell[0][9:]
    else: cell[0] = cell[0][10:]

    for round in cell:

        round_counter = [0,0,0] #red, green, blue

        for character in range(0,len(round)):

            addor = 0
            
            if skip == 1:
                skip = 0
                continue

            if round[character].isdigit() == True: #if digit
                if round[character + 1].isdigit() == True: #2 digit

                    addor = int(round[character] + round[character + 1])

                    if round[character + 3] == "r": #red
                        round_counter[0] += addor 
                    elif round[character + 3] == "g": #green
                        round_counter[1] += addor
                    else: #blue
                        round_counter[2] += addor

                    skip = 1

                else: #1 digit

                    addor = int(round[character])

                    if round[character + 2] == "r":
                        round_counter[0] += addor 
                    elif round[character + 2] == "g":
                        round_counter[1] += addor
                    else:
                        round_counter[2] += addor
            
        game_counter.append(round_counter)

    results.append(game_counter)

Task1 = []
Task2 = 0

#Task1
for cell in results:
    Possible = True
    for round in cell:
        if round[0] > 12:
            Possible = False
        elif round[1] > 13:
            Possible = False
        elif round[2] > 14:
            Possible = False
    if Possible == True:
        Task1.append(results.index(cell)+1)

print(f"Task1: {sum(Task1)}")

#Task2
for cell in results:
    r_max = 0
    g_max = 0
    b_max = 0
    for round in cell:
        if round[0] > r_max:
            r_max = round[0]
        if round[1] > g_max:
            g_max = round[1]
        if round[2] > b_max:
            b_max = round[2]
    Task2 += (r_max * b_max * g_max)

print(f"Task2: {Task2}")
