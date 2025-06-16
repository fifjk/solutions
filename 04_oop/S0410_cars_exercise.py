"""
Opgave "Cars":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en funktion drive_car(), der udskriver en bils motorlyd (f.eks. "roooaar")

I hovedprogrammet:
    Definer variabler, som repræsenterer antallet af hjul og den maksimale hastighed for 2 forskellige biler
    Udskriv disse egenskaber for begge biler
    Kald derefter funktionen drive_car()

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du åbne S0420_cars_help.py og starte derfra.
Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du stadig er gået i stå, skal du åbne S0430_cars_solution.py og sammenligne den med din løsning.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Team-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

def drive_vehicle(vehicle):
    if vehicle == 1:
        print("You rode the bike.")
        print(vehicle1_sound)
    if vehicle == 2:
        print("You drove the car.")
        print(vehicle2_sound)


vehicle1 = "Bike"
vehicle2 = "Car"

vehicle1_wheels = 2
vehicle2_wheels = 4

vehicle1_speed = "90 km/h"
vehicle2_speed = "150 km/h"

vehicle1_sound = "Rawr"
vehicle2_sound = "Vroom"

print(f"1. Vehicle: {vehicle1}. Number of wheels: {vehicle1_wheels}. Maximum speed: {vehicle1_speed}.")
print(f"2. Vehicle: {vehicle2}. Number of wheels: {vehicle2_wheels}. Maximum speed: {vehicle2_speed}.")

user_input = input("Which will you choose? Type 1 or 2 below.\n")

if user_input == "1":
    drive_vehicle(1)
if user_input == "2":
    drive_vehicle(2)