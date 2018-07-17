import turtle

bob = turtle.Turtle()

def quad():
   for i in range(4):
       bob.fd(100)
       bob.lt(90)
       

def perqua(tam, ang):
    for i in range(60):
        bob.fd(tam)
        bob.lt(ang)

perqua(200, 125)
