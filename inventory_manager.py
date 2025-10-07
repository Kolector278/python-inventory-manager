import csv

inventory_data = {}
# reads inventory.csv and prints

with open('inventory.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            inventory_data[row['product_id']] = row


order_data = []
with open('order.csv','r',newline='') as f:
        reader2 = csv.DictReader(f)
        for row in reader2:
            order_data.append(row)


#load and process orders

for order in order_data:
    product_id = order['product_id']

    quantity_ordered = int(order['quantity_ordered'])
 #actually updates
    if product_id in inventory_data:

        current_quantity = int(inventory_data[product_id]['quantity'])

        inventory_data[product_id]['quantity'] =  str(current_quantity - quantity_ordered)


print("inventory after processing orders:")
print(inventory_data)

with open('updated_inventory.csv','w',newline='') as output_file:
    fieldnames = ['product_id', 'product_name', 'quantity', 'reorder_level']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(inventory_data.values())

print("\nInventory has be updated successfully")
