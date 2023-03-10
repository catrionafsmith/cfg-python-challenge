# This solution uses number base conversion
# Loop through N possible solutions numbered from 0 to N
# convert N to number with base equal to the length of set of allowed characters
# this gives the indices that select allowed characters from list of base characgers
# selected characters are joined and tested against mystery password

from utils import list_chars, generate_random, change_base

# list of allowed characters
char_list = list_chars(lower=True, upper=False, numeric = True, special = False)

# number of unique allowed characters
base = len(char_list)
print(base)

def decrypt(password, length):
    '''Decrypt password of given length'''
    num_cycle = 0
    # loop over the number of possible solutions
    # convert each number to base
    for num in range(base**length):
        test_char_indices = change_base(num, base)
        test_chars = [char_list[ind] for ind in test_char_indices]
        test = "".join(test_chars)
        num_cycle += 1
        if test == password:
            return f"Success! The password is '{password}'. {num_cycle} cycles"
    

# generate random mystery password of length N
mystery = generate_random(4)
result = decrypt(mystery, len(mystery))
print(result)


# If password length not known 
# call function for a range of password lengths
# for length in range(5, 10):
#     decrypt(mystery, length)


# Test results
#Four-letter randomly generated password with 74 base characters took 12-27 M cycles of the for loop
# approx 20 seconds on my machine

#Five-letter randomly generated password with 74 base characters took >10 mins took

#Five-letter randomly generated password with 36 base characters took 35 M loop cycles 15 sec

#Six-letter password with 36 base characters expected to take 510 M cycles  ~12 mins


