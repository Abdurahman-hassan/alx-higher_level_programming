#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return i + 1
    except:
        print()
        return i

# or we can use the following code:
# def safe_print_list(my_list=[], x=0):
#     try:
#         for i in range(x):
#             print(my_list[i], end="")
#         print()
#         return x
#     except IndexError:
#         print()
#         return i
