import math


# 函数类
class Function:
    __choice: str  # 选择器
    __arg1 = [1, 0]  # f1(x)参数
    __arg2 = [1, 0, 0]
    __arg3 = [1, 1]

    def __init__(self, choice='linear'):  # 默认一次函数
        self.__choice = choice

    # 一次函数 f(x) = a * x + b  choice = 'linear'/'1'
    def f1(self, x0):
        a = self.__arg1[:]
        return a[0] * x0 + a[1]

    # 二次函数 f(x) = a * (x**2) + b * x + c  choice = 'quadratic'/'q'
    def f2(self, x0):
        a = self.__arg2[:]
        return a[0] * (x0**2) + a[1] * x0 + a[2]

    # f(x) = a * sin(b*x)  choice = 'sin'
    def f3(self, x0):
        a = self.__arg3[:]
        return a[0] * math.sin(a[1] * x0)

    # f(x, y) = y - 2 * x / y  choice = 'f4'
    def f4(self, x0, y0):
        return y0 - 2 * x0 / y0

    # f(x) = sin(x)/x  choice = 'f5'
    def f5(self, x0):
        if x0 != 0:
            return math.sin(x0) / x0
        else:
            return 1

    # 返回函数值（一元函数）
    def fx(self, x0):
        ch = self.__choice
        if ch == 'linear' or ch == 'l':
            return self.f1(x0)
        elif ch == 'quadratic' or ch == 'q':
            return self.f2(x0)
        elif ch == 'sin':
            return self.f3(x0)
        elif ch == 'f5':
            return self.f5(x0)

    # 返回函数值（二元函数）
    def fxy(self, x0, y0):
        return self.f4(x0, y0)

    # 设置参数
    def setArgs(self, args: list):
        ch = self.__choice
        if ch == 'linear' or ch == 'l':
            self.__arg1 = args[:]
        elif ch == 'quadratic' or ch == 'q':
            self.__arg2 = args[:]
        elif ch == 'sin':
            self.__arg3 = args[:]

    # 修改选择器
    def setChoice(self, fchoice):
        self.__choice = fchoice

    # 获取选择器
    def getChoice(self):
        return self.__choice
