with open("adventofcode2023\Day3\\input.txt") as file:
    engine = [["." for x in range(142)]]
    for line in file:
        row = ["."]
        for character in line.strip():
            row.append(character)
        row.append(".")
        engine.append(row)
    row = ["." for x in range(142)]
    engine.append(row)

#Task1            
result = 0

for y in range(1,len(engine)-1):
    skip = 0
    for x in range(1,len(engine[y])-1):
        if skip > 0:
            skip -= 1
            continue

        if engine[y][x].isdigit() == True:
            if engine[y][x+1].isdigit() == True:
                if engine[y][x+2].isdigit() == True: #3 digit
                    skip = 2
                    temp = int(str(engine[y][x]) + str(engine[y][x+1]) + str(engine[y][x+2]))
                    if engine[y][x-1] != ".":
                        result += temp
                    elif engine[y][x+3] != ".":
                        result += temp
                    else:    
                        for offset in range(-1,4):
                            if engine[y-1][x+offset] != ".":
                                result += temp
                                break
                            elif engine[y+1][x+offset] != ".":
                                result += temp
                                break

                else: #2 digit
                    skip = 1
                    temp = int(str(engine[y][x]) + str(engine[y][x+1]))
                    if engine[y][x-1] != ".":
                        result += temp
                    elif engine[y][x+2] != ".":
                        result += temp
                    else:    
                        for offset in range(-1,3):
                            if engine[y-1][x+offset] != ".":
                                result += temp
                                break
                            elif engine[y+1][x+offset] != ".":
                                result += temp
                                break

            else: #1 digit
                temp = int(str(engine[y][x]))
                if engine[y][x-1] != ".":
                    result += temp
                elif engine[y][x+1] != ".":
                    result += temp
                else:    
                    for offset in range(-1,2):
                        if engine[y-1][x+offset] != ".":
                            result += temp
                            break
                        elif engine[y+1][x+offset] != ".":
                            result += temp
                            break
print("Task1: ",result)

#Task2
result = 0
for y in range(1,len(engine)-1):
    for x in range(1,len(engine[y])-1):
        if engine[y][x] == "*":
            gears = []
            for offset in range(-1,2,2):
                if engine[y+offset][x].isdigit() == True:
                    if engine[y+offset][x+1].isdigit() == True:
                        if engine[y+offset][x+2].isdigit() == True: #3 digit
                            gears.append(int(str(engine[y+offset][x]) + str(engine[y+offset][x+1]) + str(engine[y+offset][x+2])))
                        elif engine[y+offset][x-1].isdigit() == True: #3 digit
                            gears.append(int(str(engine[y+offset][x-1]) + str(engine[y+offset][x]) + str(engine[y+offset][x+1])))
                        else: #2 digit
                            gears.append(int(str(engine[y+offset][x]) + str(engine[y+offset][x+1])))
                    elif engine[y+offset][x-1].isdigit() == True:
                        if engine[y+offset][x-2].isdigit() == True: #3 digit
                            gears.append(int(str(engine[y+offset][x-2]) + str(engine[y+offset][x-1]) + str(engine[y+offset][x])))
                        else: #2 digit
                            gears.append(int(str(engine[y+offset][x-1]) + str(engine[y+offset][x])))
                    else: #1 digit
                        gears.append(int(str(engine[y+offset][x])))
                else:
                    for offset2 in range(-1,2,2):
                        if engine[y+offset][x+(1*offset2)].isdigit() == True:
                            a = engine[y+offset][x+(1*offset2)]
                            if engine[y+offset][x+(2*offset2)].isdigit() == True:
                                b = engine[y+offset][x+(2*offset2)]
                                if engine[y+offset][x+(3*offset2)].isdigit() == True:
                                    c = engine[y+offset][x+(3*offset2)]
                                    gears.append(int((a+b+c)[::offset2]))
                                else:
                                    gears.append(int((a+b)[::offset2]))
                            else:
                                gears.append(int(a))

                if engine[y][x+(1*offset)].isdigit() == True:
                    a = engine[y][x+(1*offset)]
                    if engine[y][x+(2*offset)].isdigit() == True:
                        b = engine[y][x+(2*offset)]
                        if engine[y][x+(3*offset)].isdigit() == True:
                            c = engine[y][x+(3*offset)]
                            gears.append(int((a+b+c)[::offset]))
                        else:
                            gears.append(int((a+b)[::offset]))
                    else:
                        gears.append(int(a))

            if len(gears) == 2:
                result += (gears[0] * gears[1])
            
print("Task2: ",result)
