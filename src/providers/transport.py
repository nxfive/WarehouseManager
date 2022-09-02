import random


class TransportCar:

    def __init__(self, pallets, order):
        self.max_capacity = 40
        self.delivery_note = {key: value for (key, value) in order.items.items()}
        if self.max_capacity < pallets:
            self.delivery_cost = (self.max_capacity - pallets) * 100
            print(f"[ADDITIONAL FEE] {self.delivery_cost}")
        self.indexes = [key for key in order.items.keys()]
        self.number_of_pallets = pallets

    def drive_to_the_warehouse(self, warehouse):
        for ramp in warehouse.ramps:
            if ramp is False:
                ramp = self
                break


