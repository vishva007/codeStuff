def primefactors(n):
    pfs = []
    for i in range(2,n+1):
        if n % i == 0:
            print ("appending " + str(i) )
            pfs.append(i)
            while n%i == 0:
                n = n/i
    return pfs

if __name__ == '__main__':
    a = int(input("Find Prime Factor's of"))
    print (primefactors(a))