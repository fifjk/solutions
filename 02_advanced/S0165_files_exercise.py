"""
Opgave "Reading from a file":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Opret en tekstfil med en editor efter eget valg (pycharm, notepad, notepad++ osv.)
Hver række skal bestå af en persons navn efterfulgt af et mellemrum og et tal, der repræsenterer personens alder.
gem filen i din løsningsmappe

Skriv et program, der læser filen til en liste af strings.
Derefter brug indholdet af hver string til at udskrive en række som f.eks:
    <navn> er <alder> år gammel.

-------
Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""

datatest = ["Fifi 17\n", "Chrille 18\n", "Sisi 18\n", "Julli 17\n", "Isa 17\n"]
filenfr = "filetest"


with open(filenfr) as file:
    lines = file.readlines()
line_number = 0
for line in lines:
    line_number += 1
    print(f"Line {line_number}: {line.strip()}")
print()


navneting = ["Fifi\n", "17\n", "Chrille\n", "18\n", "Sisi\n", "18\n", "Julli\n", "17\n" "Isa\n", "17\n", "Missy\n", "16\n"]
navnefil = "folksnavne"



with open(navnefil) as file:
    for x, line in enumerate(file):
        if x % 2 == 0:
            navn = line.strip()
        else:
            alder = line.strip()
            print(f"{navn} er {alder} år gammel")
print()