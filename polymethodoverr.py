class product:
    def __init__(self,name,category,price):
        self.pname=name
        self.pcatagory=category
        self.pprice=price

    def calculate_price(self):
        pprice=self.pprice+20
        return pprice

class Sales(product):
    def __init__(self, name, category, price,qty):
        product.__init__(self,name, category, price)
        self.qty=qty

    def calculate_price(self):
        total=product.calculate_price(self)*self.qty
        return total

sale1=Sales('pen','sat',10,3)
prod1=product('pen','stat',10)
print(prod1.calculate_price())  
print(sale1.calculate_price())