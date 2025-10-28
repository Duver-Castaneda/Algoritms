


Range = input()
entrada = input()
Numbers = list(map(int, entrada.split()))


result1 = 0
index = 0
for i in Numbers:
   if i > result1:
     result1 = i

Numbers.remove(result1)  


result2 = 0
for i in Numbers:
   if i > result2:
     result2 = i



print(result1 * result2)





