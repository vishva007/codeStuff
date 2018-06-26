def fibo(n):
    ''' returns Nth Fibonacci'''
    print ("calling fibo of " + str(n))
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def allfibotill(n):
    ''' loop of all fibonacci till fibo(n) '''
    for i in range(0,n):
        print (fibo(i))

def arrayfibo(n):
    ''' use an array than recursion '''
    fibo = []
    fibo.append(1)
    fibo.append(1)
    cur = 2
    while n-2 > 0:
        fibo.append(fibo[cur-1] + fibo[cur - 2])
        cur = cur + 1
        n = n - 1    
    print (fibo)


if __name__ == "__main__":
    a = int(input('Calculate the _____th Fibonacci ?'))
    print (fibo(a))