x = 10


def my_numbers():
    global x
    print(x)
    x = 7
    print("My favorite number is ", x)


my_numbers()
print(x)
