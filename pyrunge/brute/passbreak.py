#!/usr/bin/env python3

# pip3 install pyzipper
# break passsword of an AES encrypted zip file

import pyzipper

zip_file = pyzipper.AESZipFile('secret.zip')

start_ascii=ord('a')
end_ascii=ord('z')

for i in range (start_ascii, end_ascii, 1):
    for j in range (start_ascii, end_ascii, 1):
        for k in range (start_ascii, end_ascii, 1):
            for l in range (start_ascii, end_ascii, 1):
                password_binary=bytes([i,j,k,l])
                zip_file.setpassword(password_binary)
                print('Trying ', password_binary.decode())
                try:
                    zip_file.read('secret.jpg')
                except:
                   continue
                else:
                    print("password is: ",password_binary.decode())
                    exit(0)

print("Could not find password")
exit(1)
