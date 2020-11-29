{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "middle index: 3\nChecking items on the right...\nmiddle index: 5\nChecking items on the right...\nmiddle index: 6\nChecking items on the right...\nmiddle index: 7\nChecking items on the right...\n-1\n"
     ]
    }
   ],
   "source": [
    "\n",
    "class recursiveformulas:\n",
    "    def recursivesum(N):\n",
    "            if N==1:\n",
    "                return 1\n",
    "            else:\n",
    "                return N+recursiveformulas.recursivesum(N-1)\n",
    "\n",
    "    def tail(n):\n",
    "        if n==0:\n",
    "            return n\n",
    "        print(n)\n",
    "        recursiveformulas.tail(n-1)\n",
    "\n",
    "\n",
    "    def head(n):\n",
    "        if n==0:\n",
    "            return n\n",
    "        recursiveformulas.head(n-1)\n",
    "        print(n)\n",
    "\n",
    "\n",
    "    def factorial(n):\n",
    "        if n==1:\n",
    "            return 1\n",
    "        return n*recursiveformulas.factorial(n-1)\n",
    "\n",
    "    def fibonacci(n):\n",
    "        if n==0: return 0\n",
    "        if n==1: return 1\n",
    "        fib1= recursiveformulas.fibonacci(n-1)\n",
    "        fib2= recursiveformulas.fibonacci(n-2)\n",
    "        res=fib1+fib2\n",
    "\n",
    "        return res\n",
    "\n",
    "    def hanoi(n,rod_from,rod_middle,rod_to):\n",
    "\n",
    "        if n==1:\n",
    "            print(\"plate 1 from %s to %s\"%(rod_from,rod_to))\n",
    "            return\n",
    "\n",
    "        recursiveformulas.hanoi(n-1,rod_from,rod_to,rod_middle)\n",
    "        print(\"plate %s from %s to %s\"%(n,rod_from,rod_to))\n",
    "\n",
    "        recursiveformulas.hanoi(n-1,rod_middle,rod_from,rod_to)\n",
    "\n",
    "    def binary(array, item, left, right):\n",
    "        if right<left:\n",
    "            return -1;\n",
    "        middle= left+(right-left)//2\n",
    "        print(\"middle index: %s\"%(middle))\n",
    "\n",
    "        if array[middle]==item:\n",
    "            return middle\n",
    "\n",
    "        elif array[middle]>item:\n",
    "            print(\"Checking items on the left...\")\n",
    "            return recursiveformulas.binary(array, item, left, middle-1)\n",
    "        \n",
    "        elif array[middle]<item:\n",
    "            print(\"Checking items on the right...\")\n",
    "            return recursiveformulas.binary(array, item, middle+1, right)\n",
    "\n",
    "    \n",
    "if __name__ == \"__main__\":    #re=recursivesum(2)\n",
    "    print(recursiveformulas.binary([1,4,5,6,7,8,9,10,11], 11, 0, 7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}