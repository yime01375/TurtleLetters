import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.setpos(40, 0)
        tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	tur.setheading(0)
        tur.pu()
	tur.forward(30)
        tur.right(180)
        tur.forward(30)
        tur.left(90)
        tur.forward(60)
        tur.left(90)
        tur.forward(30)
        tur.left(90)
        tur.forward(20)
        tur.left(90)
        tur.forward(20)
        tur.right(180)
        tur.forward(20)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(30)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(30)
        tur.pu()
        tur.setpos(40,0)
	   		
    elif letter == "H":
	tur.setheading(0)
        tur.pu()
	tur.left(90)
	tur.forward(60)
	tur.left(180)
	tur.forward(30)
	tur.right(90)
	tur.forward(20)
	tur.right(90)
	tur.forward(30)
	tur.right(180)
	tur.forward(60)
	tur.pu()
	tur.setpos(40,0)  
	 
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	tur.setheading(0)
        tur.pu()
	tur.fd(5)
	tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
	tur.right(90)
	tur.fd(20)
	tur.right(90)
	tur.fd(30)
	tur.pu()
        tur.setpos(40, 0)
        tur.right(180)
    elif letter == "V":
	tur.setheading(0)
	tur.pu()
	tur.fd(5)
	tur.right(45)
	tur.fd(5)
	tur.pd()
	tur.fd(30)
	tur.right(270)
	tur.fd(30)
	tur.pu()
	tur.setpos(40,0)
	tur.right(180)
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
