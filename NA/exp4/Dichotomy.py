from NA.Test import Function as F


# 二分法求解方程 f(x) = 0 的根
class Dichotomy:
    __function: F.Function
    __p: float  # precision，精度
    __left: float
    __right: float  # 初始求解区间
    __result: float  # 结果

    def __init__(self, left, right, p, fchoice):
        self.__left = left
        self.__right = right
        self.__p = p
        self.__function = F.Function(fchoice)

    # 计算结果
    def __do(self):
        left = self.__left
        right = self.__right
        p = self.__p
        f = self.__function
        mx = (left + right) / 2  # 区间中点
        r = (f.fx(mx) * f.fx(left))  # 左端与中间的函数值乘积
        while r != 0:
            if (right - left) <= p:
                break
            if r > 0:
                left = mx
            else:
                right = mx
            mx = (left + right) / 2
            r = (f.fx(mx) * f.fx(left))
        self.__result = mx

    # 修改精度
    def setp(self, p):
        self.__p = p

    # 修改寻解区间
    def setRange(self, left, right):
        self.__left = left
        self.__right = right

    # 修改要求零点的函数
    def setfx(self, fchoice):
        self.__function.setChoice(fchoice)

    # 修改函数参数
    def setArgs(self, args):
        self.__function.setArgs(args)

    # 返回结果
    def getResult(self):
        self.__do()
        return self.__result
