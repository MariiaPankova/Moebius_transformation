from Circle import *
from Line import *


class DLFunc:
    def __init__(self, a=0, b=0, c=0, d=0):
        assert a*d - b*c != 0, "Wrong args"
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def __call__(self, obj):
        if isinstance(obj, Line):
            if obj.in_line(complex(-self._d/self._c)) if self._c != 0 else True:
                if obj.start() != complex(-self._d/self._c) and obj.end() != complex(-self._d/self._c) if self._c != 0 else True:
                    return Line(self.point_call(obj.start()), self.point_call(obj.end()))
                elif obj.start() == complex(-self._d/self._c) or obj.end() == complex(-self._d/self._c):
                    return Line(self.point_call((obj.end() - obj.start())/2),
                                self.point_call((obj.end() - obj.start())*10))
            elif not obj.in_line(complex(-self._d/self._c)) if self._c != 0 else False:
                return Circle.three_points_circle(self.point_call(obj.start()), self.point_call(obj.end()),
                                                  self.point_call(obj.end()-obj.start()))
        elif isinstance(obj, Circle):
            if obj.in_line(complex(-self._d/self._c)) if self._c != 0 else False:
                if obj.get_centre()+obj.get_rad() == complex(-self._d/self._c) \
                        or obj.get_centre()-obj.get_rad() == complex(-self._d/self._c) if self._c != 0 else True:
                    return Line(self.point_call(obj.get_centre() + complex(0, obj.get_rad())),
                                self.point_call(obj.get_centre() - complex(0, obj.get_rad())))

                return Line(self.point_call(obj.get_centre()+obj.get_rad()),
                            self.point_call(obj.get_centre()-obj.get_rad()))

            elif not obj.in_line(complex(-self._d/self._c)) if self._c != 0 else True:
                return Circle.three_points_circle(self.point_call(obj.get_centre() + obj.get_rad()),
                                                  self.point_call(obj.get_centre() - obj.get_rad()),
                                                  self.point_call(obj.get_centre() + complex(0, obj.get_rad())))
        else:
            self.point_call(obj)

    def point_call(self, obj):
        return (self._a * obj + self._b)/(self._c * obj + self._d)



if __name__ == '__main__':
    a = complex(0, 0)
    b = complex(1, 1)
    #c = Line(a, b)
    c = Circle(a, 3)
    fun = DLFunc(0, 1, 1, 0)
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    #print(fun(c).end(), fun(c).start())
    c.plot()
    fun(c).plot()
    plt.show()
