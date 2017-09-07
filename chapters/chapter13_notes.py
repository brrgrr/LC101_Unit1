class Car:
    def __init__(self, make, model, color):
        self.total_distance = 0
        self.make = make
        self.model = model
        self.color = color

    def drive(self, distance)
        self.total_distance += distance
        print('traveled {}, for a total of {}').format(
            distance, self.total_distance)

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model
    # def __


class GasCar(Car):
    def __init__(self, make, model)


def main():
    c1 = Car('Mazda', '5')
    c2 = Car('Ford', 'Escape')
    c3 = Car(input("make\n"), input("model\n"))
    print(c1 == c2)
    print(c1 == c3)


if __name__ == '__main__':
    main()
