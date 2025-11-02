def change(money):
    # write your code here

    denominaciones = [1,5,10]
    usados = 0
    while money > 0:
         if denominaciones[2] <= money:
             usados = usados + 1
             money = money - denominaciones[2]
         elif denominaciones[1] <= money:
             usados = usados + 1
             money = money - denominaciones[1]
         else: 
             usados = usados + 1
             money = money - denominaciones[0]
              


        

    return usados


if __name__ == '__main__':
    m = int(input())
    print(change(m))
