""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

-------

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

-------

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""

ongoing = True
while ongoing:
    print(f"This is a calculator.\n\n- Type '1' to use addition\n- Type '2' to use subtraction\n- Type '3' to use multiplication\n"
          f"- Type '4' to use division\n- Type '0' when you are done and want to end the program.\n")
    action = input("Pick an action and press Enter.\n")
    if action == "1":
        print("\nYou picked addition.\n")
        number1 = input("Type in the first number of the equation. Example: (First number) + (Second number).\n")
        number2 = input("Type in the second number of the equation.\n")
        print(f"\n{int(number1)} + {int(number2)} = {int(number1)+int(number2)}\n")
    elif action == "2":
        print("\nYou picked subtraction.\n")
        number1 = input("Type in the first number of the equation. Example: (First number) - (Second number).\n")
        number2 = input("Type in the second number of the equation.\n")
        print(f"\n{int(number1)} - {int(number2)} = {int(number1)-int(number2)}\n")
    elif action == "3":
        print("\nYou picked multiplication.\n")
        number1 = input("Type in the first number of the equation. Example: (First number) * (Second number).\n")
        number2 = input("Type in the second number of the equation.\n")
        print(f"\n{int(number1)} * {int(number2)} = {int(number1)*int(number2)}\n")
    elif action == "4":
        print("\nYou picked division.\n")
        number1 = input("Type in the first number of the equation. Example (First number) / (Second number).\n")
        number2 = input("Type in the second number of the equation.\n")
        print(f"\n{int(number1)} / {int(number2)} = {int(number1)/int(number2)}\n")
    elif action == "0":
        print("\nYou ended the program.\n")
        ongoing = False
    else:
        print("Invalid input. Try again.")
