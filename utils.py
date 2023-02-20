'''
Helper functions to:
- create a list of allowed characters, 
- generate random passwords, 
- change base.
'''

import random

def list_chars(lower=True, upper=False, numeric = True, special = False):
    '''
    Returns list of allowed characters 
    '''
    letters= "abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    special_chars ="!@£$%^&*()_+"
    all_chars=""
    if lower:
        all_chars += letters
    if upper:
        all_chars += letters.upper()
    if numeric:
        all_chars += numbers
    if special:
        all_chars += special_chars
   
    return [char for char in all_chars] 

# test for list_chars
# print(list_chars())

def generate_random(length):
    '''
    Function takes length of password to generate and 
    returns randomly generated password of that length
    '''
    char_list = list_chars()
    password_chars = random.choices(char_list, k=length)
    password = "".join(password_chars)
    return password

# test for generate_random
# print(generate_random(7))

def change_base(dec, base):
    '''Convert decimal number to a number with new base stored as a list'''
    
    q, r = divmod(dec, base) #quotient and remainder
    result = [r]
    while q > 0:
        q, r = divmod(q, base)
        result.insert(0,r)
    return result

# print(change_base(409,20))