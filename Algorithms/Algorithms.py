class recursiveformulas:
    def __init__(Self,name,age):
         Self.name=name
         Self.age=age

    def printparameter(self):
        print(self.name,self.age)

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
            return -1
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
    


class algo_sort:
    def __init__(self, array1=[]):
        self.array1 = array1

    def sortinsertasc(self):
        A = self.array1[:]  # Create a copy of the list
        if len(A) <= 1:
            return A
        else:
            for i in range(1, len(A)):
                key = A[i]
                j = i - 1
                while j >= 0 and key < A[j]:
                    A[j + 1] = A[j]
                    j -= 1
                A[j + 1] = key
            return A

    def sortinsertdsc(self):
        B = self.array1[:]  # Create a copy of the list
        if len(B) <= 1:
            return B
        else:
            for i in range(1, len(B)):
                key = B[i]
                j = i - 1
                while j >= 0 and key > B[j]:
                    B[j + 1] = B[j]
                    j -= 1
                B[j + 1] = key
            return B

if __name__ == "__main__": 
    algo_sort_instance = algo_sort([5, 2, 9, 1, 5, 6])
    print("Initial array:", algo_sort_instance.array1)  # Debugging

    sorted_array_asc = algo_sort_instance.sortinsertasc()
    print("Sorted array in ascending order:", sorted_array_asc)

    sorted_array_dsc = algo_sort_instance.sortinsertdsc()
    print("Sorted array in descending order:", sorted_array_dsc)
