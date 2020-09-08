class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
# we pass self in as convetion, this stores everyting in instance variables

    def __str__(self):
        return '{name} menu available from {start} till {end}'.format(name=self.name, start=self.start_time, end=self.end_time)
# this is known as a dunder, when using print(Menu_instance) it will print this sting, not the place in memory like usual

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return total_price
