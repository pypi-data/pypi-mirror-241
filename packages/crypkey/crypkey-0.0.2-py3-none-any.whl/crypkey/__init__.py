def enc_txt():
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