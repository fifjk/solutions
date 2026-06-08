"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.

Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en metode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en metode ved navn wag_tail for Dog. Denne metode udskriver i konsollen noget i stil
    med "Hunden Snoopy vifter med sin 32 cm lange hale".
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father) undenfor klassen. Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google hvordan man laver det.

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import random

class Animal:

    def __init__(self, name, sound, height, weight, legs, female):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return (f"Name: {self.name}. Sound: {self.sound}. Height: {self.height}cm. Weight: {5.6}kg. Legs: {self.legs}. "
                f"Female: {self.female}.")

    def make_noise(self):
        return f"{self.sound}!"


class Dog(Animal):

    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep

    def __repr__(self):
        return (f"Dog - Name: {self.name}. Sound: {self.sound}. Height: {self.height}cm. Weight: {self.weight}kg. Legs: {self.legs}. "
                f"Female: {self.female}. Tail length: {self.tail_length}cm. Hunts sheep: {self.hunts_sheep}.")

    def __add__(self, other):
        return mate(self, other)

    def wag_tail(self):
        if self.female:
            return f"The dog {self.name} wags her {self.tail_length}cm long tail."
        else:
            return f"The dog {self.name} wags his {self.tail_length}cm long tail."


random_female_names = ["Mini", "Delilah", "Bella", "Poppy", "Daisy", "Millie", "Molly", "Rosie", "Lola", "Roxy", "Ruby", "Tilly", "Bailey",
                       "Marley", "Tia", "Holly", "Lucy", "Lexi", "Lady"]
random_male_names = ["Charlie", "Carl", "Xander", "Warren", "Max", "Buster", "Alfie", "Buddy", "Barney", "Toby", "Milo", "Archie", "Bruno",
                     "Rocky", "Billy", "Bear", "Jack", "Benji", "Jake"]

def mate(mother, father):
    if not mother.female or father.female:
        print("Error mating. The arguments need to be a female and a male dog.")
        return ""
    else:
        is_female = random.choice([True, False])
        if is_female:
            new_name = random_female_names.pop(random.randrange(len(random_female_names)))
        else:
            new_name = random_male_names.pop(random.randrange(len(random_male_names)))
        new_sound = random.choice(["bark", "woof"])
        new_height = random.randint(10, 80)
        new_weight = random.randint(2, 15)
        new_legs = 4
        new_tail_length = random.randint(1, 60)
        new_hunts_sheep = random.choice([True, False])
        new_dog = Dog(new_name, new_sound, new_height, new_weight, new_legs, is_female, new_tail_length, new_hunts_sheep)
        return new_dog


dinosaur = Animal("Dinosaur", "rawr", 500.85, 300, 4, False)
cow = Animal("Cow", "moo", 100, 100, 4, True)
snake = Animal("Snake", "sss", 10, 30, 0, True)

luna = Dog("Luna", "woof", 30.9, 5.6, 4, True, 40, False)
vio = Dog("Violetta", "woof", 45.8, 8.9, 4, True, 50, False)
chess = Dog("Chess", "woof", 30, 6.8, 4, False, 5, True)
larry = Dog("Larry", "bark", 38.9, 10.2, 3, False, 32.4, True)


print(dinosaur)
print(Animal.make_noise(dinosaur))
print(luna)
print(Dog.make_noise(luna))
print(Dog.wag_tail(luna))
print(Dog.wag_tail(chess))
new_dog_1 = luna + chess
new_dog_2 = vio + larry
new_dog_3 = luna + new_dog_1

print(new_dog_1)
print(new_dog_2)
print(new_dog_3)
