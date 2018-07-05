# Convert the string into letters
def string_to_letters(the_string, letters):
    "Takes in a string, and assigns each letter a number between 0 and 25"
    list_of_numbers = []
    index = 0
    for x in the_string:
        for index in range(0,26):
            if (x == letters[index]):        # If the character matches the letter at the current index,
                list_of_numbers.append(index) # add the index (0 < index < 26) to list of numbers
                break
            index = index + 1
    return list_of_numbers

# Convert the key to a series of numbers
def string_key_to_number_key(string_key, letters):
    "Takes in the key string and converts it into a list of numbers"
    key = []  # No we can check for null list
    index = 0
    for char in string_key:
        for index in range(0, 26):
            if(char == letters[index]):
                key.append(index + 1)
                break
    return key 

# Encrypt the message
#     -This subroutine will also be used to decrypt messages, hense the third input
def scramble(key, message, encrypt):
    x = 0
    new_message = []
    if(encrypt):
        for x in range(0, len(message)):
            new_message.append(((message[x] + key[x % len(key)]) % 25))
    else:
        for x in range(0, len(message)):
            new_message.append(((message[x] - key[x % len(key)]) % 25))

    return new_message

# Convert the cipher text back into a "readable" message
def letterize(message_in_numbers, letters):
    "Turns the list of numbers into readable characters from the alphabet"
    new_message = []
    for x in message_in_numbers:
        new_message.append(letters[x])
    return new_message

if __name__ == "__main__":
    # As close to "constants" as we can get in python
    ENCRYPT = 1
    DECRYPT = 0

    # List of all the letters
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Hardcoded message and key
    message = "hello"
    key = "cat"

    # Convert message and key to something usuable by the program
    message_numbers = string_to_letters(message.lower(), letters)
    key_numbers = string_key_to_number_key(key, letters)

    # Encrypt
    encrypted_message = scramble(key_numbers, message_numbers, ENCRYPT)

    print "Message numbers: ", message_numbers
    print "Key numbers: ", key_numbers
    print "Message: ", message
    print "Key: ", key

    print "\n"
    print letterize(encrypted_message, letters)


