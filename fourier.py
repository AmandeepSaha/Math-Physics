import numpy as np
import matplotlib.pyplot as plt


class Fourier:
    def __init__(self):
        self.n = int(input("n-th term:\t"))
        self.dx = 0.01

    def data_points(self):
        self.x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        self.y = np.arctan(self.x)
        self.a_0 = np.cumsum(self.y)*dx / np.pi
        self.a_n = lambda n: np.cumsum(self.y * np.cos(n * self.x))*dx / np.pi
        self.b_n = lambda n: np.cumsum(self.y * np.sin(n * self.x))*dx / np.pi

    def terms(self, n):
        self.data_points()
        self.fixed_term = self.a_0[-1] / 2
        self.changable_term = self.a_n(n)[-1] * np.cos(n * self.x) + self.b_n(n)[
            -1
        ] * np.sin(n * self.x)

    def draw_series(self):
        self.terms(1)
        self.whole_series = self.fixed_term + self.changable_term
        plt.plot(np.linspace(-2 * np.pi, 2 * np.pi, 1000), self.whole_series)
        for i in range(2, self.n + 2):
            plt.clf()
            plt.title(r"Fourier Series of $f(x)\:=\:x$")
            plt.xlabel(r"$x\longrightarrow$")
            plt.ylabel(r"$f(x)\longrightarrow$")
            self.terms(i)
            self.whole_series += self.changable_term
            plt.plot(np.linspace(-2 * np.pi, 2 * np.pi, 1000), self.whole_series)
            plt.pause(0.1)
        plt.show()


Fourier().draw_series()
