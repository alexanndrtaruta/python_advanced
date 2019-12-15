class Vehicle:
    start_vehicle = False

    def __init__(self, vehicle_type, spaciousness,
                 engine_volume, volume_of_the_tank, engine_type, fuel_consumption):

        self._vehicle_type = vehicle_type
        self._spaciousness = spaciousness
        self._engine_volume = engine_volume
        self._volume_of_the_tank = volume_of_the_tank
        self._engine = engine_type
        self._fuel_consumption = fuel_consumption

    def fill_up(self, fuel_volume):

         fuel_in_the_tank = 0
         while fuel_in_the_tank <= self._volume_of_the_tank:
            if fuel_volume + fuel_in_the_tank <= self._volume_of_the_tank:
                fuel_in_the_tank += fuel_volume
                print(f'Now your tank is {fuel_in_the_tank} liters full')
                break

            elif fuel_in_the_tank + fuel_volume >= self._volume_of_the_tank:
                print('Too much fuel')
                break

    def start_engine(self):
        self.start_vehicle = True

    def shut_off_engine(self):
        self.start_vehicle = True


class MotorCar(Vehicle):

    def __init__(self, num_of_doors, max_speed, vehicle_type, spaciousness, engine_volume, volume_of_the_tank,
                 engine_type, fuel_consumption):
        super().__init__(vehicle_type, spaciousness, engine_volume, volume_of_the_tank, engine_type, fuel_consumption)
        self.num_of_doors = num_of_doors
        self.max_speed = max_speed

    def fill_up(self, fuel_volume):
        if self.start_vehicle:
            super(MotorCar, self).fill_up(fuel_volume)
        else:
            print('shut off the car')


class Truck(Vehicle):
    start_vehicle = False

    def __init__(self, carrying_capacity, vehicle_type, spaciousness, engine_volume, volume_of_the_tank,
                 engine_type, fuel_consumption ):
        self.carrying_capacity = carrying_capacity
        super().__init__(vehicle_type, spaciousness, engine_volume, volume_of_the_tank, engine_type, fuel_consumption)

    def fill_up(self, fuel_volume):
        if self.start_vehicle:
            super(Truck, self).fill_up(fuel_volume)
        else:
            print('shut off the car')
