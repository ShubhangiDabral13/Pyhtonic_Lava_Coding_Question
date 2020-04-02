def profit_price(price):
    profit, min,buy_day,sell_day = 0,price[0],0,0
    for i in range(len(price)):
        if price[i]>min:
            if (price[i]-min)>profit:
                profit = (price[i]-min)
                sell_day = i
        else:
            min =  price[i]
            buy_day = i

    print("the buying day is {} and selling day is {} and the total profit is {}".format(buy_day,sell_day,profit))


price = [100, 180, 260, 310, 40, 535, 695]
profit_price(price)
