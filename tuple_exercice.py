print(__name__)

my_tuple = ("le", "!", "Bonjour", "monde")

print(my_tuple[2], my_tuple[0], my_tuple[3], my_tuple[1])

a, b, c, d = my_tuple[2], my_tuple[0], my_tuple[3], my_tuple[1]
print(a, b, c, d )



def une_func():
    global a
    a = "toto"
    print(a)



une_func()

print(a)