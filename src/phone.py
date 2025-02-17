from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_sim):
        super().__init__(name, price, quantity)
        self.__number_sim = number_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_sim})"

    @property
    def number_sim(self):
        return self.__number_sim

    @number_sim.setter
    def number_sim(self, number):
        if isinstance(number, int) and number > 0:
            self.__number_sim = number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

