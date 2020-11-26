#one time pad

import random						#this library is used to create the key, as we need to have a key that is as long as the plaintext.
import string

def key_func(plain, key): 				#function to generate the key							
    key=list(key)
    if len(plain)==len(key):
        return(key)
    else:
        for i in range(len(plain)-len(key)):
            rand=string.ascii_uppercase
            key.append(random.choice(rand))
    return(''.join(key))

def encryption(plaintext, key): 			#Function that carries out the encryption process
	cipher_text = [] 
	for i in range(len(plaintext)): 
		x=(ord(plaintext[i])+ord(key[i])) % 26
		x+=ord('A')
		cipher_text.append(chr(x)) 
	return("".join(cipher_text)) 
	
def decryption(cipher_text, key): 									#function that carries out the decryption process
	orig_text = [] 
	for i in range(len(cipher_text)): 
		x = (ord(cipher_text[i])-ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x)) 
	return("" . join(orig_text)) 

#Initial values and menu

plain_text=input("Enter the plain text:")
KEY=input("Enter the key:")
key = key_func(plain_text,KEY)
print("Generated key:",key)
while (True):
    ch=0
    ch=int(input("1.Encryption \n2.Decryption \n3.Exit \nEnter your choice:"))
    if ch==1:
        cipher_text = encryption(plain_text,key)
        print("Cipher-Text :", cipher_text)
    elif ch==2:
        cipher_text=input("Enter the Cipher Text:")
        print("Plain-text:",decryption(cipher_text, key))
    else:
        exit()
