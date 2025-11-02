from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    ValorPorUnidad = []
    ValorOrdenado =  []
 
    for i in range(len(values)):
        ValorPorUnidad.append(values[i] / weights[i]) 
        
    
    MejorValor = max(ValorPorUnidad)
    posicion = ValorPorUnidad.index(MejorValor)
    print(posicion)
    print(MejorValor)
    while capacity > 0:
        if weights[posicion] <= capacity:
            capacity = capacity - weights[posicion]
            value = (value + MejorValor) * weights[posicion]
            print(value)

    
    
    


    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    #  print("{:.10f}".format(opt_value))
   
