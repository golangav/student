




def func():

    def inner():

        print(inner)
        print(inner.__closure__)

    return inner


obj = func()
obj()
print(obj.__closure__)