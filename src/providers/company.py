from src.providers.component import Component
from src.providers.transport import TransportCar
import random
import math
import os
import errno
import json


class Company:

    def __init__(self, name, amount):
        self._name = name
        self._components = []
        with Component() as component:
            for _ in range(amount):
                self.components.append(component)
        self.pallet_per_component = {key: random.choice([0.25, 0.5, 0.75, 1]) for key in self.components}
        self.charge_for_pallet_per_component = {key: (1 - value) / value * random.randint(500, 5000)
                                                for (key, value) in self.pallet_per_component.items()}

    def add_components_to_file(self):
        """
            This function creates a directory for storing components and later created invoice files.
        """
        dir_path = f'{self.name}'
        try:
            os.makedirs(dir_path, 644)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        filename = f'{self.name}_components.json'
        with open(os.path.join(dir_path, filename), 'w') as file:
            for component in self.components:
                file.write(json.dumps(component, default=Company.encoder_component, indent=4))

    @staticmethod
    def encoder_component(component):
        if isinstance(component, Component):
            return {'index': component.index_number, 'quantity': component.quantity}
        raise TypeError(f'Object {component} is not of type Component.')

    def check_order(self, order):
        pallets = 0
        for key, value in order.items.items():
            if key in self.charge_for_pallet_per_component:
                pallets += math.ceil(value / self.components[key].quantity * self.pallet_per_component[key])
        return pallets

    def arrange_transport(self, order):
        pallets = Company.check_order(self, order)
        transport = TransportCar(pallets, order)
        return transport

    def issue_an_invoice(self, order):
        """
            This function creates a directory for storing created invoice files.
        """
        dir_path = f'{self.name}'
        with open(os.path.join(dir_path, f'{order.identity}.txt'), 'w') as file:
            invoice = Invoice(order, self)
            file.write(f'Invoice number: {invoice.number}\n')
            for index, item, payment in enumerate(invoice.items_payment.items()):
                file.write(f'{index+1}. Item id: {item.identity} - {payment} PLN.\n')
            file.write(f'Sum: {invoice.payment} PLN\n')

    @property
    def name(self):
        return self._name

    @property
    def components(self):
        return self._components


class Invoice:

    def __init__(self, order, company):
        self.number = order.identity
        self.items = order.items
        self.items_payment = self.add_payment(company)
        self.payment = sum([self.items_payment.values()])

    def add_payment(self, company):
        items_payment = dict()
        for item in self.items:
            if item in company.charge_for_pallet_per_component.keys():
                items_payment[item] = company.charge_for_pallet_per_component[item]
        return items_payment
