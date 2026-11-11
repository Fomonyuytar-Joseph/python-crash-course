import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")

product_list = inv_file["Sheet1"]

products_per_supplier = {}
total_value_per_supplier = {}
products_under_10_inv = {}


for product_row in range(2, product_list.max_row + 1):
    product_num = product_list.cell(product_row, 1).value
    inventory = product_list.cell(product_row, 2).value
    price = product_list.cell(product_row, 3).value
    supplier_name = product_list.cell(product_row, 4).value

    #add a fifth column
    inventory_price = product_list.cell(product_row, 5)
    
    

    # calculation number of products per supplier
    products_per_supplier[supplier_name] = (
        products_per_supplier.get(supplier_name, 0) + 1
    )

    # calculator of total inventory value
    calculated_value = inventory * price
    total_value_per_supplier[supplier_name] = (
        total_value_per_supplier.get(supplier_name, 0) + calculated_value
    )

    # logic products with inventory less than 10
    if inventory < 10:
        products_under_10_inv[int(product_num)] = int(inventory)

    # add value for total inventory price
    inventory_price.value = calculated_value
    
    


print(products_per_supplier)
print(total_value_per_supplier)
print(products_under_10_inv)

#save the file
inv_file.save("inventory_with_total_value.xlsx")