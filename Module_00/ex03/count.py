import string
import sys

def text_analyzer(text=None):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if text is None or text == "":
		text = input("What is the text to analyze?")

	if not isinstance(text, str):
		print("AssertionError: argument is not a string")
	else:
		count_char(text)

def count_char(text):
	upper = 0
	lower = 0
	punctuation = 0
	space = 0

	for char in text:
		if char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
		elif char.isspace():
			space += 1
		elif char in (string.punctuation):
			punctuation += 1

	print("The text contains {} character(s):".format(len(text)))
	print("- " + str(upper) + " upper letter(s)")
	print("- " + str(lower) + " lower letter(s)")
	print("- " + str(punctuation) + " punctuation mark(s)")
	print("- " + str(space) + " space(s)")

def main():
	if len(sys.argv) > 2:
		print('AssertionError: more than one argument are provided')
	else:
		text_analyzer(sys.argv[1])

if __name__ == "__main__":
	main()
