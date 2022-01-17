from warehouse import Warehouse
from product import Product
from worker import WarehouseOperator
from task import Task
from transport import TransportCar


def create_products():
    for i in range(500):
        p1 = Product()
        Product.add_product_to_products(p1)


def create_tasks():
    for product in TransportCar.delivery:
        t2 = Task(product.location, product, w1)
        Task.new_tasks.append(t2)


if __name__ == '__main__':
    # create warehouse
    w1 = Warehouse('3m')

    # create products
    create_products()

    # create the transport to warehouse
    t1 = TransportCar()

    create_tasks()

    Task.display_tasks()

    # create workers
    wop1 = WarehouseOperator('Anna', 'Williams', 49)
    wop2 = WarehouseOperator('Tom', 'Adams', 49)
    wop3 = WarehouseOperator('Merry', 'Terry', 49)
    wop4 = WarehouseOperator('Mark', 'Charles', 49)
    wop5 = WarehouseOperator('Paul', 'Lucas', 49)
    wop6 = WarehouseOperator('Tatiana', 'Gasol', 49)
    wop7 = WarehouseOperator('Krystian', 'Jordan', 49)
    wop8 = WarehouseOperator('Natalia', 'Monk', 49)
    wop9 = WarehouseOperator('Monica', 'Jerry', 49)

    # add workers to group and change
    WarehouseOperator.add_to_job_group(wop1)
    WarehouseOperator.add_to_change(wop1)
    WarehouseOperator.add_to_job_group(wop2)
    WarehouseOperator.add_to_change(wop2)
    WarehouseOperator.add_to_job_group(wop3)
    WarehouseOperator.add_to_change(wop3)
    WarehouseOperator.add_to_job_group(wop4)
    WarehouseOperator.add_to_change(wop4)
    WarehouseOperator.add_to_job_group(wop5)
    WarehouseOperator.add_to_change(wop5)
    WarehouseOperator.add_to_job_group(wop6)
    WarehouseOperator.add_to_change(wop6)
    WarehouseOperator.add_to_job_group(wop7)
    WarehouseOperator.add_to_change(wop7)
    WarehouseOperator.add_to_job_group(wop8)
    WarehouseOperator.add_to_change(wop8)
    WarehouseOperator.add_to_job_group(wop9)
    WarehouseOperator.add_to_change(wop9)

    # add tasks to workers in placement group
    for worker in WarehouseOperator.placement:
        WarehouseOperator.add_tasks(worker)
        print(worker.__dict__)

    print('----------------------------')
    WarehouseOperator.show_added_tasks_to_workers()

    # workers in placement group do the tasks
    for worker in WarehouseOperator.placement:
        WarehouseOperator.do_the_task(worker)

    # check that locations have been filled with products
    print(Warehouse.locations)
