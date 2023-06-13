from random import randint
import sys

def guess_num(target):
	count = 1
	answer = 0
	while (answer != target):
		try:
			answer = int(input("What's your guess between 1 and 99?\n"))
		except ValueError:
			if answer == 'exit':
				sys.exit()
			else:
				print("That's not a number.")
		else:
			if answer > target:
				print("Too High !")
				count += 1
			elif answer < target:
				print("Too Low")
				count += 1
			else:
				if target == 42:
					print("The answer to the ultimate question of life, the universe and everything is 42.")
				else:
					print("Congratulations, you've got it!")
	return count


def main():
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.")
	print("Good luck!")
	target = randint(1, 99)
	result = guess_num(target)
	if result > 1:
		print("You won in {} attempts!".format(result))
	elif result == 1:
		print("Congratulations! You got it on your first try!")
	else:
		print("Goodbye!")

if __name__ == "__main__":
	main()
