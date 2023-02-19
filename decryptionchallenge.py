# Assumptions:
# The length of the password is unknown
# The characters include ASCII lowercase, uppercase, digits, special characters
# We could create an array of all of the potential ASCII characters
# Idea: have a variable within the loop that is switched to True when the password is matched, and this exits the for loop
# Idea: if password is cracked then return True, and if not then increase count by 1, 
# and the count is a measure of how many characters there are in the password, and how many nested for loops there are.
# Does it have to be a function? Or could it just be a for loop?
# Recursion!
# Could we test a possible solution both ways round to try to speed up getting to the solution? i.e. use reverse


import string
# These are the rest of the items in the array which are not included here so that the program runs more quickly
#  + string.digits + string.punctuation + string.ascii_uppercase 
array = list(string.ascii_lowercase)
# password = ?
# Make function?
crackedit = False

password="pa"
# if password = "*"
# def crackdigit(password, test=""):
#     for char in array:
#         print(test+char)
#         if test+char == password:
#             crackedit = True
#             return (f"Wow awesome job you have cracked the challenge! {test+char}")



# # for ** password
# while not crackedit:
#     for let in array:
#         print(crackdigit(password, test=let))
#         break
# print("Cracked it")

def crackdigit(password, test=""):
    for char in array:
        print(test+char)
        if test+char == password:
            return True
    



# for ** password
# while not crackedit:
for let in array:
    if crackdigit(password, test=let):
        print("Cracked it")
        break
   

# for *** password:
for let in array:
    for let in array:
        if crackdigit(password, test=let):
            print("Cracked it")
            break
        
for let in array:
    if crackdigit(password, test=let):
        print("Cracked it")
        break
    else:
        for let in array:
            crackdigit(password, test=???):

# print(array)
# print(crackdigit(password))


# if password = "**"
# for char in array:
#     test = char
#     for char in array:
#         test += char
#         if test == password:
#         return "Wow awesome job you have cracked the challenge!"

# if password = "***"
# is this logic correct? I'm not sure if it should be test on line 28?
for char in array:
    test = char
    for char in array:
        test += char
        for char in array:
            test += char   
            if test == password:
            return "Wow awesome job you have cracked the challenge!"

