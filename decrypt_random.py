'''
Inspired by code from https://github.com/WeraGitHub/CFG/blob/main/Password_Cracker/main.py
'''

import random
from utils import list_chars

def decrypt_random(password):

    test = ""
    char_list = list_chars()
    num_cycle = 0

    while test != password:
        test_chars = random.choices(char_list, k=len(password))
        test = "".join(test_chars)
        num_cycle += 1

    print("Success! The password is '{}'. {} cycles".format(password, num_cycle))

# test for decrypt_random
# mystery = '*!aA'
# decrypt_random(mystery)


# Test with password of length 4 took 30-45 million while loops
# around 30 sec on my machine