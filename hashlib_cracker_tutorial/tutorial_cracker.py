'''
Following tutorial at https://workshops.hackclub.com/passwordcracker/
'''

import hashlib #for SHA-1 hashes
from urllib.request import urlopen # open and read wordlist file via url

def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Error reading wordlist file from url, error:")
        exit()
    return  wordlistfile

def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

def bruteforce(password_list, actual_password_hash):
    for guess_password in password_list:
        if hash(guess_password) == actual_password_hash:
            print(f"Success! The password is '{guess_password}'")
            exit()

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
wordlist = readwordlist(url).decode('UTF-8')
passwordlist = wordlist.split('\n')
print(len(passwordlist))
print(type(passwordlist))

actual_password = 'Victoria'
actual_password_hash = hash(actual_password)

# Running the Brute Force attack
bruteforce(passwordlist, actual_password_hash)

print("Failed! Password not in list! Couldn't crack")