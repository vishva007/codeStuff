import random
import math

def getpi():
    ''' area of a 1*1 square / area of a quarter circle = 4/pi'''
    incircle = 0
    total = 0
    while True:
        total = total + 1
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            incircle = incircle + 1
        
        ratio = incircle/total
        if total%1000000 == 0:
            print (str(4*ratio) + ":" + str(total))


if __name__ == '__main__':
    getpi()