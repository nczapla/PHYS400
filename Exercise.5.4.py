from TurtleWorld import *
world=TurtleWorld()
t=Turtle()
t.delay=.01


def koch(x):
	if x<3:
		fd(t,x)
	else:
		fd(t,x/3)
		lt(t,60)
		fd(t,x/3)
		rt(t,120)
		fd(t,x/3)
		lt(t,60)
		fd(t,x/3)

def snowflake(x,n):
	a=360/n
	for i in range(n):
		koch(x)
		rt(t,a)
		koch(x)
		lt(t,180-a)
	return