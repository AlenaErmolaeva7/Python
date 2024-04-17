def bank (x=int, y=int):
   for i in range(y):
    x = x + x * 0.1
   return x   

print (bank(1000,3))   
