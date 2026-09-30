def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


print("\nGenerator function:")

for number in simple_generator():
    print(number)
