def change_base(dec, base):
    '''Convert decimal number to a number with new base stored as a list'''
    
    q, r = divmod(dec, base) #quotient and remainder
    result = [r]
    while q > 0:
        q, r = divmod(q, base)
        result.insert(0,r)
    return result

# print(change_base(409,20))