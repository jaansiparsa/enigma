LASTNAME = "Parsa"

def enigma(starting_rotors, starting_positions, message):
    # initialize rotors and reflector {left value: right value}
    rotor1 = {0: 1, 1: 3, 2: 6, 3: 0, 4: 5, 5: 4, 6: 8, 7: 7, 8: 9, 9: 2}
    rotor2 = {0: 0, 1: 3, 2: 5, 3: 2, 4: 6, 5: 9, 6: 1, 7: 4, 8: 8, 9: 7}
    rotor3 = {0: 5, 1: 9, 2: 1, 3: 7, 4: 3, 5: 8, 6: 0, 7: 2, 8: 4, 9: 6}
    rotor4 = {0: 1, 1: 6, 2: 5, 3: 2, 4: 9, 5: 0, 6: 7, 7: 4, 8: 3, 9: 8}
    reflector = {0: 3, 3: 0, 1: 6, 6: 1, 2: 8, 8: 2, 4: 5, 5: 4, 7: 9, 9: 7}
    # make list of starting rotors
    rotorlist = []
    halfwaylist = []
    final = ""
    for i in starting_rotors:
        if i == 1:
            rotorlist.append(rotor1)
        elif i == 2:
            rotorlist.append(rotor2)
        elif i == 3:
            rotorlist.append(rotor3)
        else:
            rotorlist.append(rotor4)
    # set rotors to starting positions
    tracker = 0
    for i in starting_positions:
        the_rotor = rotorlist[tracker]
        temp_rotor = {}
        for index in the_rotor:
            temp_rotor[int(str(index + i)[-1])] = int(str(the_rotor[index]+i)[-1])
        rotorlist[tracker] = temp_rotor
        tracker += 1
    # get to reflector
    counter = 0
    copy3 = rotorlist[2].copy()
    copy2 = rotorlist[1].copy()
    copy1 = rotorlist[0].copy()
    for x in str(message):
        y = int(x)
        for i in copy3:
            rotorlist[2][int(str(i + counter)[-1])] = int(str(copy3[i] + counter)[-1])
        for i in copy2:
            rotorlist[1][int(str(i + (counter//10))[-1])] = int(str(copy2[i] + (counter//10))[-1])
        for i in copy1:
            rotorlist[0][int(str(i + (counter//100))[-1])] = int(str(copy1[i] + (counter//100))[-1])
        for num in range(0, 3):
            y = rotorlist[num][y]
        y = reflector[y]
        halfwaylist.append(y)
        # coming back from reflector
        for num in range (2, -1, -1):
            for i in rotorlist[num]:
                if y == rotorlist[num][i]:
                    y = i
                    break
        final = final + str(y)
        counter += 1
    return int(final)