# CMPT 120 - Lab #6
# JOEY LORUSSO
# 25-10-2018
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', 'power' and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()

        def getNums():
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))

            return num1, num2
        
        if cmd == "add":
            num1, num2 = getNums()
            result = num1 + num2
        elif cmd == "sub":
            num1, num2 = getNums()
            result = num1 - num2
        elif cmd == "mult":
            num1, num2 = getNums()
            result = num1 * num2
        elif cmd == "div":
            num1, num2 = getNums()
            
            try:
                frac = num1/num2
            except:
                print("Unable to divide by 0")
                frac=0
                num1, num2 = getNums()
                                    
            result = num1 // num2
        elif cmd == "power":
            num1, num2 = getNums()
            result = num1 ** num2
        elif cmd == "quit":
            break
        else:
            print(cmd, "is an invalid command")
            continue

        print("The result is " + str(result) + ".\n")
    
def main():
    showIntro() #This looks good
    doLoop()
    showOutro()

main()
