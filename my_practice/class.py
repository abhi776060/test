class Payment:
    def __init__(self,price):
        self.__final_price=price

    def get_final_price(self):
        return self.__final_price-0.05*self.__final_price

pay=Payment(10)
#print(pay.__final_price)
print(pay.get_final_price())