class NumberIterator:
    def __init__(self, max_number):
        self.number = 1
        self.max_number = max_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.max_number:
            current_number = self.number
            self.number += 1
            return current_number
        else:
            raise StopIteration


print("\nCustom iterator:")

number_iterator = NumberIterator(5)

for number in number_iterator:
    print(number)