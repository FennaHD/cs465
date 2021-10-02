import sys
from diffie_hellman import DiffieHellman


def diffie_hellman():
	sys.setrecursionlimit(1500)  # without this we hit the recursion limit and the program will crash.

	# Our generator is a small prime number.
	g = 5

	# a is my private number, p is the modulus. Both are prime and safe numbers.
	a = 3146379777777208857005361989263160327223798537006033455418977468819610921971499216680252867837701558403931074311879622506931858018266498938283054092503
	p = 2800972037945227323036254567247126975343590460514771387955221860840553381995016860687656730719464687986068436800524247768776936091505949418487214508443

	# result of dh.mod_exp(g, b, p) given from the auto-grader.
	gbmodp = 48241275436078217975677393297903544392707338354982512747000844568294320440070835805688925816523819522315786502878742458262170108378486996886681050696

	# result of dh.mod_exp(g, a, p).
	gamodp = 1164418143749027163672915858643611854570097127780466646252921426029568757472442291134886424391874900736398024843915621786221191894969812732815093258791

	# this is the same result if we were to compute mod_exp(gamodp, b, p) with the b we don't know.
	print(f'mod_exp = {DiffieHellman().mod_exp(gbmodp, a, p)}')


if __name__ == '__main__':
	diffie_hellman()