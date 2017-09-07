class Car:
    ''' Car class'''
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.num_tires = 4
        self.color = ''
    def __str__(self):
        self_str = '\n' + self.make + ' ' + self.model + '\nTires: ' + str(self.num_tires) + '\nColor: ' + self.color
        return self_str

    def get_info(self):
        info_str = '\n' + self.make + ' ' + self.model + '\nTires: ' + str(self.num_tires) + '\nColor: ' + self.color
        return info_str



    def get_make(self):
        '''Make'''
        return self.make

    def get_model(self):
        '''Model'''
        return self.model


dream_car = Car('Tesla','Model 3')
ok_car = Car('Mazda','5')

# default_car = Car()

# dream_car.make = 'Tesla'
# dream_car.model = 'Model 3'

# ok_car.make = 'Mazda'
# ok_car.model = '5'

# print(dream_car.make, dream_car.model)

print(dream_car)
print('')
print('Make:', ok_car.get_make())

print(ok_car.get_info())
# print(default_car.make, default_car.model)

