def fibonacci_number(n):
    Fibonacci = []
    Fibonacci.insert(0, 0)
    Fibonacci.insert(1, 1)
    Fibonacci.insert(2, 0)
  
    for i in range(2, n + 1):
 
  
        l = Fibonacci[i-1] + Fibonacci[i-2]
        Fibonacci.insert(i, l)
     
    print(Fibonacci[n])
   
   

    


    



if __name__ == '__main__':
    input_n = int(input())
    fibonacci_number(input_n)
