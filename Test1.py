from DLFunc import *
from math import e, pi

i = complex(0, 1)
a = complex(2, 2)
b = complex(1, 0)
d1 = DLFunc(0, 1, 1, 0)
d2 = DLFunc(1, i, 1, -i)

line1 = Line(a, b)
circle1 = Circle(b, 1)

for obj in [circle1, line1]:
     obj.plot()
     d1(obj).plot()
     plt.show()

# plt.scatter([a.real], [a.imag], )
# plt.scatter(d1.point_call(a).real, d1.point_call(a).imag)
# plt.show()

