class calci:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return (self.a + self.b)
    def sub(self):
        return (self.a - self.b)
    def mul(self):
        return (self.a * self.b)
    def remainder(self):
        return (self.a % self.b)
    def div(self):
        return (self.a / self.b)

obj1=calci(9,5)
print(obj1.add())
