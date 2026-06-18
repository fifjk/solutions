""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import random

ongoing = True

def randomizer():
    return random.randint(0, 9)


numberlist = [randomizer(), randomizer(), randomizer(), randomizer()]

print("Welcome to the number guessing game. There will be generated 4 random numbers between 0-9, and you will try to guess each one in order.\n"
      "If you guess a number correct in the right position, you get a black coin. If you guess a number correct but in the incorrect position, you get a white coin.\n"
      "You will play until you've got all the numbers correct in their right positions.\n\n"
      "Starting game...\n"
      "Game started!\n\n"
      "Generating numbers...\n"
      "Numbers generated!\n\n")


while ongoing:
    blackcoins = 0
    whitecoins = 0
    number1 = input("Please guess the first number between 0 and 9.\n")
    number2 = input("Please guess the second number between 0 and 9.\n")
    number3 = input("Please guess the third number between 0 and 9.\n")
    number4 = input("Please guess the fourth number between 0 and 9.\n\n")
    if number1 == numberlist[0]:
        blackcoins += 1
    elif number1 in numberlist:
        whitecoins += 1
    else:
        continue
    if number2 == numberlist[1]:
        blackcoins += 1
    elif number2 in numberlist:
        whitecoins += 1
    else:
        continue
    if number3 == numberlist[2]:
        blackcoins += 1
    elif number3 in numberlist:
        whitecoins += 1
    else:
        continue
    if number4 == numberlist[3]:
        blackcoins += 1
    elif number4 in numberlist:
        whitecoins += 1
    else:
        continue


