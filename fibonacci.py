def fibonacci_number(n):
    Fibonacci = [0, 1, 1]
  
    for i in range(2, n + 1):
        l = Fibonacci[i-1] + Fibonacci[i-2]
        Fibonacci.append(l)
     
    print(Fibonacci[n])
   
   

    


    



if __name__ == '__main__':
    input_n = int(input())
    fibonacci_number(input_n)
