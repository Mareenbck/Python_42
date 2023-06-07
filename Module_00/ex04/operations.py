import sys

def operation(a, b):
	sum = int(a) + int(b)
	diff = int(a) - int(b)
	product = int(a) * int(b)

	print("Sum: 		", sum)
	print("Difference: 	", diff)
	print("Product: 	", product)
	if (int(b) == 0):
		print("Quotient: 	ERROR (division by zero)")
		print("Remainder: 	ERROR (modulo by zero)")
	else:
		quotient = int(a) / int(b)
		remainder = int(a) % int(b)
		print("Quotient: 	", quotient)
		print("Remainder: 	", remainder)


def main():
	if len(sys.argv) > 3:
		print('AssertionError: too many arguments')
	elif len(sys.argv) == 1:
		print('Usage: python operations.py <number1> <number2> \nExample: \npython operations.py 10 3')
	elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
		print('AssertionError: only integers')
	else:
		operation(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
	main()

