class catagory:
    def __init__(self,catagory):
        self.catagory=catagory
    def getcatagory(self):
        return self.catagory
class product(catagory):
    def __init__(self,name,price,stock,catagory):
        super().__init__(catagory)
        self.name=name
        self.price=price
        self.stock=stock
    def display(self):
        print('name :',self.name,'\n price :',self.price,'\n stock :',self.stock,'\n catagory :',self.catagory)
    def  discount(self,discoun):
        self.discount=discoun
        disprice=(self.discount/100)*self.price
        print('discounted price is',self.price-disprice)


prod1=product('tecnotip',10,200,'pen')
prod1.display()
prod1.discount(10)

prod2=product('s22 ultra',100000,100,'mobile')
prod2.discount(20)





