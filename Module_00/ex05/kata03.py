kata = "The right format"

def main():
	s = "-" * (42 - len(kata)) + kata
	print(s, end="")

if __name__ == "__main__":
	main()
