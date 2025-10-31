def gcd(a, b):
     current_gcd = 1
    
    #  if a % 2 == 0 and b % 2 == 0:
    #      for d in range(2, min(a, b) + 1, 2):
    #          if a % d == 0 and b % d == 0:
    #              if d > current_gcd:
    #                  current_gcd = d
             
    #  if a % 2 != 0 and b % 2 != 0:
    #      for d in range(3, min(a, b) + 1, 2):
    #          if a % d == 0 and b % d == 0:
    #              if d > current_gcd:
    #                  current_gcd = d
    #  if a % 2 != 0 and b % 2 == 0 or a % 2 == 0 and b % 2 != 0:
    #      if a % 5 == 0 and b % 5 == 0:
    #         current_gcd = 5
         
       
   




     for d in range(1, min(a,b)):
        
         r = int(a % b)
         a = b
         b = r

       
             
         if b == 0:
             current_gcd = a
             break
             
         

       
         
     return current_gcd


if __name__ == "__main__":
     a, b = map(int, input().split())
     print(gcd(a, b))
