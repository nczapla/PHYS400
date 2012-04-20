from TurtleWorld import *

def polygon(r,P):
	import math
	world=TurtleWorld()
	bob=Turtle()
	bob.delay=.01
	A=360/P
	p=math.sqrt(2*(r**2)-2*r*r*(math.cos(A*(math.pi)/180)))
	B=(math.asin(r*math.sin(A*(math.pi)/180)/p))*180/(math.pi)
	for i in range(P):
		fd(bob,r)
		lt(bob,180-B)
		fd(bob,p)
		lt(bob,180-B)
		fd(bob,r)
		lt(bob,180)