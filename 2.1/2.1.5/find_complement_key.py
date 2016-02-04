# Written by John Hansen Feb 3, 2016
from paired_keys import prime_factors, factor

def find_complement_key(pubKey):
	"""Return the matching private rsa key, given a public key"""
	mod, e = pubKey
	p, q = prime_factors(mod)
	eulers_phi = (p-1)*(q-1)
	product = eulers_phi + 1
	while (factor(product).count(e) != 1):
		product += eulers_phi
	d = int(product / e)
	return (mod, d)
