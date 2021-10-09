import sys
from crypto_extension import CryptoExtension as ce
from extended_euclidean_algorithm import ExtendedEuclideanAlgorithm as eua
from rsa import RSA as rsa

def main():
    e = 65537
    p, q = ce.generatePairRelativelyPrimeTo(e)
    print(f'p = {p}\nq = {q}')
    n = p * q
    phi_n = ((p-1)*(q-1))
    gcd, d, k = eua.extended_gcd(e, phi_n)
    d = eua.normalize(d, phi_n) # if d < 0 then adds phi_n to it.
    sys.setrecursionlimit(2100) # just enough.
    if not ce.verifyNumsLessThanN(n, e, d):
        print(f'if m < n, ((m^e%n)^d)%n == m is not always true')
    elif gcd != 1:
        print("(p-1)*(q-1) is not relatively prime to e")
    else:
        print(f'n = {n}\nd = {d}')
        plain_message = input("Input integer to encrypt:")
        print(f'cipher_text = {rsa.encrypt(int(plain_message), e, n)}')

        cipher_text = input("Input integer to decrypt:")
        print(f'plain_message = {rsa.decrypt(int(cipher_text), d, n)}')


if __name__ == '__main__':
    main()