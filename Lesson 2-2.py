import random
class Supermarket:

    all_sold_products = 0
    def __init__(self, name):
        self.name = name
        self.sold_products = 0

    def calculation_local_sales(self):
        for i in range(100):
            sales = random.randint(0, 1)
            if sales:
                self.sold_products += 1

    def calculation_all_sales(self, *args):
        self.all_sold_products = sum(*args)
        return self.all_sold_products



metro_market = Supermarket('Metro')
metro_market.calculation_local_sales()
print(f'At the supermarket {metro_market.name}, {metro_market.sold_products} sales')

freshet_market = Supermarket('Freshet')
metro_market.calculation_local_sales()
print(f'At the supermarket {freshet_market.name}, {freshet_market.sold_products} sales')

Supermarket.calculation_all_sales(freshet_market.sold_products, metro_market.sold_products)
print(Supermarket.all_sold_products)