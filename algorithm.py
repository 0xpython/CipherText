#Mappings for each letter
from dictionary import *

#Algorith for Encryption
def encrypt(input): 
  encrypted_text = ''
  for letter in input:
    letter = letter.lower()
    inum = index[letter] + shift
    if inum > 27:
      inum = inum - 27
    encrypted_letter = index[inum]
    encrypted_text = encrypted_text + encrypted_letter
  return encrypted_text

def decrypt(entext):
  decrypted_format = ''
  for letter in entext:
    letter = letter.lower()
    ilet = index[letter] - shift
    if ilet < 1:
      ilet = 27 + ilet 
    decrypt_letter = index[ilet]
    decrypted_format = decrypted_format + decrypt_letter
  return decrypted_format

shift = 5 #Use int(input('code: ')) for customizable code

user_input = input('Text for encryption: ')
encrypting = encrypt(user_input)
print(encrypting)

decrypt_input = input('Text for decryption: ')
decrypting = decrypt(decrypt_input)
print(decrypting)
