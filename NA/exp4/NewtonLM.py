from NA.Test import Function as F


# 牛顿迭代法求解 f(x) = 0 在x0附近的根
class NewtonLM:
    __function: F.Function  # f(x)
    __functionD: F.Function  # f'(x)
    __x0: float  # 初始迭代点
    __times = 5  # 迭代次数，默认为5
    __result: float  # 结果

    def __init__(self, x0, fchoice, fdchoice):
        self.__x0 = x0
        self.__function = F.Function(fchoice)
        self.__functionD = F.Function(fdchoice)

    # 计算结果
    def __do(self):
        xk = self.__x0
        f = self.__function
        fd = self.__functionD
        for i in range(self.__times):
            temp = xk
            xk = xk - f.fx(xk) / fd.fx(xk)
            if temp == xk:
                break
        self.__result = xk

    # 修改x0
    def setx0(self, x0):
        self.__x0 = x0

    # 修改迭代次数
    def setTimes(self, times):
        self.__times = times

    # 修改要求零点的函数: f(x)
    def setfx(self, fchoice):
        self.__function.setChoice(fchoice)

    # 修改f(x)参数
    def setfxArgs(self, args):
        self.__function.setArgs(args)

    # 修改f'(x)
    def setfdx(self, fdchoice):
        self.__functionD.setChoice(fdchoice)

    # 修改f'(x)参数
    def setfdxArgs(self, args):
        self.__functionD.setArgs(args)

    # 返回结果
    def getResult(self):
        self.__do()
        return self.__result
