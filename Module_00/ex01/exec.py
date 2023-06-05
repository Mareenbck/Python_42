import sys

def reverse_slicing(s):
    return s[::-1]

def swap_case(s):
	return s.swapcase()

def main():
	if len(sys.argv) > 1:
		joined_s = ' '.join(sys.argv[1:])
		rev_s = reverse_slicing(joined_s)
		result = swap_case(rev_s)
		print(result)
	else:
		print('')

if __name__ == "__main__":
	main()
