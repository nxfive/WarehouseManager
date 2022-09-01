def create_transport():
    pass


def create_products():
    pass


def create_workers():
    pass


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
