from list_chars import list_chars #function returns list of allowed characters

# Decrypt one letter password
def decrypt1(password):
    num_cycle = 0
    test = ""
    for char in list_chars():
        test = char
        num_cycle += 1 
        if test == password:
            print(f"Success! The password is '{password}'. {num_cycle} cycles")

mystery = r"%"
decrypt1(mystery)

# Decrypt two letter password
def decrypt2(password):
    num_cycle = 0
    for char1 in list_chars():
        test_chars = [char1]
        num_cycle += 1 
        for char2 in list_chars():
            num_cycle += 1
            test_chars.append(char2)
            test = "".join(test_chars)
            if test == password:
                print(f"Success! The password is '{password}'. {num_cycle} cycles")

mystery = r"%a"
decrypt2(mystery)