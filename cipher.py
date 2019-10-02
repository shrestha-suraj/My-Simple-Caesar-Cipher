def askingUser():
    message=input('Enter the message you want to encode: ')
    mykey=34190725
    key=input("Enter the 8 bit key for encryption and decryption (Example: 12345678):  ")

def encrypter(message,key):
    bit_keys=[int(x) for x in str(key)]
    message_array=[str(y) for y in str(message)]
    bit_control=8
    encoded_message=""
    for i in range(0,len(message)):
        each_key=bit_keys[i % bit_control]
        each_char=message_array[i]
        char_ascii=ord(each_char)
        if (each_key % 2 == 0):
            char_ascii+=each_key
        else:
            char_ascii-=each_key
        encoded_message+=str(chr(char_ascii))
    return encoded_message

def decrypter(code,key):
    bit_keys=[int(x) for x in str(key)]
    message_array=[str(y) for y in str(code)]
    bit_control=8
    decoded_message=""
    for i in range(0,len(code)):
        each_key=bit_keys[i % bit_control]
        each_char=message_array[i]
        char_ascii=ord(each_char)
        if (each_key % 2 != 0):
            char_ascii+=each_key
        else:
            char_ascii-=each_key
        decoded_message+=str(chr(char_ascii))
    return decoded_message

# code=encrypter(message,key)
# print("Message encryption successful.\nEncrypted Code: "+str(code))
# print("\n\nMessage decryption successful.\nDecrypted Message: "+str(decrypter(code,key)))