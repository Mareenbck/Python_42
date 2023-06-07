kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

def main():
	for author in kata:
		print("{} was created by {}".format(author, kata[author]))


if __name__ == "__main__":
	main()

