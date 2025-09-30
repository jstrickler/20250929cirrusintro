# define function
def say_hello():
    print("Hello, world")

say_hello()  # Call function
say_hello()

def greet(whom: str="world"):  # type hint!
    print(f"Hello, {whom}")

greet("world")
greet("New York")
greet("Texas")
greet("Mom")
greet(123)
greet()

# def NAME(p1, p2=MMM, p3=XXX):
#    pass
#   NAME(v1, v2, v3, ...)
print('-' * 60)

def greet_many(*whom):
    for thing in whom:
        print(f"Hello, {thing}")

greet_many("mom", "dad")
greet_many("Aunt Sally")
greet_many("dog", 'cat', 'wildebeest')

# def spam(a, b, *c):
#    pass

def c2f(fahr):
    # blah blah
    return celsius

x = c2f(100)
