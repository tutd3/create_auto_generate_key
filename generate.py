from os import chmod
from Crypto.PublicKey import RSA

#create private key
key = RSA.generate(2048)
with open("/home/ubuntu/private.key", 'wb') as content_file:
    chmod("/home/ubuntu/private.key", 0600)
    content_file.write(key.exportKey('PEM'))
#create pub
pubkey = key.publickey()
with open("/home/ubuntu/public.key", 'wb') as content_file:
    content_file.write(pubkey.exportKey('OpenSSH'))
