"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


def sleep(sleepamount):
    while sleepamount > 0:
        if morris["turn"] >= 1000 or dead():
            break
        else:
            morris["sleepiness"] -= 10
            morris["thirst"] +=1
            morris["hunger"] +=1
            morris["whisky"] += 0
            morris["gold"] += 0
            morris["turn"] += 1
            sleepamount -=1
            if morris["sleepiness"] < 0:
                morris["sleepiness"] = 0
            print(morris)
            if morris["turn"] >=1000  or dead():
                break

def mine(mineamount):
    while mineamount > 0:
        if morris["turn"] >= 1000 or dead():
            break
        else:
            morris["sleepiness"] +=5
            morris["thirst"] += 5
            morris["hunger"] += 5
            morris["whisky"] += 0
            morris["gold"] += 5
            morris["turn"] += 1
            mineamount -= 1
            print(morris)
            if morris["turn"] >= 1000 or dead():
                break

def eat(eatamount):
    while eatamount > 0:
        if morris["gold"] <= 1:
            print("Morris does not have enough gold to perform this action.")
        else:
            if morris["turn"] >= 1000 or dead():
                break
            else:
                morris["sleepiness"] +=5
                morris["thirst"] -=5
                morris["hunger"] -=20
                morris["whisky"] += 0
                morris["gold"] -=2
                morris["turn"] += 1
                eatamount -= 1
                if morris["thirst"] < 0:
                    morris["thirst"] = 0
                if morris["hunger"] < 0:
                    morris["hunger"] = 0
                print(morris)
                if morris["turn"] >= 1000 or dead():
                    break

def buy_whisky(wamount):
    while wamount >0:
        if morris["gold"] <= 0:
            print("Morris does not have enough gold to perform this action.")
        if morris["whisky"] >= 10:
            print("Morris already has the maximum amount of whisky.")
        else:
            if morris["turn"] >= 1000 or dead():
                break
            else:
                morris["sleepiness"] +=5
                morris["thirst"] +=1
                morris["hunger"] +=1
                morris["whisky"] += 1
                morris["gold"] -=1
                morris["turn"] +=1
                wamount -= 1
                print(morris)
                if morris["turn"] >= 1000 or dead():
                    break

def drink(drinkamount):
    if morris["whisky"] <= 0:
        if not morris["turn"] >= 1000 and not dead():
            print("Morris does not have enough whisky to perform this action.")
    else:
        while drinkamount > 0:
            if morris["turn"] >= 1000 or dead():
                break
            else:
                morris["sleepiness"] +=5
                morris["thirst"] -=15
                morris["hunger"] -=1
                morris["whisky"] -= 1
                morris["gold"] += 0
                morris["turn"] +=1
                drinkamount -= 1
                if morris["thirst"] < 0:
                    morris["thirst"] = 0
                if morris["hunger"] < 0:
                    morris["hunger"] = 0
                print(morris)
                if morris["turn"] >= 1000 or dead():
                    break


def dead():
    return morris["sleepiness"] >=100 or morris["thirst"] >= 100 or morris["hunger"] >= 100


morris = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}

if morris["sleepiness"] < 0:
    morris["sleepiness"] = 0

if morris["thirst"] < 0:
    morris["thirst"] = 0

if morris["hunger"] < 0:
    morris["hunger"] = 0



#notdone
while not dead() and morris["turn"] < 1000:
    mine(10)
    buy_whisky(3)
    drink(2)
    eat(2)
    sleep(8)
    eat(2)
    drink(1)
    sleep(2)



if dead():
    print("Morris died.")