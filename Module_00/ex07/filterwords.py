import sys

def filterwords(words, count):
	splitted = words.split(" ")
	result = []
	for word in splitted:
		word_without_punctuation = ''.join(char for char in word if char.isalpha())
		if len(word) > int(count):
			result.append(word_without_punctuation)
	print(result)


def main():
	if len(sys.argv) != 3:
		print("ERROR")
	elif not isinstance(sys.argv[1], str) or not sys.argv[2].isdigit():
		print("ERROR")
	else:
		filterwords(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
	main()
