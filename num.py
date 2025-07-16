import math
x = -2.9
print(abs(x))
e=10
num1=2+3j
num2=complex(3,4)
print(num2.real,num2.imag)
print(round(5.55))
print(round(5.67,1))#it show the one number after a decimal
from enum import Enum
class State(Enum):
    INACTIVE=0
    ACTIVE=1
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE' ])

#enum is readable name that bound with constant value fixed the value all over the code and 
#do not change