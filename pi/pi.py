import decimal
import time
import math

decimalPoint =100
# Reference https://docs.python.org/3/library/decimal.html#recipes
def pi():
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s               # unary plus applies the new precision


happyText= """                                                 
   @@   @@     @@@@      @@@@@@  @@@@@@@ @@   @@                
   @@   @@    @@  @@     @@   @@ @@   @@  @@ @@                 
   @@@@@@@   @@@@@@@@    @@  @@@ @@@ @@@   @@@                  
   @@   @@  @@      @@   @@      @@        @@             
   """

pieText= """
    @@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@
@     @(    @@,    
     ,@    .@@     
    ,@@    @@@     
   .@@@    @@@     @
  @@@@*     @@@@@@@
 """
dayText="""
   @@@@@@@     @@@@   @@@  @@                               
   @@   @@@   @@  @@    @@@@                                
   @@   @@@  @@@@@@@     @@                                 
   @@@@@@@  @@     @@   @@ 
"""

print(happyText)
time.sleep(1)

print(pieText)

time.sleep(1)
print(dayText)

print("To what decimal point do you want pi?")
decimalInput = input(">")
decimalInput = int(decimalInput) + 1
decimal.getcontext().prec = decimalInput

pi = pi()

print(decimalInput)
print(pi)
