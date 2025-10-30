def fibonacci_last_digit(n):
    Fibonacci = [0,1]

    for i in range(n):
        Fibonacci.insert(2, Fibonacci[1] + Fibonacci[0])
        del Fibonacci[:-2]
     
        
    Digito = Fibonacci[0]
    print(Digito)
    
    Ultimo = Digito % 10
    print(Ultimo)
    

    


if __name__ == '__main__':
    n = int(input())
    fibonacci_last_digit(n)
