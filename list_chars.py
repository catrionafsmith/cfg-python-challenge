def list_chars():
    '''
    Returns list of allowed characters 
    '''

    letters= "abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    special_chars ="!@£$%^&*()_+"

    all_chars = letters + letters.upper() + numbers + special_chars
    
    return [char for char in all_chars] 

# print(list_chars())