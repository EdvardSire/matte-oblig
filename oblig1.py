import numpy as np


def fixpoint(x):
    prev, i = 0, 0
    while (x != prev):
        i += 1
        prev = x
        x = np.cos(x)
    return x, i-1


def newton(x):
    prev, i = 0, 0
    while (x != prev):
        i += 1
        prev = x
        x = x - (np.cos(x) - x)/(-np.sin(x) - 1)
    return x, i-1


def current(x):
    prev, i = 0, 0
    q = 1.60217663e-19
    k = 1.380649e-23
    T = 300
    while (x != prev):
        i += 1
        prev = x
        x = 1-(k*T*np.log(x+1))/q
    return x, i-1


f = fixpoint(1)
n = newton(1)
print(f'Fixpoint: {f}')
print(f'Newton: {n}')
print(f'Newton - Fixpoint: {n[0] - f[0]}')
print(f'Newton == Fixpoint: {n[0] == f[0]}')
print(f'Current: {current(1)}')
