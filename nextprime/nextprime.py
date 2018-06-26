primearray = [2,3]
def nextprime():
    start = primearray[len(primearray)-1] + 1
    current = start
    while True:
        found = True
        for i in primearray:
            if current % i == 0:
                found = False
                break
        if(found):
            primearray.append(current)
            return
        current = current + 1
        


if __name__ == '__main__':
    while True:
        a = input("Next Prime")
        if a == 'n':
            break
        else:
            nextprime()
            print (primearray[len(primearray)-1])