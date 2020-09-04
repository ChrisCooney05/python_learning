hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
    total_price += price

average_price = total_price / len(prices)
print('Average Haircut Price: £' + str(average_price))

new_prices = [price - 5 for price in prices]
# this is known as list comprehension we take 5 of each price in prices and return that

print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
# len(hairstyles) gives us a length, we then create a range so we can create a for loop
print('Total Revenue: £' + str(total_revenue))

average_daily_revenue = total_revenue / 7
print('£' + str(average_daily_revenue))

cuts_under_30 = [price for price in prices if price < 30]
# returns a new list with only values under 30
print(cuts_under_30)

for price in prices:
    if price < 35:
        continue
    print(price)
# contine can be used to skip over an element and continue with the loop.

for cut in hairstyles:
    print(cut)
    if cut == "crew":
        break
# Like Javascript, we can break out of a loop using break when a condition is met
