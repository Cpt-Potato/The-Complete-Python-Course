def prime_generator(bound):
    for num in range(2, bound):
        for divider in range(2, num):
            if num % divider == 0:
                break
        else:
            yield num


g = prime_generator(100)
print(next(g))
print(list(g), '\n')


class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for num in range(self.start, self.stop):
            for div in range(2, num):
                if num % div == 0:
                    break
            else:
                self.start = num + 1
                return num
        raise StopIteration()


gen = PrimeGenerator(30)

for _ in range(10):
    print(next(gen))

my_numbers = [x for x in [1, 2, 3, 4, 5]]
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])
