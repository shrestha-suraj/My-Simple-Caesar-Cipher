message=input('Enter the message you want to encode: ')
key=34190725
print("This is the message: "+message)

def encrypter(message,key):
    bit_keys=[int(x) for x in str(key)]
    print("Log Bit_Keys: " + str(bit_keys))
    message_array=[str(y) for y in str(message)]
    print("Log Message_Array: " + str(message_array))
    bit_control=8
    encoded_message=""
    for i in range(0,len(message)):
        each_key=bit_keys[i % bit_control]
        print("Log Each_Key: "+str(each_key))
        each_char=message_array[i]
        print("Log Each_Char: "+str(each_char))
        char_ascii=ord(each_char)
        print("Log char_ascii: "+str(char_ascii))
        if (each_key % 2 == 0):
            char_ascii+=each_key
        else:
            char_ascii-=each_key
        encoded_message+=str(chr(char_ascii))


    print (encoded_message)


encrypter(message,key)