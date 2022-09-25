import numpy as np
import matplotlib.pyplot as plt


def backwardsEuler(func, dfunc, tol):
    def f(v): return eval(func)
    def df(v): return eval(dfunc)
    start, stop, N = 0, 10, 100
    h = (stop - start)/(N)
    x = np.linspace(start, stop, N+1)
    y = np.zeros_like(x)

    for i in range(N):
        iterY, prev = y[i], 0
        while (abs(iterY - prev) > tol):
            prev = iterY
            iterY = iterY - (-iterY + y[i] + h*f(iterY))/(h*df(iterY)-1)

        y[i+1] = y[i] + h*f(iterY)

    return x, y


def naive(func):
    def f(v): return eval(func)
    start, stop, N = 0, 10, 100
    h = (stop - start)/(N)
    x = np.linspace(start, stop, N+1)
    y = np.zeros_like(x)

    for i in range(N):
        for _ in range(20):
            y[i+1] = y[i] + h*f(y[i+1])

    return x, y


if __name__ == "__main__":
    plt.plot(*backwardsEuler("1-v**2", "-2*v", 1e-14))
    plt.show()
