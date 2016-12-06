
def recursive_mult(x, y):
	"""
	Implements grade school multiplication algorithm with recursion
	"""
	# base case, if x == 0 or y == 0, return 0
	# or if a = 1
	if x == 0 or y == 0:
		return 0
	elif x == 1:
		return y
	else:
		return recursive_mult(x-1, y) + y


if __name__ == "__main__":
	pairs = [[6, 3], [4, 1], [8000, 0]]
	for pair in pairs:
		product = recursive_mult(pair[0], pair[1])
		print(product)