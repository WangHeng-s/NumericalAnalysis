from NA.exp3 import EulerM as el
from NA.exp3 import RungeKuttaM as rk


# test code of Exp3
def testExp3():
    print('-'*8 + "The Improved Euler Method" + '-'*8)

    euler = el.EulerM(0, 1, 'f4')

    ls = euler.getResult()
    for t in ls:
        print('{:.2f}: {:.4f}'.format(t[0], t[1]))

    print('-' * 8 + "Runge-Kutta Method" + '-' * 8)

    rungekutta = rk.RungeKuttaM(0, 1, 'f4')

    ls = rungekutta.getResult()
    for t in ls:
        print('{:.2f}: {:.4f}'.format(t[0], t[1]))


testExp3()
