import os
import errno
import json


def validation_input(value, value_name):
    if value_name in ('name', 'surname'):
        if not isinstance(value, str):
            raise TypeError(f'{value_name.capitalize()} value must be str not {type(value).__name__}.')
        if not value.isalpha():
            raise ValueError(f'{value_name.capitalize()} should only include alphabet chars.')
    if value_name == 'age':
        if not isinstance(value, (str, int)):
            raise TypeError(f'Age value cannot be other than str if its a num or int.')
        try:
            int(value)
            if not 18 >= value <= 65:
                raise ValueError('Age value should be between 18 and 65')
        except ValueError:
            raise ValueError('Wrong value.')


def is_dir_exist(dir_path):
    try:
        os.makedirs(dir_path, 644)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


class FileMaker:

    @staticmethod
    def save_items_in_json(instance):
        """
            This function creates a directory for storing components for Company instance or
            products for ProductProduction instance.
        """
        dir_path = f'{instance.name}'
        is_dir_exist(dir_path)

        if instance.__class__.__name__ == 'Company':
            filename = f'{instance.name}_components.json'
            with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as file:
                for component in instance.components:
                    json.dump(component, file, indent=4)
        if instance.__class__.__name__ == 'ProductProduction':
            filename = f'{instance.name}_products.json'
            with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as file:
                for product, components in instance.products_components.items():
                    json.dump((product, components), file, indent=4)

    @staticmethod
    def save_invoice_to_text_file(company_instance, invoice):
        """
            This function creates a directory for storing created invoice files.
        """
        dir_path = 'Invoices'
        is_dir_exist(dir_path)

        with open(os.path.join(dir_path, f'{company_instance.name}_{invoice.number}.txt'),
                  'w', encoding='utf-8') as file:
            file.write(f'Invoice number: {invoice.number}\n')
            for index, item, payment in enumerate(invoice.items_payment.items()):
                file.write(f'{index + 1}. Item id: {item.identity} - {payment} PLN.\n')
            file.write(f'Sum: {invoice.payment} PLN\n')


def create_transport():
    pass


def create_products():
    pass


def create_workers():
    pass


