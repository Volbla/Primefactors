import numpy as np
from math import sqrt, ceil

from numpy.typing import NDArray


def gen_primes(max_value: int|float) -> NDArray[np.int_]:
	"""Find all prime numbers <= max_value."""

	if max_value < 2:
		return np.array([])

	odd_indices = np.ones(ceil(max_value / 2), dtype=bool)
	sqrt_index = round(sqrt(max_value) / 2) + 1

	for n, x in enumerate(odd_indices[1:sqrt_index], 1):
		if x:
			p = 2*n + 1
			odd_indices[n+p*n::p] = False

	primelist = np.flatnonzero(odd_indices) * 2 + 1

	primelist[0] = 2

	return primelist


cached_primes = np.array([2], dtype=int)

def list_primes(x: float) -> NDArray[np.int_]:
	global cached_primes

	if cached_primes[-1] >= x:
		top = np.searchsorted(cached_primes, x)
		return cached_primes[:top+1]

	else:
		cached_primes = gen_primes(x)
		return cached_primes


def find_prime_factors(number: int) -> list[int]:
	if number == 0:
		return []

	number = abs(number)
	useful_primes = list_primes(sqrt(number))
	factors = []

	for p in useful_primes:
		while number % p == 0:
			factors.append(p)
			number //= p

	if number > 1:
		factors.append(number)

	return factors
