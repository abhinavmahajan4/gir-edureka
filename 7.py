class Mobile:
    def __init__(self):
        print("inside constructor")
    def purchase(qty,self):
        print(id(qty))
        print(id(mob1))
mob1=Mobile()
mob1.purchase(2)
