from src.providers.component import Component
from src.providers.transport import TransportCar
import random
import math
from src.utils.utils import FileMaker as Fm


class Company:

    def __init__(self, name, amount):
        self._name = name
        self._components = []
        with Component() as component:
            for _ in range(amount):
                self.components.append(component)
        Fm.save_items_in_json(self)
        self.pallet_per_component = {key: random.choice([0.25, 0.5, 0.75, 1]) for key in self.components}
        self.charge_for_pallet_per_component = {key: (1 - value) / value * random.randint(500, 5000)
                                                for (key, value) in self.pallet_per_component.items()}

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
        invoice = Invoice(order, self)
        Fm.save_invoice_to_text_file(self, invoice)
        return

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
