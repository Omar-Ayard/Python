def debug(f):
    def new_function(a, b):
        print("Decoradores antes de la función Principal")
        return f(a, b)
    return new_function

@debug
def add(a, b):
    return a + b
print(add(7, 5))