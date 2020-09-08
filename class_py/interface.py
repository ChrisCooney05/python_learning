from menu import Menu
from franchise import Franchise
from business import Business


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

#<-------franchise------->#

flagship_store = Franchise("1232 West End Road", [
                           brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [
                            brunch, early_bird, dinner, kids])

print(flagship_store)
print(new_installment)

flagship_store.available_menus(12)
new_installment.available_menus(17)

#<------business------>#

basta = Business("Basta Fazoolin' with my Heart", [
                 flagship_store, new_installment])

arepas_place_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_place_menu)

arepa = Business("Take a' Arepa", arepas_place)
