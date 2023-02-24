from utils import list_chars
from itertools import product


# num_dig is the number of digits in the password

# Smaller set of characters to test with
# char_list = list("zabike")
char_list = list_chars()


password = 'bbbbb'

# To cycle through words from 1 to 9 letters
def iter_decrypt():
    for num_dig in range(1, 9):
        for letters in product(char_list, repeat = num_dig):
            test = ''.join(letters)
            # print(test)
            if test == password:
                return (f"You solved it, it's {test}")


# To show number of cycles:   
def iter_decrypt_cycles():
    for num_dig in range(1, 9): 
        for num_cycle, letters in enumerate(product(char_list, repeat = num_dig), 1):
            test = ''.join(letters)
            # print(test, num_cycle)
            if test == password:
                return (f"You solved it, it's {test} {num_cycle}")

print(iter_decrypt())
print(iter_decrypt_cycles())