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
        all_chars += special
   
    return [char for char in all_chars] 

# print(list_chars())