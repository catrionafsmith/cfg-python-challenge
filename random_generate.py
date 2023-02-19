import random
from list_chars import list_chars

def generate_random(length):
    '''
    Function takes length of password to generate and 
    returns randomly generated password of that length
    '''
    char_list = list_chars()
    password_chars = random.choices(char_list, k=length)
    password = "".join(password_chars)
    return password

# print(generate_random(7))

