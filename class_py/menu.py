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


brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

brunch = Menu('Brunch', brunch_items, 11, 16)
early_bird = Menu('Early Bird', early_bird_items, 15, 18)
dinner = Menu('Dinner', dinner_items, 17, 23)
kids = Menu('Kids', kids_items, 11, 21)
# Creates instances of each menu

print(brunch)
print(early_bird)
print(dinner)
print(kids)
# Because of our __str__ method printing the instance gives ous a nice string

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(
    ['salumeria plate', 'mushroom ravioli (vegan)']))
