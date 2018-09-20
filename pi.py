import math

def main():
    count=int(input("Enter a number: "))
    denominator=3
    answer=4
    minus=True
    
    for i in range(count):
        if minus==True:
            answer-=4/denominator
            denominator+=2
            minus=False
        else:
            answer+=4/denominator
            denominator+=2
            minus=True

    print(answer)
    

main()
