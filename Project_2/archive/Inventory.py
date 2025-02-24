import pandas as pd
import random
from datetime import datetime
import logging

#Logging to check if the functions are running successfully
logging.basicConfig(filename = "/Users/user/Projects/Learning/Project_2/checks.log",format = '%(asctime)s %(message)s',filemode = 'w')
logger = logging.getLogger()

#A list of products from the the products like will be generated
products = [
    "Laptop", "Smartphone", "Headphones", "Bluetooth Speaker", "Smartwatch",
    "Tablet", "Wireless Mouse", "Mechanical Keyboard", "Gaming Monitor", "External Hard Drive",
    "Coffee Maker", "Microwave Oven", "Air Fryer", "Refrigerator", "Dishwasher",
    "Vacuum Cleaner", "Electric Kettle", "Toaster", "Blender", "Hair Dryer",
    "Running Shoes", "Sneakers", "Backpack", "Leather Wallet", "Sunglasses",
    "T-Shirt", "Jeans", "Hoodie", "Jacket", "Formal Shoes",
    "Wristwatch", "Perfume", "Smart TV", "Streaming Stick", "Projector",
    "Electric Toothbrush", "Fitness Tracker", "Water Bottle", "Camping Tent", "Sleeping Bag",
    "E-Book Reader", "Desk Lamp", "Office Chair", "Standing Desk", "Portable Fan",
    "Yoga Mat", "Dumbbells", "Resistance Bands", "Jump Rope", "Massage Gun"
]

#A list of categories
categories = [
    "Electronics", "Home Appliances", "Furniture", "Clothing", "Footwear",
    "Beauty & Personal Care", "Health & Wellness", "Sports & Outdoors", "Fitness Equipment", "Automotive Accessories", "Power Tools", "Medical Supplies",
    "Camera & Photography", "Gaming & Accessories", "Art & Crafts", "Hobby & DIY", "Party Supplies"
]

#Function for generating a random product, returns a string
def random_products(products):
    return random.choice(products)

#Function for generating a random category, returns a string
def random_categories(categories):
    return random.choice(categories)

#Function for generating a random price.
def random_prices():
    return random.randrange(1,20000)

#Function for generating a random stock quantity
def random_stock_quantity():
    return random.randrange(1,500)

#Function for generating the inventory database, this function creates a dataframe, updates each row using the functions given above
def inventory_data_gen(n):
    global df
    df = pd.DataFrame({"product_id":1,"name":"headphone","category":"Electronics","price": 1000,
                       "stock_quantity": 50},index = [0])
    
    for i in range(1,n+1,1):
        new_row = pd.DataFrame({"product_id":i+1,"name":random_products(products),
                                "category":random_categories(categories),"price": random_prices(),
                       "stock_quantity": random_stock_quantity()},index = [i])
        df = pd.concat([df,new_row],ignore_index = True)
    return df

products_dat = inventory_data_gen(50)
print(products_dat)

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
        
    def update_stock(self,quantity):
        #products_dat.at[self.product_id-1,"stock_quantity"] = quantity
        #print(products_dat.iloc[self.product_id-1].to_dict())
        self.stock_quantity = quantity
        logger.info('stock has been updated')

    def get_product_info(self):
        print(self.info)

class Inventory():
    def __init__(self,product: object):
        self.inven = {product.product_id: product}
    
    def add_product(self,product: object,database):
         index = database.shape[0]
         new_row = pd.DataFrame({"product_id":product.product_id,"name":product.name,
                                 "category":product.category,"price": product.price,
                       "stock_quantity": product.stock_quantity},index = [index])
         database = pd.concat([database,new_row],ignore_index= True)
         print(database.loc[index])
    
    def remove_product(self,product: object,database):
        database = database[database['name'] != product.name]
        #database.drop(index = int(product.product_id - 1),inplace = True,reset_index = )

    def get_low_stock_products(self,threshold: int):
        rows = products_dat.shape[0]
        low_invent = []
        for ind in range(0,rows,1):
            if int(df.at[ind,"stock_quantity"]) < threshold:
                low_invent.append(str(df.at[ind,"name"]))
        return low_invent

class Order:
    def __init__(self,order_id: int,customer_name: str,total_price:int,quantity,product:object):
        self.order_id = order_id
        self.customer_name = customer_name
        self.quantity = quantity
        self.items = {product.product_id:{"product":product,"quantity":self.quantity}}
        self.total_price = total_price

    def calculate_total(self,product: object):
        self.total_price = product.price * self.quantity
        return self.total_price

    def process_order(self,product: object,database):
        database.loc[database["product_id"]== product.product_id,"stock_quantity"] -= self.quantity
        infor = database.loc[df["product_id"] == product.product_id,"stock_quantity"].to_list()
        if len(infor) > 0:
            logger.info("processing successful")
        else:
            logger.error("processing not successful")
        print(infor)
        return datetime.now()

prod_test = Product(52,"Paneer","FMCG",200,500)
prod_test.update_stock(20)
prod_test.get_product_info()

inven_ins = Inventory(prod_test)
inven_ins.add_product(prod_test,products_dat)
inven_ins.remove_product(prod_test,products_dat)
print(inven_ins.get_low_stock_products(50))
inven_ins.add_product(prod_test,products_dat)

order_1 = Order(1,"Deepak",0,100,prod_test)
print(order_1.calculate_total(prod_test))
print(order_1.process_order(prod_test,products_dat))