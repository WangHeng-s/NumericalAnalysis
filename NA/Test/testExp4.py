from NA.exp4 import SecantM as sct
from NA.exp4 import NewtonLM as nl
from NA.exp4 import Dichotomy as d


# test code of Exp4
def testExp4():
    print('-'*8 + "Dichotomy Method" + '-'*8)

    dm = d.Dichotomy(-1, 5, 0.001, 'l')

    dm.setArgs([2, 1])
    print('方程：2 * x + 1 = 0, 精度：0.001')
    print(dm.getResult())

    dm.setp(0.000001)
    print('方程：2 * x + 1 = 0, 精度：0.000001')
    print(dm.getResult())

    dm.setfx('q')
    dm.setArgs([1, -4, 3])
    dm.setRange(-1, 2)
    print('方程：x**2 - 4 * x + 3 = 0, 精度：0.000001, 寻根区间[-1, 2]')
    print(dm.getResult())

    print('-' * 8 + "Newton iteration Method" + '-' * 8)

    nlm = nl.NewtonLM(0, 'q', 'l')

    nlm.setfxArgs([1, -4, 3])
    nlm.setfdxArgs([2, -4])
    nlm.setTimes(2)
    print('方程：x**2 - 4 * x + 3 = 0, 初始迭代点: 0, 迭代2次')
    print(nlm.getResult())

    nlm.setx0(-1)
    nlm.setTimes(4)
    print('方程：x**2 - 4 * x + 3 = 0, 初始迭代点: -1, 迭代4次')
    print(nlm.getResult())

    print('-' * 8 + "Secant Method" + '-' * 8)

    sctm = sct.SecantM(-1, 0, 'q')

    sctm.setArgs([1, -4, 3])
    print('方程：x**2 - 4 * x + 3 = 0, 初始迭代点: 0, -1, 迭代5次')
    print(sctm.getResult())

    sctm.setTimes(3)
    sctm.setx(0.5, 0)
    print('方程：x**2 - 4 * x + 3 = 0, 初始迭代点: 0.5, 0, 迭代3次')
    print(sctm.getResult())


testExp4()
