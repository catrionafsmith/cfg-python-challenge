array = ["a", "b", "c"]
password = "cba"



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


for i in range(len(array)):
    print(array[i])
    if array[i] == password:
        print(f"Yes! {array[i]}")
for j in range(len(array)):
    for i in range(len(array)):
        print(array[j]+array[i])
        if array[j]+array[i] == password:
            print(f"Yes! {array[j]+array[i]}")
for k in range(len(array)):
    for j in range(len(array)):
        for i in range(len(array)):
            print(array[k]+array[j]+array[i])
            if array[k]+array[j]+array[i] == password:
                print(f"Yes! {array[k]+array[j]+array[i]}")
                break
for l in range(len(array)):
    for k in range(len(array)):
        for j in range(len(array)):
            for i in range(len(array)):
                print(array[l]+array[k]+array[j]+array[i])
                if array[l]+array[k]+array[j]+array[i] == password:
                    print(f"Yes! {array[l]+array[k]+array[j]+array[i]}")
                    break
# Need to find the pattern
# How do we 'add another for loop"
# What should the variable (i, j, k, l etc be?)
# Need to break out of nested for loops when the correct password is found