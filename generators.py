# Custom iterator that returns numbers from 1 to n

class MyIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# Usage
it = MyIterator(5)

for number in it:
    print(number)
