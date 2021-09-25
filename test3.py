# '''
# index = 0 1 3 4
# day   = 1 2 4 5

# '''

array = [100, 180, 260, 310, 40, 535, 695]

buy_price = min(array)
buy_day = array.index(buy_price) + 1

sell_price = max(array)
sell_day = array.index(sell_price) + 1

profit = sell_price - buy_price

print(f"Buy on - {buy_day} - Sell on - {sell_day} - Profit = {profit}")

print("buy on-",buy_day,"Sell on-",sell_day,"profit =",profit)

