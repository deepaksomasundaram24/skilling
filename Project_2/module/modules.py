import pandas as pd
import random
from datetime import datetime
import logging
import json
from os import path 

logging.basicConfig(filename = "/Users/user/Projects/Learning/Project_2/checks.log",format = '%(asctime)s %(message)s', filemode = 'w')
logger = logging.getLogger()

class Product:
    def __init__(self,product_id: int,name: str,category: str,price: int,stock_quantity: int):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
        self.info = {self.product_id:{"name":self.name, 
                                      "category":self.category,"price":self.price,
                                      "stock_quantity":self.stock_quantity}}
        
        file_name = "/Users/user/Projects/Learning/Project_2/database/products.json"
        if path.isfile(file_name) == False:
            raise Exception ("File not found")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)
                for key,value in json_dict.items():
                    print(type(key),type(self.product_id))
                    if key == str(self.product_id):
                        logger.info("Items already present in products list")
                        print("Item already present in product list")
                        return
                json_dict.update(self.info)
            except json.decoder.JSONDecodeError:
                json_dict = {}
                json_dict.update(self.info)

        with open(file_name, 'w') as json_file:
            json.dump(json_dict,json_file,indent=4)

    def update_stock(self,quantity):
        #products_dat.at[self.product_id-1,"stock_quantity"] = quantity
        #print(products_dat.iloc[self.product_id-1].to_dict())
        file_name = "/Users/user/Projects/Learning/Project_2/database/products.json"
        if path.isfile(file_name) == False:
            raise Exception ("File not found")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)
                json_dict[f"{self.product_id}"]["stock_quantity"] += quantity
            except json.decoder.JSONDecodeError:
                json_dict = {}
                print("Product information has not been loaded")

        with open(file_name, 'w') as json_file:
            json.dump(json_dict,json_file,indent=4)
        logger.info('stock has been updated')

    def get_product_info(self):
        print(self.info)

class Inventory():
    def __init__(self):
        return 
    
    def add_product(self,product: Product):
        file_name = "/Users/user/Projects/Learning/Project_2/database/inventory.json"
        if path.isfile(file_name) == False:
            raise Exception ("File not found")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)
                for key,value in json_dict.items():
                    #print(type(key),type(product.product_id))
                    if key == str(product.product_id):
                        logger.info("Items already present in inventory")
                        print("Item already present in inventory")
                        return
                json_dict.update(product.info)
                logger.info("the inventory has been successfully updated")
            except json.decoder.JSONDecodeError:
                json_dict = {}
                json_dict.update(product.info)

        with open(file_name, 'w') as json_file:
            json.dump(json_dict,json_file,indent=4)
    
    def remove_product(self,product: Product):
        file_name = "/Users/user/Projects/Learning/Project_2/database/inventory.json"
        if path.isfile(file_name) == False:
            raise Exception ("File not found")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)
                json_dict.pop(f"{product.product_id}")
                logger.info("the product has been deleted from inventory")
            except json.decoder.JSONDecodeError:
                json_dict = {}
                json_dict.pop(f"{product.product_id}")

        with open(file_name, 'w') as json_file:
            json.dump(json_dict,json_file,indent=4)

    def get_low_stock_products(self,threshold: int):
        file_name = "/Users/user/Projects/Learning/Project_2/database/inventory.json"
        if path.isfile(file_name) == False:
            raise Exception ("File not found")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)

            except json.decoder.JSONDecodeError:
                print("Inventory does not exist")
                return 
            low_stock_dict = {}
            for key,value in json_dict.items():
                if value["stock_quantity"] < threshold:
                    low_stock_dict.update(json_dict[key])
                    print(key,value)

        return low_stock_dict
    
class Order:
    def __init__(self,order_id: int,customer_name: str,total_price: int ,product:Product,quantity:int):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_price = total_price
        self.quantity = quantity
        self.items = {self.quantity: product.info}
        self.order_info = {self.order_id: {"customer_name": self.customer_name,"items":self.items,"price":product.price*self.quantity}}

        file_name = "/Users/user/Projects/Learning/Project_2/database/orders.json"
        if path.isfile(file_name) == False:
            raise Exception ("File not found")

        with open(file_name) as file:
            try:
                json_dict = json.load(file) #If attempting to do duplicate order, then no processing of the order
                print(list(json_dict.keys()))
                if str(self.order_id) in list(json_dict.keys()):
                    print("This is a duplicate order, it cannot be processsed")
                    return 
                json_dict.update(self.order_info)
            except json.decoder.JSONDecodeError:
                json_dict = {}
                json_dict.update(self.order_info)

        with open(file_name, 'w') as json_file:
            json.dump(json_dict,json_file,indent=4)

    def calculate_total(self,product:Product):
        self.total_price = product.price * self.quantity
        return self.total_price

    def process_order(self,product:Product):
        if product.stock_quantity < self.quantity:
            print("There is not enough stock")
            logger.info("There is not enough stock")
            return 
        else:
            product.update_stock(self.quantity)
            logger.info("The order has been processed")
            return
