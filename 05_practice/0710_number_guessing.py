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

random_numbers = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]

blackcoins = 0

print("Welcome to the number guessing game! Type a 4 digit number, for example: 2937.\n"
      "For every number you've guessed correct in the right position, you'll get a Black Coin.\n"
      "For every number you've guessed correct in the wrong position, you'll get a White Coin.\n"
      "You win by getting all four Black Coins. Good luck!")

while blackcoins < 4:
    blackcoins = 0
    whitecoins = 0
    number_guess = [int(x) for x in input("\nGuess a 4 digit number:\n")]
    for i in range(4):
        if number_guess[i] == random_numbers[i]:
            blackcoins += 1
            whitecoins -= 1
    for i in range(4):
        if number_guess[i] in random_numbers:
            whitecoins += 1
    print(f"Black coins: {blackcoins}. White coins: {whitecoins}.")

print("You guessed right! :D")


