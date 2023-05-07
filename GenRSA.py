import random

# Compute the greatest common divisor of two numbers using Euclid's algorithm


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Check if a number is prime


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random prime number of the given bit size


def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

# Generate RSA key pairs of the given bit size


def generate_keys(key_size):
    # Generate two large prime numbers
    p = generate_prime(key_size // 2)
    q = generate_prime(key_size // 2)

    # Calculate n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find a number e such that gcd(e, phi(n)) == 1
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break

    # Calculate the modular inverse of e
    d = pow(e, -1, phi)

    return (n, e), (n, d)

# Encrypt a plaintext string using RSA


def encrypt(plaintext, public_key):
    n, e = public_key
    ciphertext = [pow(ord(c), e, n) for c in plaintext]
    return ciphertext

# Decrypt a ciphertext list using RSA


def decrypt(ciphertext, private_key):
    n, d = private_key
    plaintext = ''.join([chr(pow(c, d, n)) for c in ciphertext])
    return plaintext


# Example usage:
public_key, private_key = generate_keys(100)
print("Public key:", public_key)
print("Private key:", private_key)

plaintext = "Sajal Shrestha"
ciphertext = encrypt(plaintext, public_key)
print("Ciphertext:", ciphertext)

decrypted_plaintext = decrypt(ciphertext, private_key)
print("Decrypted plaintext:", decrypted_plaintext)
