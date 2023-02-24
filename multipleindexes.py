#  Assumptions:
# The length of the password is unknown
# The characters include ASCII lowercase, uppercase, digits, special characters
# We could create an array of all of the potential ASCII characters
# Idea: have a variable within the loop that is switched to True when the password is matched, and this exits the for loop
# Idea: if password is cracked then return True, and if not then increase count by 1, 
# and the count is a measure of how many characters there are in the password, and how many nested for loops there are.
# Does it have to be a function? Or could it just be a for loop?
# Recursion!
# Could we test a possible solution both ways round to try to speed up getting to the solution? i.e. use reverse


array = ["a", "b", "c"]
password = "cbacabaa"



def crackedFun():
    for num_dig in range(1, 9):
            if num_dig == 1:
                for i in range(len(array)):
                    test = array[i]
                    print(test)
                    if test == password:
                        return print(f"Yes! {test}")
                num_dig += 1
            elif num_dig == 2:
                for j in range(len(array)):
                    for i in range(len(array)):
                        test = array[j]+array[i]
                        print(test)
                        if test == password:
                            return print(f"Yes! {test}") 
                num_dig += 1
            elif num_dig == 3:
                for k in range(len(array)):
                    for j in range(len(array)):
                        for i in range(len(array)):
                            test = array[k]+array[j]+array[i]
                            print(test)
                            if test == password:
                                return print(f"Yes! {test}")
                num_dig += 1
            elif num_dig == 4:
                for l in range(len(array)):
                    for k in range(len(array)):
                        for j in range(len(array)):
                            for i in range(len(array)):
                                test = array[l]+array[k]+array[j]+array[i]
                                print(test)
                                if test == password:
                                    return print(f"Yes! {test}")
                num_dig += 1
            elif num_dig == 5:
                for m in range(len(array)):
                    for l in range(len(array)):
                        for k in range(len(array)):
                            for j in range(len(array)):
                                for i in range(len(array)):
                                    test = array[m]+array[l]+array[k]+array[j]+array[i]
                                    print(test)
                                    if test == password:
                                        return print(f"Yes! {test}")
                num_dig += 1
            elif num_dig == 6:
                for n in range(len(array)):   
                    for m in range(len(array)):
                        for l in range(len(array)):
                            for k in range(len(array)):
                                for j in range(len(array)):
                                    for i in range(len(array)):
                                        test = array[n]+array[m]+array[l]+array[k]+array[j]+array[i]
                                        print(test)
                                        if test == password:
                                            return print(f"Yes! {test}")
                num_dig += 1
            elif num_dig == 7:
                for o in range(len(array)):
                    for n in range(len(array)):   
                        for m in range(len(array)):
                            for l in range(len(array)):
                                for k in range(len(array)):
                                    for j in range(len(array)):
                                        for i in range(len(array)):
                                            test = array[o]+array[n]+array[m]+array[l]+array[k]+array[j]+array[i]
                                            print(test)
                                            if test == password:
                                                return print(f"Yes! {test}")
                num_dig += 1
            elif num_dig == 8:
                for p in range(len(array)):
                    for o in range(len(array)):
                        for n in range(len(array)):   
                            for m in range(len(array)):
                                for l in range(len(array)):
                                    for k in range(len(array)):
                                        for j in range(len(array)):
                                            for i in range(len(array)):
                                                test = array[p]+array[o]+array[n]+array[m]+array[l]+array[k]+array[j]+array[i]
                                                print(test)
                                                if test == password:
                                                    return print(f"Yes! {test}")





crackedFun()


# Need to find the pattern and generalise
# How do we 'add another for loop"
# What should the variable (i, j, k, l etc be?)
# Need to break out of nested for loops when the correct password is found