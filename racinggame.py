import turtle, random


"""screen setup"""
s = turtle.Screen()
s.setup(width = 800, height = 600) #set the screen size for our game
s.bgpic('road.gif') #sets up the background pic

y_intercept = [262, 174, 87, 4, -83, -170, -258]

"""color pallet"""
colors = ["red", "orange", "blue",  "white", "yellow", "brown", "green"]


"""list of turtles"""
racers = []


"""turtle replicas"""
for i in range(7):
    racer = turtle.Turtle("turtle")
    racer.up()
    racer.shapesize(1.25)
    racer.goto(-375, y_intercept[i])
    racer.color(colors[i])
    racers.append(racer)

race_on = True
user_bet = s.textinput("ENTER YOUR BET", "Which turtle color: ").lower()

while race_on:
    for racer in racers:
        if racer.xcor() > 355:
            race_on = False
            winner = racer.pencolor()
            if winner == user_bet:
                turtle.write(f"Congratulations you won!, the {winner} racer is the winner", align="center",
            font=("Courier", 16, "normal"))
                turtle.ht()
            else:
                turtle.write(f"Better luck next time!, the {winner} racer is the winner", align="center",
            font=("Courier", 16, "normal"))
                turtle.ht()

        racer.fd(random.randint(0, 7))


s.exitonclick()