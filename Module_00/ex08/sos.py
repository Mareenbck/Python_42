import sys

morse = {'A': '.-', 'B': '-...',
				'C': '-.-.', 'D': '-..', 'E': '.',
				'F': '..-.', 'G': '--.', 'H': '....',
				'I': '..', 'J': '.---', 'K': '-.-',
				'L': '.-..', 'M': '--', 'N': '-.',
				'O': '---', 'P': '.--.', 'Q': '--.-',
				'R': '.-.', 'S': '...', 'T': '-',
				'U': '..-', 'V': '...-', 'W': '.--',
				'X': '-..-', 'Y': '-.--', 'Z': '--..',
				'1': '.----', '2': '..---', '3': '...--',
				'4': '....-', '5': '.....', '6': '-....',
				'7': '--...', '8': '---..', '9': '----.',
				'0': '-----', ' ': '/'}

def morse_code(str):
	str = ' '.join(str)
	result = ""
	for char in str:
		if char.upper() in morse.keys():
			result += ''.join(morse[char.upper()] + ' ')
		else:
			return "ERROR"
	return result


def main():
	if len(sys.argv) == 1:
		sys.exit()
	else:
		print(morse_code(sys.argv[1::]))

if __name__ == "__main__":
	main()
