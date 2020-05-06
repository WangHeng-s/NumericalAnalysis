from NA.Test import Function as F


# 用弦截法求f(x) = 0 的根
class SecantM:
    __function: F.Function  # f(x)
    __x0: float
    __x1: float  # 开始值
    __times = 5  # 迭代次数，默认为5
    __result: float  # 结果

    def __init__(self, x0, x1, fchoice):
        self.__x0 = x0
        self.__x1 = x1
        self.__function = F.Function(fchoice)

    # 计算结果
    def __do(self):
        xkb = self.__x0  # Xk-1
        xk = self.__x1  # Xk
        f = self.__function
        for i in range(self.__times):
            temp = xk
            xk = xk - f.fx(xk) / (f.fx(xk) - f.fx(xkb)) * (xk - xkb)
            if temp == xk:
                break
        self.__result = xk

    # 修改x0, x1
    def setx(self, x0, x1):
        self.__x0 = x0
        self.__x1 = x1

    # 修改迭代次数
    def setTimes(self, times):
        self.__times = times

    # 修改要求零点的函数: f(x)
    def setfx(self, fchoice):
        self.__function.setChoice(fchoice)

    # 修改f(x)参数
    def setArgs(self, args):
        self.__function.setArgs(args)

    # 返回结果
    def getResult(self):
        self.__do()
        return self.__result
