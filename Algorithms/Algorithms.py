
class recursiveformulas:
    def recursivesum(N):
            if N==1:
                return 1
            else:
                return N+recursiveformulas.recursivesum(N-1)

    def tail(n):
        if n==0:
            return n
        print(n)
        recursiveformulas.tail(n-1)


    def head(n):
        if n==0:
            return n
        recursiveformulas.head(n-1)
        print(n)


    def factorial(n):
        if n==1:
            return 1
        return n*recursiveformulas.factorial(n-1)

    def fibonacci(n):
        if n==0: return 0
        if n==1: return 1
        fib1= recursiveformulas.fibonacci(n-1)
        fib2= recursiveformulas.fibonacci(n-2)
        res=fib1+fib2

        return res

    def hanoi(n,rod_from,rod_middle,rod_to):

        if n==1:
            print("plate 1 from %s to %s"%(rod_from,rod_to))
            return

        recursiveformulas.hanoi(n-1,rod_from,rod_to,rod_middle)
        print("plate %s from %s to %s"%(n,rod_from,rod_to))

        recursiveformulas.hanoi(n-1,rod_middle,rod_from,rod_to)

    def binary(array, item, left, right):
        if right<left:
            return -1;
        middle= left+(right-left)//2
        print("middle index: %s"%(middle))

        if array[middle]==item:
            return middle

        elif array[middle]>item:
            print("Checking items on the left...")
            return recursiveformulas.binary(array, item, left, middle-1)
        
        elif array[middle]<item:
            print("Checking items on the right...")
            return recursiveformulas.binary(array, item, middle+1, right)

    
if __name__ == "__main__":
    #re=recursivesum(2)
    print(recursiveformulas.binary([1,4,5,6,7,8,9,10,11], 11, 0, 7))

