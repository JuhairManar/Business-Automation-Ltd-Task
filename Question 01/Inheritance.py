class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    class Meta:
        abstract=True

    def get_car_info(self):
        return f'{self.year} {self.name} {self.model}'


class ElectricCar(Car):
    def __init__(self, name, model, year, battery_capacity):
        super().__init__(name, model, year)
        self.battery_capacity = battery_capacity

    def get_car_info(self):
        return f'{super().get_car_info()}\n\t Battery Capacity: {self.battery_capacity} kWh'


class GasCar(Car):
    def __init__(self, name, model, year, fuel_efficiency):
        super().__init__(name, model, year)
        self.fuel_efficiency = fuel_efficiency

    def get_car_info(self):
        return f'{super().get_car_info()}\n\t Fuel Efficiency: {self.fuel_efficiency} MPG'


car_type = input("Enter car type (Electric/Gas): ").lower()
name = input("Enter Name: ")
model = input("Enter model: ")
year = input("Enter year: ")

if car_type == "electric":
    battery_capacity = input("Enter battery capacity (kWh): ")
    car_obj = ElectricCar(name, model, year, battery_capacity)
    print("Car Information:")
    print('\t', car_obj.get_car_info())

elif car_type == 'gas':
    fuel_efficiency = input("Enter fuel efficiency (MPG): ")
    car_obj = GasCar(name, model, year, fuel_efficiency)
    print("Car Information:")
    print('\t', car_obj.get_car_info())
