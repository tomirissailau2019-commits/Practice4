def even_numbers(max_number):
    number = 2

    while number <= max_number:
        yield number
        number += 2


print("\nEven numbers generator:")

for number in even_numbers(10):
    print(number)