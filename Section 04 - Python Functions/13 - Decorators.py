def my_decorator(function):
    def wrapper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper()


def say_hello():
    return "hello world python!"


decorate = my_decorator(say_hello)
print(decorate)
print(say_hello())
