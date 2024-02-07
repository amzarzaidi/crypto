from rsa import writeInBinfile
from rsa import encryptRSA

text = input("Données :").encode("utf-8")

keyfile = "publicBob.pem"

encrypted_data = encryptRSA(text,keyfile)

writeInBinfile(encrypted_data,"file.bin")