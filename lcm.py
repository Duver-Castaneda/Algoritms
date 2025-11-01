def lcm(a, b):
     current_gcd = 1
     mult = a * b
     for d in range(1, min(a,b)):
         r = int(a % b)
         a = b
         b = r

       
             
         if b == 0:
             current_gcd = a
             break

     return int(mult / current_gcd)

    


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

