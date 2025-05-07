total_per_upc = {}

for key in sales:
    for items in key["items"]:
        type = items["upc"]
        value = items["unit_price"]
        if type not in total_per_upc:
            total_per_upc[type] = 0
            total_per_upc[type] += value

print(total_per_upc)