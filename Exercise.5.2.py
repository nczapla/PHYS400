def is_triangle(a,b,c):
	if a>=b+c:
		print 'Not today junior!'
	else:
		if b>=a+c:
			print 'Not today junior!'
		else:
			if c>=a+b:
				print 'Not today junior!'
			else:
				print 'Houston we have lift off!'


def is_triangle1():
	print 'Pick three numbers greater than 0 to see if they can form a triangle'
	a=float(raw_input('a=?\n'))
	b=float(raw_input('b=?\n'))
	c=float(raw_input('c=?\n'))
	is_triangle(a,b,c)