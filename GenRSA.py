# import random
# from math import gcd

# # Generate uniform n-bit primes p, q


# def generate_primes(n):
#     while True:
#         p = random.randint(2**(n-1), 2**n-1)
#         if is_prime(p):
#             break
#     while True:
#         q = random.randint(2**(n-1), 2**n-1)
#         if is_prime(q):
#             break
#     return p, q

# # Check if a number is prime


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**(0.5))+1):
#         if n % i == 0:
#             return False
#     return True

# # Compute gcd(a, b)


# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     gcd_, x1, y1 = extended_gcd(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#     return gcd_, x, y

# # Generate RSA parameters


# def gen_rsa(n):
#     p, q = generate_primes(n)
#     N = p * q
#     phi_N = (p-1) * (q-1)
#     e = 3 if gcd(3, phi_N) == 1 else 216+1
#     gcd_, d, _ = extended_gcd(e, phi_N)
#     d = d % phi_N
#     return N, e, d

# # Encrypt plaintext message using public key (N, e)


# def encrypt(N, e, plaintext):
#     plaintext_bytes = plaintext.encode()
#     plaintext_int = int.from_bytes(plaintext_bytes, 'big')
#     ciphertext_int = pow(plaintext_int, e, N)
#     ciphertext_bytes = ciphertext_int.to_bytes(
#         (ciphertext_int.bit_length()+7)//8, 'big')
#     return ciphertext_bytes

# # Decrypt ciphertext message using private key d


# def decrypt(N, d, ciphertext):
#     ciphertext_int = int.from_bytes(ciphertext, 'big')
#     plaintext_int = pow(ciphertext_int, d, N)
#     plaintext_bytes = plaintext_int.to_bytes(
#         (plaintext_int.bit_length()+7)//8, 'big')
#     plaintext = plaintext_bytes.decode()
#     return plaintext

import random
from math import gcd

# Generate uniform n-bit primes p, q


def generate_primes(n):
    while True:
        p = random.randint(2**(n-1), 2**n-1)
        if is_prime(p):
            break
    while True:
        q = random.randint(2**(n-1), 2**n-1)
        if is_prime(q):
            break
    return p, q

# Check if a number is prime


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

# Compute gcd(a, b)


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    _gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return _gcd, x, y

# Generate RSA parameters


def gen_rsa(n):
    p, q = generate_primes(n)
    N = p * q
    phi_N = (p-1) * (q-1)
    e = 3 if gcd(3, phi_N) == 1 else 216+1
    _gcd, d, _ = extended_gcd(e, phi_N)
    d = d % phi_N
    return N, e, d

# Encrypt plaintext message using public key (N, e)


def encrypt(N, e, plaintext):
    plaintext_bytes = plaintext.encode()
    plaintext_int = int.from_bytes(plaintext_bytes, 'big')
    ciphertext_int = pow(plaintext_int, e, N)
    ciphertext_bytes = ciphertext_int.to_bytes(
        (ciphertext_int.bit_length()+7)//8, 'big')
    return ciphertext_bytes

# Decrypt ciphertext message using private key d


def decrypt(N, d, ciphertext):
    ciphertext_int = int.from_bytes(ciphertext, 'big')
    plaintext_int = pow(ciphertext_int, d, N)
    plaintext_bytes = plaintext_int.to_bytes(
        (plaintext_int.bit_length()+7)//8, 'big')
    # print('>>>>>', plaintext_bytes)
    plaintext = plaintext_bytes.decode('iso-8859-1')
    return plaintext


# Example usage
if __name__ == '__main__':
    # Generate RSA parameters
    N, e, d = gen_rsa(16)
    print(f'N = {N}, e = {e}, d = {d}')

    # Encrypt plaintext
    plaintext = 'Hello, world!'
    ciphertext = encrypt(N, e, plaintext)
    print(f'Ciphertext: {ciphertext.hex()}')

    # Decrypt ciphertext
    decrypted_plaintext = decrypt(N, d, ciphertext)
    print(f'Decrypted plaintext: {decrypted_plaintext}')


def test():
    N, e, d = gen_rsa(14)
    print(f'N: {N}\ne: {e}\nd: {d}')

    ciphertext = encrypt(N, e, "Sajal Shrestha")
    print(f'Ciphertext: {ciphertext}')

    plaintext = decrypt(N, d, ciphertext)
    print('plaintext-> ', plaintext)


test()


# # Define byte string
# byte_string = b'*\t6\x8f'

# # Decode byte string to plain text
# plain_text = byte_string.hex()

# # Print decoded plain text
# print(plain_text)

# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import binascii

# keyPair = RSA.generate(3072)

# pubKey = keyPair.publickey()
# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
# pubKeyPEM = pubKey.exportKey()
# print(pubKeyPEM.decode('ascii'))

# print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
# privKeyPEM = keyPair.exportKey()
# print(privKeyPEM.decode('ascii'))
