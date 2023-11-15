def subs_caesar1():
    s = '''
def encrypt_text(plaintext,n):
	ans = ""
	ans1 = ""
# iterate over the given text
	for i in range(len(plaintext)):
		ch = plaintext[i]
# check if space is there then simply add space
		if ch==" ":
			ans+=" "
			ans1+=" "
# check if a character is uppercase then encrypt it accordingly
		elif (ch.isupper()):
			ans += chr((ord(ch) + n-65) % 26 + 65)
			ans1 += chr((ord(ch) + ROT13-65) % 26 + 65)
# check if a character is lowercase then encrypt it accordingly
		else:
			ans += chr((ord(ch) + n-97) % 26 + 97)
			ans1 += chr((ord(ch) + ROT13-97) % 26 + 97)
	return ans
plaintext = "HELLO EVERYONE"
n = 3
ROT13 = 13
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is(Caesar Cipher): " + encrypt_text(plaintext,n))
print("Cipher Text is(ROT-13) : " + encrypt_text(plaintext,ROT13))'''
    return s

def subs_poly2():
    s = '''
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
def encryption(string, key):
	encrypt_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +ord(key[i])) % 26
		x += ord('A')
		encrypt_text.append(chr(x))
	return("" . join(encrypt_text))

def decryption(encrypt_text, key):
	orig_text = []
	for i in range(len(encrypt_text)):
		x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return(""
. join(orig_text))
if __name__ == "__main__":
	string = input("Enter the message: ")
	keyword = input("Enter the keyword: ")
	key = generateKey(string, keyword)
	encrypt_text = encryption(string,key)
	print("Encrypted message:", encrypt_text)
	print("Decrypted message:", decryption(encrypt_text, key))
#Input:
# Enter the message:  Welcome to srm
# Enter the keyword:  hello
# Encrypted message: JUIZOFUKQOGIOJ
# Decrypted message: WKRIUSKTZUTYXS'''
    return s

def des4():
	s = '''
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Define the plaintext and the 8-byte key
plaintext = b"LOOK AROUND"
key = get_random_bytes(8)

# Create a DES cipher object for encryption
cipher = DES.new(key, DES.MODE_ECB)

# Pad the plaintext to be a multiple of 8 bytes (DES block size)
padding_length = 8 - len(plaintext) % 8
plaintext += bytes([padding_length]) * padding_length

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decipher = DES.new(key, DES.MODE_ECB)
decrypted_text = decipher.decrypt(ciphertext)

# Remove the padding
padding_length = decrypted_text[-1]
decrypted_text = decrypted_text[:-padding_length]

print("Plaintext:", plaintext.decode("utf-8"))
print("Key:", key.hex())
print("Ciphertext:", ciphertext.hex())'''
	return s

def blow5():
    s = '''
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

# Function to pad the plaintext to a multiple of block size bytes
def pad_text(text, block_size):
    padding_length = block_size - (len(text) % block_size)
    padding = bytes([padding_length] * padding_length)
    return text + padding

# Function to unpad the text
def unpad_text(text):
    padding_length = text[-1]
    return text[:-padding_length]

# Define the plaintext and the key
plaintext = b"Hey there!"
key = get_random_bytes(16)  # 16 bytes key (128 bits)

# Create a Blowfish cipher object for encryption
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Pad the plaintext to be a multiple of the block size
plaintext = pad_text(plaintext, Blowfish.block_size)

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decipher = Blowfish.new(key, Blowfish.MODE_ECB)
decrypted_text = decipher.decrypt(ciphertext)

# Remove the padding
decrypted_text = unpad_text(decrypted_text)

print("Plaintext:", plaintext.decode("utf-8"))
print("Key:", key.hex())
print("Ciphertext:", ciphertext.hex())
print("Decrypted text:", decrypted_text.decode("utf-8"))
'''
	return s

def rijn6():
     s = '''
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define functions for padding and unpadding data
def pad_data(data):
    block_size = AES.block_size
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding

def unpad_data(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Generate a random 256-bit (32-byte) AES key
key = get_random_bytes(32)

# Create an AES cipher object for encryption
cipher = AES.new(key, AES.MODE_CBC)
iv = cipher.iv  # Save the IV for later use during decryption

# Define the plaintext
plaintext = b"Yellow is a nice color."

# Pad the plaintext to be a multiple of the AES block size
plaintext = pad_data(plaintext)

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decipher = AES.new(key, AES.MODE_CBC, iv=iv)
decrypted_text = decipher.decrypt(ciphertext)

# Remove the padding
decrypted_text = unpad_data(decrypted_text)

print("Plaintext:", plaintext.decode("utf-8"))
print("Key:", key.hex())
print("Ciphertext:", ciphertext.hex())
print("Decrypted text:", decrypted_text.decode("utf-8"))'''
	return s

