from NA.exp1 import LagrangeM as Lg
from NA.exp1 import NewtonM as Nt
from NA.exp1 import LeastSquareM as Ls


# test method of Exp1
def testExp1():
    with open('插值数据.csv', 'r', encoding='utf-8') as f:  # 导入测试数据
        ls = [line.strip().split(',') for line in f]
    x = [eval(x) for x in ls[0]]
    y = [eval(y) for y in ls[1]]

    x0 = 4.44

    print('x:')
    for t in x:
        print(t, end=' ')
    print()
    print('y:')
    for t in y:
        print(t, end=' ')
    print()
    print('x0: {}'.format(x0))
    print('-' * 5 + 'Lagrange' + '-' * 5)
    lagrange = Lg.LagrangeM(x, y)
    print(lagrange.fx(x0))

    print('-' * 5 + 'Newton' + '-'*5)
    newton = Nt.NewtonM(x, y)
    print(newton.fx(x0))

    print('-' * 5 + 'LeastSquare' + '-' * 5)
    lsm = Ls.LeastSquareM(x, y)
    print(lsm.result())

    lagrange.paint()
    newton.paint()
    lsm.paint()


testExp1()
