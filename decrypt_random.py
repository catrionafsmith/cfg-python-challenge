'''
Inspired by code by Weronika. For full version with Tkinter please see 
https://github.com/WeraGitHub/CFG/blob/main/Password_Cracker/main.py
'''

import random
from utils import list_chars, generate_random

def decrypt_random(password):

    test = ""
    char_list = list_chars()
    num_cycle = 0

    while test != password:
        test_chars = random.choices(char_list, k=len(password))
        test = "".join(test_chars)
        num_cycle += 1

    return "Success! The password is '{}'. {} cycles".format(password, num_cycle)

# test for decrypt_random
mystery = generate_random(4)
result = decrypt_random(mystery)
print(result)

# Test with password of length 4 took 30-45 million while loops
# around 30 sec on my machine