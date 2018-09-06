# CMPT 120L 113
# Mars Rover Program
# Author: Joey LoRusso
# Created 9/6/18

light = 186000 # miles/second
dist = 34000000 # distance from mars to earth

def main():
    time = dist/light
    print("It will take" , time , "seconds to recive a photo from the Curiosity rover.")

main()
