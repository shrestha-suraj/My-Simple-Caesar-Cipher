import cipher

file=open("test.txt","r")
writeFile=open("testCipher.txt","w")
key=input("Enter 8 digit cipher key:  ")
file=file.readlines()
cipherMessage=""

for line in file:
    encryptedMessage=cipher.encrypter(line,key)
    writeFile.write(encryptedMessage+"\n")
    cipherMessage+=(encryptedMessage+"\n")

print(cipherMessage)

#print(cipher.encrypter("Hello World",12345678))