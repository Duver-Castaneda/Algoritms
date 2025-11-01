import math
import numpy as np

def fibonacci_huge_naive(n, m):
   
     Fibonacci = [0,1]
     pi = math.pi
     print(pi)

     A = np.array([[1,1],[1,0]])
     A2 = A @ A
     for d in range(n):
         A2 = (A2 @ A) 
     print(A2)
    #  for i in range(n):
    #       Fibonacci.insert(2, (Fibonacci[1] + Fibonacci[0]) % m) 
        
    #       del Fibonacci[:-2]
    

     #return Fibonacci[0] 
      
     



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
