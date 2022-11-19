#y=tg0.5x/x^3+7.5   0.1<=x<=1.2     ~x=0.1
import math
print("-----------------")
print("|   X      Y    |")
print("-----------------")
x=0.1
while (x < 1.21):
    print("|  {:.1f}   {:.3f}  |".format(x, (math.tan(0.5)*x)/((x**3)+7.5)))
    x += 0.1
print("-----------------")
