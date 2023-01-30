import random

class bank:
    def __init__(self,bankname,branch,ifsc):
        self.bankname=bankname
        self.branch=branch
        self.ifsc=ifsc

    def aboutbank(self):
        return self.bankname
        return  self.branch
        return self.ifsc

class debitcard:
    def __init__(self):
        self.__cardno=random.randint(1000000000000000,9999999999999999)
        self.__atmpin =random.randint(1000,9999)
    def get_cardno(self):
        return self.__cardno
    def get_atmpin(self):
        return self.__atmpin
    def setpin(self,atmpin):
        self.__atmpin=atmpin
        return self.__atmpin


class customer(bank,debitcard):
    def __init__(self,cname,accno,email,phone,balance,bankname,ifsc,branch):
        bank.__init__(self,bankname,branch,ifsc)
        debitcard.__init__(self)

        self.name=cname
        self.__accno=accno
        self.email=email
        self.phone=phone
        self.accbalance=balance



    def display(self):
        print('Ac Holder Name :',self.name,'\n Ac Number :',self.__accno,'\n Email :',self.email,'\n Phone',self.phone,'\n Balance:',self.accbalance
              ,'\n Bank',self.bankname,'\n ifsc Code',self.ifsc,'\n branch',self.branch)


cus1=customer('Rishan',123333,'sddd',12333,12344,'dddd',5678,'dfff')
cus1.display()
print(cus1.get_atmpin())
print(cus1.get_cardno())
cus1.setpin(3234)
print(cus1.get_atmpin())




