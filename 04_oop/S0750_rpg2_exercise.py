"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""

import random

class Character:

    def __init__(self, name, max_health, current_health, attackpower):
        self.name = name
        self.max_health = max_health
        self._current_health = current_health
        self.attackpower = attackpower
        self.sleeping = False
        self.dead = False

    def __repr__(self):
        return (f"{self.name} currently has {self._current_health} health, with a max health of {self.max_health}. "
                f"Their attackpower is {self.attackpower}.")

    def is_sleeping(self):
        if self.sleeping:
            self.sleeping = False
            print(f"{self.name} woke up.")

    def hit(self, other):
        if other.dead:
            print(f"{other.name} is dead. {self.name} cannot attack them.")
        elif self.dead:
            print(f"{self.name} is dead. They cannot attack.")
        elif self.sleeping:
            self.sleeping = False
        else:
            if self.sleeping:
                print(f"{self.name} was told to attack {other.name}, but {self.name} is sleeping.")
            else:
                hit_or_miss = random.randint(1, 10)
                if hit_or_miss == 1:
                    print(f"{self.name} tried to attack {other.name} but missed!")
                else:
                    print(f"{self.name} attacked {other.name}!")
                    other.get_hit(self.attackpower)

    def get_hit(self, attackpower):
        if (self._current_health - attackpower) <= 0:
            print(f"{self.name} died.")
            self.dead = True
        else:
            self._current_health -= attackpower
            print(f"{self.name} took {attackpower} damage. They now have {self._current_health} health.")
            self.is_sleeping()

    def get_healed(self, healpower):
        if self._current_health <= (self.max_health - healpower):
            self._current_health += healpower
            print(f"{self.name} got healed {healpower} health. They now have {self._current_health} health.")
        else:
            extra_health = self.max_health - self._current_health
            self._current_health = self.max_health
            print(f"{self.name} got healed {extra_health} health. They now have {self._current_health} health.")

    def get_commanded(self):
        if (self._current_health - self.attackpower) <= 0:
            print(f"{self.name} died.")
            self.dead = True
        else:
            self._current_health -= self.attackpower
            self.is_sleeping()
            print(f"{self.name} hit themself and took {self.attackpower} damage. They now have {self._current_health} health.")

    def get_slept(self):
        self.is_sleeping()
        print(f"{self.name} successfully got slept. They will sleep through their next move, or until they are attacked or commanded.")
        self.sleeping = True


class Healer(Character):

    def __init__(self, name, max_health, current_health, healpower):
        super().__init__(name, max_health, current_health, 5)
        self.healpower = healpower

    def __repr__(self):
        return (f"{self.name} currently has {self._current_health} health, with a max health of {self.max_health}. "
                f"Their healpower is {self.healpower}.")

    def heal(self, other):
        if other.dead:
            print(f"{other.name} is dead. {self.name} cannot heal them.")
        elif self.dead:
            print(f"{self.name} is dead. They cannot heal.")
        else:
            hit_or_miss = random.randint(1, 10)
            if hit_or_miss == 1:
                print(f"{self.name} tried to heal {other.name} but failed!")
            else:
                print(f"{self.name} healed {other.name}!")
                other.get_healed(self.healpower)


class Puppeteer(Character):

    def __init__(self, name, max_health, current_health, max_psychicenergy, psychicenergy):
        super().__init__(name, max_health, current_health, 10)
        self.maxpsyenergy = max_psychicenergy
        self.psyenergy = psychicenergy

    def __repr__(self):
        return (f"{self.name} currently has {self._current_health} health, with a max health of {self.max_health}. "
                f"Their current psychic energy is at {self.psyenergy}, and their maximum is {self.maxpsyenergy}.")

    def command(self, other):
        if self.psyenergy < (self.maxpsyenergy/5):
            print(f"The puppeteer needs at least 20 psychic energy to command someone.")
        elif other.dead:
            print(f"{other.name} is dead. {self.name} cannot command them.")
        elif self.dead:
            print(f"{self.name} is dead. They cannot command.")
        else:
            self.is_sleeping()
            if self.sleeping:
                print(f"{self.name} was told to command {other.name}, but {self.name} is sleeping.")
            else:
                hit_or_miss = random.randint(1, 10)
                if hit_or_miss == 1:
                    print(f"{self.name} tried to command {other.name} but they resisted!")
                else:
                    print(f"{self.name} commanded {other.name} to hit themself!")
                    other.get_commanded()

    def restore_energy(self):
        if self.psyenergy <= (self.maxpsyenergy - (self.maxpsyenergy/5)):
            self.psyenergy += (self.maxpsyenergy/5)
            print(f"{self.name} recovered {(self.maxpsyenergy/5)} psychic energy. They now have {self.psyenergy} psychic energy.")
        else:
            extra_energy = self.maxpsyenergy - (self.maxpsyenergy/5)
            self.psyenergy = self.maxpsyenergy
            print(f"{self.name} got recovered {extra_energy} psychic energy. They now have {self._current_health} psychic energy.")

