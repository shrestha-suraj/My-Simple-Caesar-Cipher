message=input('Enter the message you want to encode: ')
key=34190725
print("This is the message: "+message)

def encrypter(message,key):
    bit_keys=[int(x) for x in str(key)]
    message_array=[str(y) for y in str(message)]
    bit_control=8
    encoded_message=""
    for i in range(0,len(message)):
        each_key=bit_keys[i % bit_control]
        each_char=message_array[i]
        char_ascii=ord(each_char)
        print (chr(char_ascii+each_key))


    print ("End of encryption.")


encrypter(message,key)