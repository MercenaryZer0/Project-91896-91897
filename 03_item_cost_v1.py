import pandas

# dictionaries to hold ticket details
items = ["a", "b", "c", "d", "e"]
all_item_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

store_dict = {
    "Name": items,
    "Ticket Price": all_item_costs,
    "Surcharge": surcharge
}

item_frame = pandas.DataFrame(store_dict)

# Calculate the total ticket cost (item + surcharge)
item_frame['Total'] = item_frame['Surcharge']
+ item_frame['Ticket Price']

# calculate the profit for each item
item_frame['Profit'] = item_frame['Ticket Price'] - 5

# calculate item and profit totals
total = item_frame['Total'].sum()
profit = item_frame["Profit"].sum()

# output table with item data
print(item_frame)

# output total item sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Totale Profit: ${:.2f}".format(profit))