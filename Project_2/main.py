from module import modules

prod_test = modules.Product(52,"Paneer","FMCG",200,500)
prod_test.update_stock(20)
prod_test.get_product_info()

# prod_test_2 = modules.Product(53,"Paratta","FMCG",100,1000)
# prod_test_3 = modules.Product(54,"Dosa","FMCG",70,700)

inven_test = modules.Inventory()
inven_test.add_product(prod_test)
# inven_test.add_product(prod_test_2)
# inven_test.add_product(prod_test_2)
# inven_test.add_product(prod_test_3)
# inven_test.remove_product(prod_test_3)

# inven_test.get_low_stock_products(700)

order_1 = modules.Order(1,"Deepak",0,prod_test,50)
print(order_1.calculate_total(prod_test))
order_1.process_order(prod_test)