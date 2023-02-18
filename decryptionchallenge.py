# Assumptions:
# The length of the password is unknown
# The characters include ASCII lowercase, uppercase, digits, special characters
# We could create an array of all of the potential ASCII characters
array = [lowercase, uppercase, digits, special characters]
password = ?

# if password = "*"
for char in array:
    test = char
    if test == password:
        return "Wow awesome job you have cracked the challenge!"

# if password = "**"
for char in array:
    test = char
    for char in array:
        test += char
        if test == password:
        return "Wow awesome job you have cracked the challenge!"

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
