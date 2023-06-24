from primefunctions import find_prime_factors
import re


def take_input():
	print("Enter a number or numbers separated by commas to get their prime factors.")

	multiplication_dot = "∙"
	superdigits = "⁰¹²³⁴⁵⁶⁷⁸⁹"

	# Convert a multi-digit number to superscript
	def super_each_digit(n: int) -> str:
		supers_list = [superdigits[int(digit)] for digit in str(n)]
		return "".join(supers_list)

	def stringify(primes: list[int], powers: list[int]) -> str:
		powers_strings = [
			super_each_digit(x) if x > 1
			else ""
			for x in powers
		]
		powered_factors = [str(prime) + pwr for prime, pwr in zip(primes, powers_strings)]

		return multiplication_dot.join(powered_factors)


	while True:
		entered_string = input("\nNumbers: ")
		if entered_string.lower() in ("", "exit", "quit"):
			print("Exiting")
			return

		try:
			numberstrings = re.split(r"[, ]+", entered_string)
			values = [int(x) for x in numberstrings]
		except ValueError:
			print("Error: Inputs must be whole numbers")
			continue

		width = max(len(x) for x in numberstrings) + 1

		for num_string, value in zip(numberstrings, values):
			primes = find_prime_factors(value)
			unique_primes, counts = unique(primes)

			factor_string = stringify(unique_primes, counts)
			sign = "-" if value < 0 else ""
			print(num_string.rjust(width) + " = " + sign + factor_string)


def unique(numbers: list[int]) -> tuple[list[int], list[int]]:
	"""Vanilla implementation of numpy.unique.

	Presumes the input is sorted.
	"""

	if len(numbers) == 0:
		return [], []

	values = [numbers[0]]
	counts = [1]

	for n in numbers[1:]:
		if n == values[-1]:
			counts[-1] += 1

		else:
			values.append(n)
			counts.append(1)

	return values, counts


if __name__ == "__main__":
	take_input()
