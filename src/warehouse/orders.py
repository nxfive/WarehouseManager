import datetime


class Order:

    """Order item is to order one pallet full of one item"""

    def __init__(self):
        self.identity = str(datetime.datetime.today())[:-7].replace('-', '').replace(':', '').replace(' ', '')
        self.items = dict()  # identity: amount

    def add_items(self):
        pass





