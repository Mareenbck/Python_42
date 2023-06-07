kata = (2019, 9, 25, 3, 30)

def main():
	date = "{:02d}/{:02d}/{}".format(kata[1], kata[2], kata[0])
	heure = "{:02d}:{:02d}".format(kata[3], kata[4])
	print("{} {}".format(date, heure))

if __name__ == "__main__":
	main()
