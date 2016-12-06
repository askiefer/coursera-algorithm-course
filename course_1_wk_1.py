
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

def karatsuba_mult(x, y):
	"""Implements Karatsuba multiplication
	"""
	# takes the larger of the two numbers
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y

	num = max(len(str(x)), len(str(y)))
	num_split = num / 2
	a = x / 10**(num_split)
	b = x % 10**(num_split)
	c = y / 10**(num_split)
	d = y % 10**(num_split)

	ac = karatsuba_mult(a, c)
	bd = karatsuba_mult(b, d)
	ad_plus_bc = karatsuba_mult(a+b, c+d) - ac - bd
	product = ac*10**(2*num_split) + (ad_plus_bc*10**num_split) + bd
	return product

if __name__ == "__main__":
	pairs = [[6, 3], [4, 1], [8000, 0]]
	for pair in pairs:
		product = recursive_mult(pair[0], pair[1])
		print(product)
	kar_product = karatsuba_mult(1234, 56785)
	kar_product = karatsuba_mult(3141592653589793238462643383279502884197169399375105820974944592, 
								 2718281828459045235360287471352662497757247093699959574966967627)
	print(kar_product)
		