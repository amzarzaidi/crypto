from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def writeInBinfile(tosave,filename):
    with open(filename,"wb") as file:
        file.write(tosave)

def readInBinfile(filename):
    with open(filename,"rb") as file:
        result = file.read()
    return result

def encryptRSA(msg, keyFile):
    pubkey = readInBinfile(keyFile)
    rsa_key = RSA.import_key(pubkey)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    result = cipher_rsa.encrypt(msg)
    return result

def generateKeys(privateKeyFile, publicKeyFile):
    key = RSA.generate(2048)
    private_key = key.export_key()
    with open(privateKeyFile,"wb") as f:
        f.write(private_key)
    public_key = key.publickey().export_key()
    with open(publicKeyFile,"wb") as f:
        f.write(public_key)

def decryptRSA(msg, keyFile):
    prikey = readInBinfile(keyFile)
    rsa_key = RSA.import_key(prikey)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    decryp_data = cipher_rsa.decrypt(msg)
    return decryp_data

if __name__ == '__main__':
    mypubkey = "mypub.pem"
    myprikey = "mypri.pem"
    generateKeys(myprikey,mypubkey)
    

