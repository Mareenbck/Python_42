kata = (19,42,21)


def main():
	s = ''.join(str(kata))
	s = "The 3 numbers are: " + s[1:-1]
	print(s)


if __name__ == "__main__":
	main()
