from random import randint
import json


def genper():
    randperlist = []
    with open("randomdata/names.dat", 'r') as names:
        with open("randomdata/address.dat", 'r') as address:
            with open("randomdata/pin.dat", 'r') as pins:
                for i in range(50):
                    randpersonDict = dict()
                    randpersonDict['voter_name'] = names.readline()[:-1]
                    randpersonDict['aLine1'] = address.readline()[:-1]
                    randpersonDict['aLine2'] = address.readline()[:-1]
                    randpersonDict['pin'] = pins.readline()[:-1]
                    randpersonDict['s_code'] = randint(1, 5)
                    randpersonDict['c_code'] = randint(1, randpersonDict['s_code']*2)
                    randpersonDict['d_code'] = randint(1, randpersonDict['c_code']*2)
                    randpersonDict['age'] = randint(18, 100)
                    if i < 25:
                        randpersonDict['gender'] = 1
                    else:
                        randpersonDict['gender'] = 2
                    randpersonDict['aadhar_no'] = int(
                        ''.join([str(randint(1, 9)) for i in range(12)]))
                    randperlist.append(json.dumps(randpersonDict))
    return randperlist


print(genper()[0])
