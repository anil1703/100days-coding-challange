class product:
    gst=5
    sgst=3
    cgst=6
    offer=20
    def __init__(self,name,price,deal_price,quantity,rating):
        self.name=name;
        self.price=price;
        self.deal_price=deal_price;
        self.quantity=quantity;
        self.rating=rating;
    def groceries(self):
        print("name: {}".format(self.name))
        print("price: {}".format(self.price))
        print("deal_price: {}".format(self.deal_price))
        print("quantity: {}".format(self.quantity))
        print("rating: {}".format(self.rating))
    def electronics(self):
        print("name: {}".format(self.name))
        print("price: {}".format(self.price))
        print("deal_price: {}".format(self.deal_price))
        print("quantity: {}".format(self.quantity))
        print("rating: {}".format(self.rating))
    def clothes(self):
        print("name: {}".format(self.name))
        print("price: {}".format(self.price))
        print("deal_price: {}".format(self.deal_price))
        print("quantity: {}".format(self.quantity))
        print("rating: {}".format(self.rating))
class welcome:
        @staticmethod
        def greet():
            print("Thanks for Shopping")
obj1=product("milk",30,30,2,4.7)
obj1.groceries()
print(product.gst)
print("_________________")
obj2=product("IQOO",27000,24000,1,9.8)
obj2.electronics()
print(product.gst)
print("________________")
obj3=product("jeans",999,900,3,9.2)
obj3.clothes()
print(product.gst)
print("________________")
welcome.greet()

#