def diffie7():
     s = '''
import random

# Publicly agreed upon prime number (p) and primitive root (g)
p = 10
g = 6

# Alice generates her private key (a)
a = random.randint(1, p - 1)

# Bob generates his private key (b)
b = random.randint(1, p - 1)

# Function to compute modular exponentiation (g^x mod p)
def mod_exp(g, x, p):
    return (g ** x) % p

# Alice computes her public key (A)
A = mod_exp(g, a, p)

# Bob computes his public key (B)
B = mod_exp(g, b, p)

# Alice and Bob exchange public keys

# Alice computes the shared secret key
shared_secret_A = mod_exp(B, a, p)

# Bob computes the shared secret key
shared_secret_B = mod_exp(A, b, p)

# Both Alice and Bob now have the same shared secret key
print("Monsij shared secret:", shared_secret_A)
print("Deb shared secret:", shared_secret_B)
'''
	return s

def rsa8():
    s = '''
import random
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    return ((n, e), (n, d))

def encrypt(public_key, plaintext):
    n, e = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    n, d = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

if __name__ == "__main__":
    bits = int(input("Enter the number of bits for the key size: "))
    public_key, private_key = generate_keypair(bits)
    message = input("Enter the message to encrypt: ")
    encrypted_message = encrypt(public_key, message)
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Original message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)
'''
	return s

def digital9():
    s = '''
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Step 1: Key Generation
key_pair = DSA.generate(2048)  # Generate key pair
public_key = key_pair.publickey().export_key()
private_key = key_pair.export_key()

# Step 2: Signing
message = input("Enter the message to be signed: ").encode()  # Message to be signed
hash_object = SHA256.new(message)  # Create a hash of the message
signer = DSS.new(key_pair, 'fips-186-3')  # Create a digital signature
signature = signer.sign(hash_object)

# Step 3: Verification
hash_object = SHA256.new(message)  # Hash the original message again
verifier = DSS.new(key_pair.publickey(), 'fips-186-3')  # Create a verifier
try:
    verifier.verify(hash_object, signature)  # Verify the signature
    print("Signature is valid.")
except ValueError:
    print("Signature is invalid.")

# Output public and private keys (for demonstration purposes)
print("\nPublic Key:")
print(public_key.decode())
print("\nPrivate Key:")
print(private_key.decode())
'''
	return s

def transport3():
    s = '''
#include<iostream>
#include<string.h>
using namespace std;

void encryptMsg(char msg[], int key){
    int msgLen = strlen(msg), i, j, k = -1, row = 0, col = 0;
    char railMatrix[key][msgLen];
    
    for(i = 0; i < key; ++i)
        for(j = 0; j < msgLen; ++j)
            railMatrix[i][j] = '\n';
    
    for(i = 0; i < msgLen; ++i){
        railMatrix[row][col++] = msg[i];
        if(row == 0 || row == key-1)
            k= k * (-1);
        row = row + k;
    }
    
    cout<<"\nEncrypted Message: ";
    
    for(i = 0; i < key; ++i)
        for(j = 0; j < msgLen; ++j)
            if(railMatrix[i][j] != '\n')
                cout<<railMatrix[i][j];
}

void decryptMsg(char enMsg[], int key){
    int msgLen = strlen(enMsg), i, j, k = -1, row = 0, col = 0, m = 0;
    char railMatrix[key][msgLen];
    
    for(i = 0; i < key; ++i)
        for(j = 0; j < msgLen; ++j)
            railMatrix[i][j] = '\n';
    
    for(i = 0; i < msgLen; ++i){
        railMatrix[row][col++] = '*';
        if(row == 0 || row == key-1)
            k= k * (-1);
        row = row + k;
    }
    
    for(i = 0; i < key; ++i)
        for(j = 0; j < msgLen; ++j)
            if(railMatrix[i][j] == '*')
                railMatrix[i][j] = enMsg[m++];
    
    row = col = 0;
    k = -1;
    
    cout<<"\nDecrypted Message: ";
    
    for(i = 0; i < msgLen; ++i){
        cout<<railMatrix[row][col++];
        if(row == 0 || row == key-1)
            k= k * (-1);
        row = row + k;
    }
}

int main(){
    char msg[] = "Hello World";
    char enMsg[] = "Horel ollWd";
    int key = 3;
    
    cout<<"Original Message: "<<msg;
    encryptMsg(msg, key);
    decryptMsg(enMsg, key);
    
    return 0;
}
'''
	return s

