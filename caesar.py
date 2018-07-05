def string_to_letters(the_string, letters):
	"Takes in a string, and assigns each letter a number between 0 and 25"
	list_of_numbers = []
	index = 0;
	for x in the_string:
		for index in range(0, 26):
			if (x == letters[index]):
				list_of_numbers.append(index)
			index = index + 1
	return list_of_numbers 

def numberize(letters, character): 
	"Takes in a letter and maps it to a value between 1 and 26"
	key = -1
	index = 0
	for index in range(0,26):
		if (character == letters[index]):
			key = index
	return key + 1

def scramble(key, plaintext, encrypt):
	"Encrypts is encrypt==1, else decrypts"
	x = 0 
	new_text = []
	if(encrypt):
		for x in range(0, len(plaintext)):
			new_text.append(((plaintext[x] + key) % 25))
	else:
		for x in range(0, len(plaintext)):
			new_text.append(((plaintext[x] - key) % 25)) 
			
	return new_text

def letterize(numbers, letters):
	"Turns the list of numbers into readable characters from the alphabet"
	new_message = []
	for x in numbers:
		new_message.append(letters[x])
	return new_message

ENCRYPT = 1;
DECRYPT = 0;

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cipher = "o"
key = numberize(letters, 'a')

numbers = string_to_letters(cipher.lower(), letters)
encrypted_numbers = scramble(key, numbers, ENCRYPT)
decrypted_numbers = scramble(key, encrypted_numbers, DECRYPT)

print letterize(numbers, letters)
print letterize(encrypted_numbers, letters)
print letterize(decrypted_numbers, letters)
	
