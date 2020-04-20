#Add a method for interacting with a pizza's toppings, 
# called add_topping.
#Add a method for outputting a description of the
#pizza (sample output below).
#Make two different instances of a pizza.
#If you have properly defined the class, 
#you should be able to do something like the 
#following code with your Pizza type.


class Pizza:
    
    def __init__(self):
        self.size = ""
        self.crust_type = ""
        self.toppings = list()
        
    def add_topping(self, item):
        self.toppings.append(item)
        
        
    def print_order(self):
        print(f"I would like a {self.size}-inch, {self.crust_type} pizza with {' and '.join(self.toppings)}.")


my_pizza = Pizza()
my_pizza.size = 16
my_pizza.crust_type = "thin crust"
my_pizza.add_topping("mushrooms")
my_pizza.add_topping("bell peppers")
my_pizza.print_order()

his_pizza = Pizza()
his_pizza.size = 12
his_pizza.crust_type = "Deep dish"
his_pizza.add_topping("sausage")
his_pizza.add_topping("onions")
his_pizza.print_order()

