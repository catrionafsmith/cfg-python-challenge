array = ["a", "b", "c"]
password = "cba"

# for char in array:
#     if char == password:
#         print(f"yes! password is {password}")
#         break
#     else:
#         for let in array:
#             if char + let == password:
#                 print(f"Yes Yes password is {password}")
#                 break
#             else:
#                 for test in array:
#                     print(char+let+test)
#                     if char + let + test == password:
#                         print(f"Yes Yes Yes password is {password}")
#                         break
                  
    
# Works for passwords with two digits, but not those with three.

global count 
count = -1
def checkdigit(password, test=""):
    global count
    for char in array:
        print(test+char)
        if test+char == password:
            print(f"Yes Yes password is {test+char}")
            return 
    count +=1
    print(count)
    nextchar = array[count]
    print(f"nextchar is {nextchar}")
    print(f"char is {char}")
    checkdigit(password, test=nextchar)

# for char in array:
#     if char == password:
#         print(f"yes! password is {char}")
#         break
#     else:
#         checkdigit(char, password)

checkdigit(password)