class Bard(Character):

    def __init__(self, name, max_health, current_health, chance_of_success):
        super().__init__(name, max_health, current_health, 5)
        self.success_chance = chance_of_success

    def __repr__(self):
        return (f"{self.name} currently has {self._current_health} health, with a max health of {self.max_health}. "
                f"Their chance of success at at singing someone to sleep is {self.success_chance}.")

    def sing(self, other):
        if other.dead:
            print(f"{other.name} is dead. {self.name} cannot sing them to sleep.")
        elif self.dead:
            print(f"{self.name} is dead. They cannot sing.")
        else:
            print(f"{self.name} is attempting to sing {other.name} to sleep...")
            success = random.randint(1, self.success_chance)
            if success == 1:
                other.get_slept()
            else:
                print(f"{self.name} was unsuccessful.")


hero = Character("Hero", 100, 100, 20)
villain = Character("Villain", 100, 20, 20)
healer = Healer("Healer", 60, 60, 20)
puppeteer = Puppeteer("Puppeteer", 80, 20, 100, 100)
bard = Bard("Bard", 60, 60, 3)


character_names = {
    "villain": villain,
    "hero": hero,
    "healer": healer,
    "puppeteer": puppeteer,
    "bard": bard
}

team1 = [hero, healer, bard]
team2 = [villain, puppeteer]


def play_game():
    round_number = 1
    end_game = False
    while not end_game:
        if hero.dead and healer.dead and bard.dead:
            end_game = True
            continue
        elif villain.dead and puppeteer.dead:
            end_game = True
            continue
        else:
            end_game = False

        if round_number == 1:
            print(f"Round {round_number}\n")
            move = input("What's your move? Type 'help' for help.\n")
        else:
            print(f"\nRound {round_number}\n")
            move = input("What's your next move? Type 'help' for help.\n")

        if move == "help":
            print("Your current options are:\n"
                  "Attack: hero_attack\n"
                  "Heal: healer_heal\n"
                  "Sing: bard_sing\n"
                  "Make sure to type in lower case!")

            continue

        elif move == "hero_attack":
            target_name = input("Who should Hero attack?\n")
            target = character_names.get(target_name)
            hero.hit(target)
            round_number += 1

        elif move == "villain_attack":
            target_name = input("Who should Villain attack?\n")
            target = character_names.get(target_name)
            villain.hit(target)
            round_number += 1

        elif move == "healer_heal":
            target_name = input("Who should Healer heal?\n")
            target = character_names.get(target_name)
            healer.heal(target)
            round_number += 1

        elif move == "puppeteer_command":
            target_name = input("Who should Puppeteer command?\n")
            target = character_names.get(target_name)
            puppeteer.command(target)
            round_number += 1

        elif move == "bard_sing":
            target_name = input("Who should Bard sing to?\n")
            target = character_names.get(target_name)
            bard.sing(target)
            round_number += 1

        print("")
        who_attacks = random.randint(1, len(team2))
        whos_attacked = random.randint(1, len(team1))
        if villain.dead and puppeteer.dead:
            continue
        else:
            if who_attacks == 1:
                if villain.dead:
                    if whos_attacked == 1:
                        puppeteer.command(hero)
                    elif whos_attacked == 2:
                        puppeteer.command(healer)
                    elif whos_attacked == 3:
                        puppeteer.command(bard)
                elif whos_attacked == 1:
                    villain.hit(hero)
                elif whos_attacked == 2:
                    villain.hit(healer)
                elif whos_attacked == 3:
                    villain.hit(bard)
            else:
                if puppeteer.dead:
                    if whos_attacked == 1:
                        villain.hit(hero)
                    elif whos_attacked == 2:
                        villain.hit(healer)
                    elif whos_attacked == 3:
                        villain.hit(bard)
                if whos_attacked == 1:
                    puppeteer.command(hero)
                elif whos_attacked == 2:
                    puppeteer.command(healer)
                elif whos_attacked == 3:
                    puppeteer.command(bard)

    if villain.dead and puppeteer.dead:
        print("Villain and Puppeteer both died. Team 1 won.")
    else:
        print("Hero, Healer and Bard all died. Team 2 won.")


play_game()
