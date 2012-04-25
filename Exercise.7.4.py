def eval_loop():
	a=raw_input()
	while a != 'done':
		print eval(a)
		eval_loop()
		return
