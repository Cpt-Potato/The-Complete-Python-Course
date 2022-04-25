class Iterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __getitem__(self, item):
        return self.cars[item]


for car in Iterable():
    print(car)
