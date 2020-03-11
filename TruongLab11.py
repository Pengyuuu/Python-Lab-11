'''
    Name: Eric Truong
    ID: 018149311
    Instructor: Minhthong Nguyen
    Date: November 30, 2018
'''
import random

def partOne():
    seriesOne = []
    x = 0
    while x < 20:
        serial = int(input('Enter a number: '))
        seriesOne.append(serial)
        x += 1
    print(seriesOne)
    print('Highest number:', max(seriesOne))
    print('Lowest number:', min(seriesOne))
    total = 0
    for value in seriesOne:
          total += value
    avg = total / len(seriesOne)
    print('Total:', total)
    print('Average:', avg)

def partTwo():
    lottery = []
    x = 0
    while x < 7:
        random.seed()
        rand = random.randint(0, 7)
        lottery.append(rand)
        x += 1
    for n in lottery:
        print(n)
    

def main():
    partOne()
    partTwo()
    
main()
