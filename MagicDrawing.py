import turtle

t = turtle.Turtle()

def rouge():
    t.color("red")

def bleu():
    t.color("blue")

def vert():
    t.color("green")

def noir():
    t.color("noir")

turtle.onkeypress(rouge, "r")
turtle.onkeypress(bleu, "b")
turtle.onkeypress(vert, "v")
turtle.onkeypress(noir, "n")
def haut():
    t.setheading(90)
    t.forward(20)

def bas():
    t.setheading(270)
    t.forward(20)

def gauche():
    t.setheading(180)
    t.forward(20)

def droite():
    t.setheading(0)
    t.forward(20)

turtle.listen()

turtle.onkeypress(haut, "Up")
turtle.onkeypress(bas, "Down")
turtle.onkeypress(gauche, "Left")
turtle.onkeypress(droite, "Right")

turtle.mainloop()
