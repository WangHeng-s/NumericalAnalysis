import numpy as np
from NA.Test import Function as f


# 复化梯形求积
class CompositeTM:
    __left: float
    __right: float  # 求积区间
    __n: int  # 区间等分数 n >= 1
    __step: float  # 小区间步长
    __function: f.Function  # 被积函数

    def __init__(self, l, r, n, fchoice):
        self.__left = l
        self.__right = r
        self.__n = n
        self.__step = (r - l) / n
        self.__function = f.Function(fchoice)

    # 修改被积函数
    def setfx(self, fchoice):
        self.__function.setChoice(fchoice)

    # 修改被积函数参数
    def setArgs(self, args):
        self.__function.setArgs(args)

    # 修改求积区间
    def setRange(self, left, right):
        self.__left = left
        self.__right = right

    # 修改等分数
    def setn(self, n):
        self.__n = n
        self.__step = (self.__right - self.__left) / n

    # 积分值
    def getResult(self):
        l = self.__left
        r = self.__right
        h = self.__step
        temp = 0
        for i in np.arange(l + h, r, h):
            temp += self.__function.fx(i)
        result = h * (0.5 * self.__function.fx(l) + temp + 0.5 * self.__function.fx(r))
        return result
