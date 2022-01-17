from product import Product
import random


class TransportCar:

    products = Product.products
    delivery = []

    def __init__(self):
        self.delivery_note = TransportCar.get_delivery()  # {'index': 1234szt, 'index1': 124szt}
        self.index = [index for index in self.delivery_note.keys() if index != 'INDEX']
        self.number_of_pallets = len(self.delivery_note.keys())

    @staticmethod
    def get_delivery():
        number_of_ordered_pallets = random.randint(20, 35)
        print(f'The quantity of the ordered goods: {number_of_ordered_pallets}')
        delivery = {'INDEX': 'AMOUNT'}
        if TransportCar.products:
            for _ in range(number_of_ordered_pallets):
                instance = random.choice(TransportCar.products)
                delivery[instance.index_number] = instance.quantity
                TransportCar.products.remove(instance)
                TransportCar.delivery.append(instance)
        else:
            print('There are not enough goods to fulfill the order. '
                  f'Missing {1 + number_of_ordered_pallets - len(delivery.keys())} pallets.')
        return delivery
