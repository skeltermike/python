class Fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def onyesha(self):
        print(f"My favourite fruit is  {self.name} "
              f"and it costs ksh . {self.price} "
              f"and it is  in  {self.color}")


myobj = Fruits("Apples", 60, color="green or red color")
myobj.onyesha()
myobj2= Fruits(name="Banana",price=50,color="yellow colour")
myobj3= Fruits(name="Strawberry",price=50,color="red colour")
myobj2.onyesha()
myobj3.onyesha()