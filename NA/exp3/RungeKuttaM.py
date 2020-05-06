from NA.Test import Function as F


# 4阶Runge-Kutta经典形式
class RungeKuttaM:
    __x0: float
    __y0: float  # 初始条件
    __function: F.Function  # f'(x) = f(x, y) 的右式
    __h: float  # 步长，默认为0.1
    __times: int  # 步数，默认为10
    __x: list
    __y: list

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
        x0 = self.__x0
        y0 = self.__y0
        x = [x0]
        y = [y0]
        for i in range(self.__times):  # 四阶龙格库塔方法经典格式
            xt = x[i] + h  # xt: Xn+1
            xm = x[i] + h * 0.5  # xm: Xn+1/2
            K1 = f.fxy(x[i], y[i])  # x[i]: Xn  y[i]: Yn
            K2 = f.fxy(xm, y[i] + K1 * h / 2)
            K3 = f.fxy(xm, y[i] + K2 * h / 2)
            K4 = f.fxy(xt, y[i] + h * K3)
            yt = y[i] + (K1 + 2 * K2 + 2 * K3 + K4) * h / 6  # yt: Yn+1
            x.append(xt)
            y.append(yt)
        self.__x = x[:]
        self.__y = y[:]
