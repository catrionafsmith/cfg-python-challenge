letters= "abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
special_chars ="!@£$%^&*()_+"
all_chars = letters + letters.upper() + numbers + special_chars

# list of allowed characters
array = [char for char in all_chars] 
# print(array)

def decrypt1(password):
    # length 1
    num_cycle = 0
    test = ""
    for char in array:
        test = char
        num_cycle += 1 
        if test == password:
            print(f"Success! The password is '{password}'. {num_cycle} cycles")

mystery = r"%"
decrypt1(mystery)

# Decrypt two letter password
def decrypt2(password):
    num_cycle = 0
    for char1 in array:
        test_chars = [char1]
        num_cycle += 1 
        for char2 in array:
            num_cycle += 1
            test_chars.append(char2)
            test = "".join(test_chars)
            if test == password:
                print(f"Success! The password is '{password}'. {num_cycle} cycles")

mystery = r"%a"
decrypt2(mystery)

# # if password = "***"
# # is this logic correct? I'm not sure if it should be test on line 28?
# for char in array:
#     test = char
#     for char in array:
#         test += char
#         for char in array:
#             test += char   
#             if test == password:
#             return "Wow awesome job you have cracked the challenge!"
