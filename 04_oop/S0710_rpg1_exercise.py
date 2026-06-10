"""Opgave: Objektorienteret rollespil, afsnit 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
    _current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Del 2:
    Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.

Del 3:
    Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Del 4:
    Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
    Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.
    Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
    Definer derfor en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Del 5:
    Tilføj en klasse "Healer", som arver fra klassen Character.
    En healer har attackpower=0 men den har en ekstra attribut "healpower".

Del 6:
    Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
    For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
    tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Character:

    def __init__(self, name, max_health, _current_health, attackpower):
        self.name = name
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower

    def __repr__(self):
        return (f"{self.name} currently has {self._current_health} health, with a max health of {self.max_health}. "
                f"Their attackpower is {self.attackpower}.")

    def hit(self, other):
        if other.max_health <= 0:
            print(f"{other.name} is dead. {self.name} cannot attack them.")
        elif self.max_health <= 0:
            print(f"{self.name} is dead. They cannot attack.")
        else:
            print(f"{self.name} attacked {other.name}!")
            other.get_hit(self.attackpower)

    def get_hit(self, damage):
        if (self._current_health - damage) <= 0:
            self._current_health -= damage
            print(f"{self.name} died.")
            self.max_health = self._current_health
        else:
            self._current_health -= damage
            print(f"{self.name} took {damage} damage. They now have {self._current_health} health.")

    def get_healed(self, heal_amount):
        if self._current_health <= (self.max_health - heal_amount):
            self._current_health += heal_amount
            print(f"{self.name} got healed {heal_amount} health. They now have {self._current_health} health.")
        else:
            extra_health = self.max_health - self._current_health
            self._current_health = self.max_health
            print(f"{self.name} got healed {extra_health} health. They now have {self._current_health} health.")


class Healer(Character):

    def __init__(self, name, max_health, _current_health, healpower):
        super().__init__(name, max_health, _current_health, 0)
        self.healpower = healpower

    def __repr__(self):
        return (f"{self.name} currently has {self._current_health} health, with a max health of {self.max_health}. "
                f"Their healpower is {self.healpower}.")

    def heal(self, other):
        if other.max_health <= 0:
            print(f"{other.name} is dead. {self.name} cannot heal them.")
        elif self.max_health <= 0:
            print(f"{self.name} is dead. They cannot heal.")
        else:
            print(f"{self.name} healed {other.name}!")
            other.get_healed(self.healpower)


hero = Character("Hero", 100, 100, 10)
villain = Character("Villain", 100, 100, 20)
healer = Healer("Healer", 80, 80, 20)