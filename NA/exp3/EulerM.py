from NA.Test import Function as F


# 改进的欧拉法
class EulerM:
    __x0: float
    __y0: float  # 初始条件
    __function: F.Function  # f'(x) = f(x, y) 的右式
    __h: float  # 步长，默认为0.1
    __times: int  # 步数，默认为10
    __x: list
    __y: list  # 结果集

    def __init__(self, x0, y0, fchoice):
        self.__x0 = x0
        self.__y0 = y0
        self.__function = F.Function(fchoice)
        self.__h = 0.1
        self.__times = 10
        self.__do()

    # 设置步长
    def seth(self, h):
        self.__h = h
        self.__do()

    # 设置步数
    def setTimes(self, times):
        self.__times = times
        self.__do()

    # 获取结果
    def getResult(self):
        return list(zip(self.__x, self.__y))

    # 计算
    def __do(self):
        h = self.__h
        f = self.__function
        x = [self.__x0]
        y = [self.__y0]
        for i in range(self.__times):  # 采用平均化形式计算
            yp = y[i] + h * f.fxy(x[i], y[i])
            xt = self.__x0 + h * (i+1)
            x.append(xt)
            ye = y[i] + h * f.fxy(xt, yp)
            yt = 0.5 * (yp + ye)
            y.append(yt)
        self.__x = x[:]
        self.__y = y[:]
