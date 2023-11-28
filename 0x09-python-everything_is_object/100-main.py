#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

# #!/usr/bin/python3
# def magic_string():
# count the number of times the function is called, if counter is not found, it will be created
# and initialized to 0 and then incremented by 1 each time the function is called
#     magic_string.counter = getattr(magic_string, "counter", 0) + 1
# to avoid comma, at the end of the string
#     return "BestSchool, " * (magic_string.counter - 1) + "BestSchool"
