import matplotlib.pyplot as plt


class Line:
    def __init__(self, a=complex(0), b=complex(0)):
        self._a = a
        self._b = b

    def set_new_a_b(self, new_a, new_b):
        self._a = new_a
        self._b = new_b

    def start(self):
        return self._a

    def end(self):
        return self._b

    def in_line(self, x0):
        return ((self._a.imag-self._b.imag)*x0.real + (self._b.real - self._a.real)*x0.imag +
                (self._a.real*self._b.imag - self._b.real*self._a.imag) == 0)

    def plot(self):
        ax = plt.subplot()
        plt.grid(linestyle='-')
        ax.set_aspect(1)
        x_short = (self._a.real, self._b.real)
        y_short = (self._a.imag, self._b.imag)
        return ax.plot(x_short, y_short)
