def greeting():
    def say_hello():
        return "Hello"
    return say_hello()


hello = greeting()
print(hello)
