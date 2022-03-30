import random
import platform
from platform import python_version


x = random.random()
print(x)

y = random.randint(0, 50)
print(y)

j = platform.system()
p = python_version()
print(j)
print(p)
