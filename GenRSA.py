import random
import math
import argparse


def is_prime(n, k=5):
    """Test if a number is prime using the Miller-Rabin test."""
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Write n-1 as 2^r*d by factoring powers of 2 from n-1
    r = 0
    d = n-1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test for k rounds
    for i in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for j in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True


def random_prime(bit_length):
    """Generate a random prime number of the given bit length."""
    p = random.getrandbits(bit_length)
    # Set two most significant bits to 1 to ensure p is odd
    p |= (1 << bit_length - 1) | 1
    while not is_prime(p):
        p = random.getrandbits(bit_length)
        p |= (1 << bit_length - 1) | 1
    return p


def mod_inverse(a, n):
    t, new_t = 0, 1
    r, new_r = n, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        return None   # a is not invertible modulo n
    if t < 0:
        t += n

    return t


def GenRSA(bit_length):
    # Generate two random primes with half the bit length
    p = random_prime(bit_length//2)
    q = random_prime(bit_length//2)
    # Compute N as the product of the two primes
    N = p*q
    # Compute the totient of N
    phiN = (p-1)*(q-1)
    # Choose a random prime e that is relatively prime to phiN
    e = random_prime(bit_length//4)
    while math.gcd(e, phiN) != 1:
        e = random_prime(bit_length//4)
    # Compute the modular inverse of e modulo phiN
    d = mod_inverse(e, phiN)
    return (N, e, d)


def encrypt(plaintext, N, e):
    # Convert the plaintext to an integer using big-endian byte ordering
    m = int.from_bytes(plaintext.encode(), 'big')
    # Compute the ciphertext by raising m to the power of e modulo N
    c = pow(m, e, N)
    return c


def decrypt(ciphertext, N, d):
    # Compute the plaintext by raising the ciphertext to the power of d modulo N
    m = pow(ciphertext, d, N)
    # Convert the plaintext integer to a byte string using big-endian byte ordering
    plaintext = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
    return plaintext


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Pseudo one-time pad encryption/decryption')
    parser.add_argument('-gen', type=int, help='')
    parser.add_argument('-enc', nargs=3, help='')
    parser.add_argument('-dec', nargs=3, help='')
    args = parser.parse_args()

    if args.gen:
        N, e, d = GenRSA(args.gen)
        print('N: ', N, 'e: ', e, 'd: ', d)
    elif args.enc:
        plaintext = args.enc[0]
        N = args.enc[1]
        e = args.enc[2]
        ciphertext = encrypt(plaintext, int(N), int(e))
        print('ciphertext: ', ciphertext)
    elif args.dec:
        ciphertext = args.dec[0]
        N = args.dec[1]
        d = args.dec[2]
        plaintext = decrypt(int(ciphertext), int(N), int(d))
        print('plaintext: ', plaintext)
    else:
        parser.print_help()

# # Example usage
# bit_length = 1024
# N, e, d = GenRSA(bit_length)
# plaintext = "Hello, world!"
# ciphertext = encrypt(plaintext, N, e)
# decrypted = decrypt(ciphertext, N, d)
# print(f"Plaintext: {plaintext}")
# print(f"Ciphertext: {ciphertext}")
# print(f"Decrypted: {decrypted}")
