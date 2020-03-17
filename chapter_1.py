from custom_exception import IllegalClassError


class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        self.__pax_count = pax_count
        self.__car_mass = car_mass
        self.__gear_count = gear_count

        if car_mass > 2000:
            raise IllegalClassError("Value can not be higher then 2000.")

        if pax_count > 5 or pax_count < 1:
            raise IllegalClassError("Value has to be between 1 and 5.")

    @property
    def pax_count(self):
        return self.__pax_count

    @pax_count.setter
    def pax_count(self, p):
        if p > 5 or p < 1:
            raise IllegalClassError("Value has to be between 1 and 5.")
        self.__pax_count = p

    @property
    def car_mass(self):
        return self.__car_mass

    @car_mass.setter
    def car_mass(self, c):
        if c > 2000:
            raise IllegalClassError("Value can not be higher then 2000.")
        self.__car_mass = c

    def total_mass(self, person_weight=70):
        return self.__car_mass + self.__pax_count * person_weight


if __name__ == '__main__':
    c = Car(4, 1600, 5)
    #c.car_mass = 2100
    #c.pax_count = 7
    print(c.total_mass())
