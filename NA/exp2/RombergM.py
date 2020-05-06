import numpy as np
from NA.Test import Function as f
from NA.exp2 import CompositeTM as CT


# Romberg公式求积分
class RombergM:
    __left: float
    __right: float  # 求积区间
    __function: f.Function  # 被积函数

    def __init__(self, l, r, fchoice):
        self.__left = l
        self.__right = r
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

    # 积分值
    def getResult(self):
        l = self.__left
        r = self.__right
        n = [1, 2, 4, 8]  # 二分0，1，2，3次对应复化梯形求积等分为1，2，4，8份
        ct = CT.CompositeTM(l, r, 1, self.__function.getChoice())
        t = []  # 梯形公式二分的结果Tn
        for i in n:
            ct.setn(i)
            t.append(ct.getResult())
        s = []  # Sn
        for i in range(3):
            temp = (t[i+1] * 4 / 3) - (t[i] / 3)
            s.append(temp)
        c = []  # Cn
        for i in range(2):
            temp = (s[i + 1] * 16 / 15) - (s[i] / 15)
            c.append(temp)
        r = (c[1] * 64 / 63) - (c[0] / 63)  # R1
        return r
