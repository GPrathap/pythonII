

message = input("Please Enter your message to be encrypted: ")
pin = int(input("Please Enter your PIN: "))

message_len = len(message)

reversed_message = ""
encrypted_message = ""

# reverse the message
index = message_len
while index > 0:
    reversed_message += message[index-1] # save the value of str[index-1] in reversed_message
    index =  index -1 # decrement index

#add the value of the password to the reversed message
for i in range(0, message_len):
    if(reversed_message[i].isalpha()):
        if(reversed_message[i].isupper()):
            encrypted_message += chr((ord(reversed_message[i]) - ord('A') + pin ) % 26 + ord('A'))
        else:
            encrypted_message += chr((ord(reversed_message[i]) - ord('a') + pin ) % 26 + ord('a'))
    else:
        encrypted_message += reversed_message[i]

print("Encrypted message: ", encrypted_message)
