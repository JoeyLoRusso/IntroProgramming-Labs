# Fibonacci Project
# By Joey LoRusso

def main():
    count=int(input("Enter a number: "))-1
    # Create the first 2 numbers in the Fibonacci sequence
    n1 = 0
    n2 = 1

    for i in range(count):
        n3=n1+n2
        n1=n2
        n2=n3

    print(n3)

    
main()
