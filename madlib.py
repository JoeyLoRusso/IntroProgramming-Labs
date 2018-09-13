def promptForWords():
    global place, noun, name, verb, noun2
    place=input("Enter a place: ")
    noun=input("Enter a noun: ")
    name=input("Enter a name: ")
    verb=input("Enter a verb: ")
    noun2=input("Enter another noun: ")

def makeAndPrintSentence():
    print("Tim ran to the "+place+" to see the "+noun+". When he arived, he saw his friend, "+name+". They said, 'Tim! "+verb+" to the store, they are having a sale on "+noun2+".'")


def main():
    promptForWords()
    makeAndPrintSentence()

main()
