import matplotlib.pyplot as plt
import numpy as np


class Circle:
    def __init__(self, x0=complex(0), rad=1):
        self._rad = rad
        self._x0 = x0

    def in_line(self, x):
        return (self._x0.real - x.real)**2 + (self._x0.imag - x.imag)**2 == self._rad**2

    def get_centre(self):
        return self._x0

    def get_rad(self):
        return self._rad

    @classmethod
    def three_points_circle(self, z1, z2, z3):
        m_a = (z2.imag - z1.imag)/(z2.real - z1.real)
        m_b = (z3.imag - z2.imag)/(z3.real - z2.real)
        print(z1, z2, z3, m_a, m_b)
        x_0 = (m_a*m_b*(z1.imag - z3.imag) + m_b*(z1.real + z2.real) - m_a*(z2.real + z3.real))/(2*(m_b - m_a))
        if m_a != 0:
            y_0 = (-1/m_a) * (x_0 - (z1.real + z2.real)/2) + (z1.imag + z2.imag)/2
        else:
            y_0 = 0
        centre = complex(x_0, y_0)
        rad = np.sqrt((z1.real - x_0)**2 + (z1.imag - y_0)**2)
        return Circle(centre, rad)

    def plot(self):
        c = plt.Circle((self._x0.real, self._x0.imag), self._rad, fill=False)
        fig, ax = plt.subplots()
        plt.grid(linestyle='--')
        ax.set_aspect(1)
        plt.xlim(-(self.get_centre().real+self.get_rad()+3), self.get_centre().real+self.get_rad()+3)
        plt.ylim(-(self.get_centre().imag+self.get_rad()+3), self.get_centre().imag+self.get_rad()+3)
        return ax.add_artist(c)
