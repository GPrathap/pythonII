

message = input("Please Enter your message to be encrypted:")
password = input("Please Enter your password:")

message_len = len(message)
password_len = len(password)

reversed_message = []
encrypted_message = []

# reverse the message
index = message_len
while index > 0:
    reversed_message += message[index-1] # save the value of str[index-1] in reversed_message
    index =  index -1 # decrement index

#add the value of the password to the reversed message
j = 0
for i in range(0, message_len):
    if(isalpha(reversed_message[i])):
        encrypted_message[i] = chr(ord(reversed_message[i]) + ord(password[j]) - ord('a'))
    j = j + 1
    if (j == password_len):
        j = 0
