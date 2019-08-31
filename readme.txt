Author: Suraj Shrestha
Email: sshrest4@go.olemiss.edu
Date: 8/31/2019

Project Description: This is a simple algorithm that I developed for
the message encoding and decoding using a 8 bit key. The key used here
should be numbers and can only have 8 digits. For example: 12345678.

The way the code works is very simple.The program prompts user to put in
their message and ask for the eight digit key. After the key is entered
the program generates the encrypted message and also decrypts it for you.
Basically, there are two functions in the pogram that executes these actions.
The first function is encrypter which takes 2 parameters i.e. the message and
the key and it returns the encrypted code. The decrypter does exact opposite.

My Caesar Cipher Algorithm with example:
Message (M): cryptography
Key     (K): 34190725
Process: Odd digits decrease the ascii of the corresponding message
            while even number increases the ascii of corresponding
            message and the Cipher is done.
Encrypted Message: `vxgthim^tgp

How?

c = ASCII(c) = 99
Corresponding key = 3 which is odd so subtraction
99-3 = 96 = CharacterofASCII(96) = `

r = ASCII(r) = 114
Corresponding key = 4 which is even so addition
114+4 = 118 = CharacterofASCII(118) = v

y = ASCII(y) = 121
Corresponding key = 1 which is odd so subtraction
121-1 = 120 = CharacterofASCII(120) = x

p = ASCII(p) = 112
Corresponding key = 9 which is odd so subtraction
112-9 = 103 = CharacterofASCII(103) = g

t = ASCII(t) = 116
Corresponding key = 0 which is considered even so subtraction
116-0 = 116 = CharacterofASCII(116) = t

o = ASCII(o) = 111
Corresponding key = 7 which is odd so subtraction
111-7 = 104 = CharacterofASCII(104) = h

And so on....