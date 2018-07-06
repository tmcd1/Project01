# Bit flipping so I can keep track of which sets have  already been touched
def bit_flip(states, bit, state_to_set):
    states[bit] = state_to_set

# 1. Determine how many combinations are possible with the given psswrd
lowercase = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
uppercase = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
numbers = {'1','2','3','4','5','6','7','8','9','0'}
# There are 32 symbols on the average American keyboard

# State markers
HIGH = 1
LOW = 0
LOWERCASE = 0
UPPERCASE = 1
NUMBERS = 2
SYMBOLS = 3

# Bit flipping, because embedded is my life
#   -states go in this order: lowercase, uppercase, numbers, and symbols
states = [0, 0, 0, 0]

password_to_check = "This password is awesome"

for x in password_to_check:
    if (x in lowercase):
        bit_flip(states, LOWERCASE, HIGH)
    elif (x in uppercase):
        bit_flip(states, UPPERCASE, HIGH)
    elif (x in numbers):
        bit_flip(states, NUMBERS, HIGH)
    else:
        bit_flip(states, SYMBOLS, HIGH)

# Translate states into number of possible combinations
num_combinations = 0
if (states[LOWERCASE] == 1):
    num_combinations = num_combinations + 26
if (states[UPPERCASE] == 1):
    num_combinations = num_combinations + 26
if (states[NUMBERS] == 1):
    num_combinations = num_combinations + 10
if (states[SYMBOLS] == 1):
    num_combinations = num_combinations + 32

# Calculate the time needed to crack this password using brute force, assuming
#   the password is cracked after half of the combinations are tried
#   Algorithim from bit.ly/psswrdCalc
time = ((1.7 * 0.000001) * (num_combinations ** len(password_to_check))) / 2

seconds = time % 60
minutes = time / 60
hours = minutes / 60
days = hours / 24
years = days / 356

print "Time needed to crack this password:"
print "Years: {}, Days: {}, Hours: {}, Minutes: {}, Seconds: {}".format(years, days, hours, minutes, seconds)
