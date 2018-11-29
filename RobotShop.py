class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

products = [ Product("Ultrasonic range finder", 2.50, 4),
             Product("Servo motor", 14.99, 10),
             Product("Servo controller", 44.95, 5),
             Product("Microcontroller board", 34.95, 7),
             Product("Laser range finder", 149.99, 2),
             Product("Lithium polymer battery", 8.99, 8)]

#productNames = [ "Ultrasonic range finder",
#                 "Servo controller", 
#                 "Servo motor",
#                 "Microcontroller board"
#                 "Laser range finder",
#                 "Lithium polymer battery"]
#
#productPrices = [2.50, 14.99, 44.95, 34.95, 149.99, 8.99]
#productQuantities = [4, 10, 5, 7, 2, 8]


def printStock():
    print()
    print("Available Products:")
    print("-------------------")
    for i in range(0,len(productNames)):
        if productQuantities[i] > 0:
            print(str(i)+")", productNames[i], "$", productPrices[i])
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and Quantity you wish to buy: ").split(" ")

        if vals[0] == "quit":
            break

        prodId = int(vals[0])
        count = int(vals[1])

        if productQuantities[prodId] >= count:
            if cash >= productPrices[prodId] * count:
                productQuantities[prodId] * count
                cash -= productPrices[prodId] *count
                print("You purchased", count, productNames[prodId]+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you can not afford that.")
        else:
            print("Sorry, we are sold out of", productNames[prodId])

main()
