import sys

def odd_or_even(num):
	if (int(num) == 0):
		print("I\' m Zero.")
	elif (int(num) % 2 == 0):
		print("I\' m Even.")
	else:
		print("I\' m Odd.")

def main():
	if len(sys.argv) == 1:
		print("")
	elif len(sys.argv) != 2:
		print('AssertionError: more than one argument are provided')
	elif not sys.argv[1].isdigit():
		print('AssertionError: argument is not an integer')
	else:
		odd_or_even(sys.argv[1])

if __name__ == "__main__":
	main()
