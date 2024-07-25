class Shopping_cart:
    def _init_(self, items, price) :
        self.items=items
        self.price=price
    def addingElements(self,elements) :
        self.items+=elements
    def removing(self, elements) :
        self.items-=elements
    def calculating_total_price(self) :
        return self.price*self.items
Obj=Shopping_cart(5,20) 
Obj.addingElements(4) 
Obj.removing(2) 
print(Obj.calculating_total_price() ) 

