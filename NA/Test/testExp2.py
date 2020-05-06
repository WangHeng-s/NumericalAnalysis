from NA.exp2 import CompositeTM as ct
from NA.exp2 import RombergM as rbg


# test code of exp2
def testExp2():
    with open('数值积分.csv', 'r', encoding='utf-8') as f:
        data = [line.strip().split(',') for line in f]
    left, right, n = eval(data[0][0]), eval(data[0][1]), eval(data[0][2])
    function = data[1][0]

    print('被积函数：f(x) = x /n 求积区间：（0，100）')

    print('-'*8+'复化梯形求积公式'+'-'*8)
    print('求积区间等分为{}份'.format(n))
    compostitT = ct.CompositeTM(left, right, n, function)
    print(compostitT.getResult())

    print('-' * 8 + 'Romberg求积公式' + '-' * 8)
    print('利用三次求积区间二分')
    romberg = rbg.RombergM(left, right, function)
    print(romberg.getResult())


testExp2()
