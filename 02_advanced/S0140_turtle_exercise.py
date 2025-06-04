"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 3:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 4:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 5:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.

def demo():  # demonstration of basic turtle commands
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


tom = turtle.Turtle()  # create an object named tom of type Turtle


def square(length):
    print(type(tom))
    tom.speed(3)
    tom.forward(length)
    tom.right(90)
    tom.forward(length)
    tom.right(90)
    tom.forward(length)
    tom.right(90)
    tom.forward(length)
    tom.penup()
    turtle.done()


def many_squares(antal, størrelse, afstand):
    for x in range(antal):
        tom.forward(størrelse)
        tom.right(90)
        tom.forward(størrelse)
        tom.right(90)
        tom.forward(størrelse)
        tom.right(90)
        tom.forward(størrelse)
        tom.penup()
        tom.forward(afstand)
        tom.pendown()
    turtle.done()

def coolpattern(antal, størrelse, afstand):
    for x in range(antal):
        side_størrelse = størrelse
        for y in range(størrelse // 5):
            tom.forward(side_størrelse)
            tom.right(90)
            side_størrelse -= 5
        tom.penup()
        tom.setheading(0)
        tom.forward(størrelse + afstand)
        tom.pendown()
    turtle.done()


def starpatterns(antal, størrelse, afstand, type):

    if type >3:
        print("Type a number between 1 and 3 for 'type'.")
    else:
        tom.setheading(72)
        tom.speed(1)
        if type == 1:
            for x in range(antal):
                for y in range(5):
                    tom.forward(størrelse)
                    tom.right(144)
                tom.penup()
                tom.right(90)
                tom.forward(størrelse + afstand)
                tom.setheading(72)
                tom.pendown()
        elif type == 2:
            for x in range(antal):
                for y in range(7):
                    tom.forward(størrelse)
                    tom.right(154.2857)
                tom.penup()
                tom.right(90)
                tom.forward(størrelse + afstand)
                tom.setheading(72)
                tom.pendown()
        elif type == 3:
            for x in range(antal):
                for y in range(11):
                    tom.forward(størrelse)
                    tom.right(130.909)
                tom.penup()
                tom.right(90)
                tom.forward(størrelse + afstand)
                tom.setheading(72)
                tom.pendown()
    turtle.done()
