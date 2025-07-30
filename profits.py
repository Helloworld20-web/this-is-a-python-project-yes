costprice = int(input("Type in cost price: "))
sellingprice = int(input("Type in selling price: "))

stonks = sellingprice - costprice
if (stonks > costprice*2):
    print("Profits:", stonks)
    print("Big Stonks$$$$$$ :)")

elif (stonks > costprice):
    print("Profits:", stonks)
    print("Stonks :)")

else:
    print("Profits:", stonks)
    print("No stonks :(")