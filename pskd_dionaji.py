import Cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) 
publickey = key.publickey() 

p = open('plaintext.txt', 'r')
pesan = p.read()

msg = bytes(pesan, 'utf-8')
encryptor = PKCS1_OAEP.new(publickey)
encrypted = encryptor.encrypt(msg)

print ('encrypted =', encrypted)
f = open ('encryption.txt', 'w')
f.write(str(encrypted)) 
f.close()

f = open ('encryption.txt', 'r')
msg2 = f.read()

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(msg2)))

print ('decrypted = ', decrypted.decode('utf-8'))

f = open ('encryption.txt', 'w')
f.write(str(msg2))
f.write(str(decrypted))
f.close()