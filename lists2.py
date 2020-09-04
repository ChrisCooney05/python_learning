toppings = ['pepperoni', 'pineapple', 'cheese',
            'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
# gives the length of the toppings list
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
# .sort() mutates our list sorted(pizzas) would return a new list and not mutate the original
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
# [:3] can also be [0:3] this means slice from 0 up to but not including index 3 of pizzas
print(three_cheapest)

three_most_expensive = pizzas[-3:]
# slices out the last three items, if you know the list length you can also use [4:] index 4 till end
print(three_most_expensive)

num_two_dollar_slices = prices.count(2)
# count will go through the list and count how many times 2 has been used
print(num_two_dollar_slices)
