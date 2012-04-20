from TurtleWorld import *
world=TurtleWorld()
bob=Turtle()
bob.delay=.01

def draw(length, n):
	if n <= 0:
		return
	angle = 50
	fd(bob, length*n)
	lt(bob, angle)
	draw(length, n-1)
	rt(bob, 2*angle)
	draw(length, n-1)
	lt(bob, angle)
	bk(bob, length*n)