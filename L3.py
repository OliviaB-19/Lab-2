import math

a=math.tan(math.pi/4)
numerator=math.sqrt(a+1)

b=math.tan(math.pi/3)
denominator=math.sqrt(b+math.sin(math.pi/3))
value=numerator/denominator
print(value)
