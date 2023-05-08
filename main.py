# Oops Concept : 
# -------------------------------------------

class ClassName:
    # pass
    pay_rate = 0.8
    
    def __init__(self, name:str, price:int, quantity:int): # these def function will called every time whenever an instance is created, it's called magic method.
        #Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero!" #with assert we can add our own exception message
        assert quantity >=0, f"Quantity {quantity} is not greater than"
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
         
    # def calculate_total_price(anyOneParameterorSelf, x, y):
    def calculate_total_price(anyOneParameterorSelf):
        # return x*y
        return anyOneParameterorSelf.price * anyOneParameterorSelf.quantity
    
    #Actions to execute
        ClassName.all.append(self)
    

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        # self.price = self.price * ClassName.pay_rate
        self.price = self.price * self.pay_rate
        

    def __repr__(self):
        return "item"
        

# Creating instances of class 
item1 = ClassName("Phone", 44, 5) # pass some value of name 
# item1.price = 100
# item1.quantity = 5 
# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = ClassName("Mobile", 60 , 3)
# item2.price = 200
# item2.quantity = 7
# print(item2.calculate_total_price(item2.price, item2.quantity))

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(ClassName.__dict__) # All the attributes for Class Level
# print(item1.__dict__) # All the attributes for instance level

# item1 = ClassName("phone", 100, 2)
# item1.apply_discount()
# print(item1.price)

# item2 = ClassName("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

item1 = ClassName("Laptop", 30, 1)
item2 = ClassName("Phone", 450, 3)
item3 = ClassName("Cable", 45, 2)
item4 = ClassName("Keyboard", 23, 4)
item5 = ClassName("Mouse", 22, 9)

print(ClassName.all)