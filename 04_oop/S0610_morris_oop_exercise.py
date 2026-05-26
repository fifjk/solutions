"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Morris:
    def __init__(self, sleeplvl, thirstlvl, hungerlvl, whiskylvl, goldlvl, turnlvl):
        self.sleeplvl = sleeplvl
        self.thirstlvl = thirstlvl
        self.hungerlvl = hungerlvl
        self.whiskylvl = whiskylvl
        self.goldlvl = goldlvl
        self.turnlvl = turnlvl

    def sleep(self, sleepamount):
        while sleepamount > 0:
            if self.turnlvl >= 1000 or dead():
                break
            else:
                self.sleeplvl -= 10
                self.thirstlvl += 1
                self.hungerlvl += 1
                self.turnlvl += 1
                sleepamount -= 1
                if self.sleeplvl < 0:
                    self.sleeplvl = 0
                print(morris_state)
                print("Morris> slept.")
                if self.turnlvl >= 1000 or dead():
                    break

    def mine(self, mineamount):
        while mineamount > 0:
            if self.turnlvl >= 1000 or dead():
                break
            else:
                self.sleeplvl += 5
                self.thirstlvl += 5
                self.hungerlvl += 5
                self.goldlvl += 5
                self.turnlvl += 1
                mineamount -= 1
                print(morris_state)
                print("Morris mined.")
                if self.turnlvl >= 1000 or dead():
                    break

    def eat(self, eatamount):
        while eatamount > 0:
            if self.goldlvl <= 1:
                print("Morris does not have enough gold to perform this action.")
            else:
                if self.turnlvl >= 1000 or dead():
                    break
                else:
                    self.sleeplvl += 5
                    self.thirstlvl -= 5
                    self.hungerlvl -= 20
                    self.goldlvl -= 2
                    self.turnlvl += 1
                    eatamount -= 1
                    if self.thirstlvl < 0:
                        self.thirstlvl = 0
                    if self.hungerlvl < 0:
                        self.hungerlvl = 0
                    print(morris_state)
                    print("Morris ate.")
                    if self.turnlvl >= 1000 or dead():
                        break

    def buy_whisky(self, wamount):
        while wamount > 0:
            if self.goldlvl <= 0:
                print("Morris does not have enough gold to perform this action.")
            if self.whiskylvl >= 10:
                print("Morris already has the maximum amount of whisky.")
            else:
                if self.turnlvl >= 1000 or dead():
                    break
                else:
                    self.sleeplvl += 5
                    self.thirstlvl += 1
                    self.hungerlvl += 1
                    self.whiskylvl += 1
                    self.goldlvl -= 1
                    self.turnlvl += 1
                    wamount -= 1
                    print(morris_state)
                    print("Morris bought whisky.")
                    if self.turnlvl >= 1000 or dead():
                        break

    def drink(self, drinkamount):
        if self.whiskylvl <= 0:
            if not self.turnlvl >= 1000 and not dead():
                print("Morris does not have enough whisky to perform this action.")
        else:
            while drinkamount > 0:
                if self.turnlvl >= 1000 or dead():
                    break
                else:
                    self.sleeplvl += 5
                    self.thirstlvl -= 15
                    self.hungerlvl -= 1
                    self.whiskylvl -= 1
                    self.goldlvl += 0
                    self.turnlvl += 1
                    drinkamount -= 1
                    if self.thirstlvl < 0:
                        self.thirstlvl = 0
                    if self.hungerlvl < 0:
                        self.hungerlvl = 0
                    print(morris_state)
                    print("Morris drank whisky.")
                    if self.turnlvl >= 1000 or dead():
                        break

    def play(self):
        while not dead() and self.turnlvl < 1000:
            self.mine(10)
            self.buy_whisky(3)
            self.drink(2)
            self.eat(2)
            self.sleep(8)
            self.eat(2)
            self.drink(1)
            self.sleep(2)

    def __repr__(self):
        return f"Sleepiness: {self.sleeplvl}, thirst: {self.thirstlvl}, hunger: {self.hungerlvl}, whisky: {self.whiskylvl}, gold: {self.goldlvl}, turn: {self.turnlvl}"


def dead():
    return morris_state.sleeplvl >= 100 or morris_state.thirstlvl >= 100 or morris_state.hungerlvl >= 100


morris_state = Morris(0, 0, 0, 0, 0, 0)

if morris_state.sleeplvl < 0:
    morris_state.sleeplvl = 0

if morris_state.thirstlvl < 0:
    morris_state.thirstlvl = 0

if morris_state.hungerlvl < 0:
    morris_state.hungerlvl = 0

if dead():
    print("Morris died.")

morris_state.play()

print(f"You reached {morris_state.turnlvl} turns and Morris got {morris_state.goldlvl} gold.")