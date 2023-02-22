array = ["a", "b", "c"]
password = "cbacabaa"



# for j in range(3):
#     for i in range(len(array)):
#         if array[i] == password:
#             print(f"Yay it's {array[i]}")

# test = ""
# count = 0
# for char in array:
#     print(test +char)
#     if test + char == password:
#         print(f"Yes! {test}")
# count +=1
# test = array[0]
# for char in array:
#     print(test +char)
#     if test + char== password:
#         print(f"Yes! {test}")
# count +=1
# test = array[1]
# for char in array:
#     print(test +char)
#     if test + char== password:
#         print(f"Yes! {test}")
# count += 1
# test = array[2]
# for char in array:
#     print(test +char)
#     if test + char== password:
#         print(f"Yes! {test}")


# def crackedFun():
#     crackedit = False
#     for x in range(1, 10):
#         while crackedit == False:
#             if x == 1:
#                 for i in range(len(array)):
#                     print(array[i])
#                     if array[i] == password:
#                         return print(f"Yes! {array[i]}")
#                         crackedit = True
#                         break
#                 x += 1
#             elif x == 2:
#                 for j in range(len(array)):
#                     for i in range(len(array)):
#                         print(array[j]+array[i])
#                         if array[j]+array[i] == password:
#                             return print(f"Yes! {array[j]+array[i]}")
#                             crackedit = True
#                             break
                        
#                 x += 1
#             elif x == 3:
#                 for k in range(len(array)):
#                     for j in range(len(array)):
#                         for i in range(len(array)):
#                             print(array[k]+array[j]+array[i])
#                             if array[k]+array[j]+array[i] == password:
#                                 return print(f"Yes! {array[k]+array[j]+array[i]}")
#                                 crackedit = True
#                                 break
#                 x += 1
#             elif x == 4:
#                 for l in range(len(array)):
#                     for k in range(len(array)):
#                         for j in range(len(array)):
#                             for i in range(len(array)):
#                                 print(array[l]+array[k]+array[j]+array[i])
#                                 if array[l]+array[k]+array[j]+array[i] == password:
#                                     print(f"Yes! {array[l]+array[k]+array[j]+array[i]}")
#                                     crackedit = True
#                                     break
#             elif x == 4:
#                 for m in range(len(array)):
#                     for l in range(len(array)):
#                         for k in range(len(array)):
#                             for j in range(len(array)):
#                                 for i in range(len(array)):
#                                     print(array[m]+array[l]+array[k]+array[j]+array[i])
#                                     if array[m]+array[l]+array[k]+array[j]+array[i] == password:
#                                         print(f"Yes! {array[m]+array[l]+array[k]+array[j]+array[i]}")
#                                         crackedit = True
#                                         break



# crackedFun()

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