from rsa import readInBinfile, decryptRSA

privatekey = "mypri.pem"

message = readInBinfile("msgChiffreBob01451999.txt")

print(decryptRSA(message,privatekey))