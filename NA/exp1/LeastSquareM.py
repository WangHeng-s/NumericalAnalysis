import matplotlib.pyplot as plt
import numpy as np


# 曲线拟合的最小二乘法
class LeastSquareM:  # M: Method
    __a: float  # a,b为曲线拟合的结果
    __b: float
    __x: list  # x->y为曲线拟合所用点集
    __y: list

    def __init__(self, xt, yt):
        self.__x = xt[:]
        self.__y = yt[:]
        self.__do()  # 通过最小二乘法计算__a和__b

    # 最小二乘法计算得到__a和__b
    def __do(self):
        N = len(self.__x)
        sumOfX = sum(self.__x)  # 所有xi求和
        sumOfY = sum(self.__y)  # 所有yi求和
        sumOfXS = sum([xi**2 for xi in self.__x])  # xi的平方和
        sumOfXmY = sum([self.__x[i] * self.__y[i] for i in range(N)])  # xi * yi 的和
        ''' 
        接下来解方程组 
        a * N + b * sumOfX = sumOfY
        a * sumOfX + b * sumOfXS = sumOfXmY
        解得 b = (sumOfY * sumOfX - N * sumOfXmY)/(sumOfX ** 2 - N * sumOfXS)
        a = (sumOfY - b * sumOfX)/N
        '''
        self.__b = (sumOfY * sumOfX - N * sumOfXmY) / (sumOfX ** 2 - N * sumOfXS)
        self.__a = (sumOfY - self.__b * sumOfX) / N

    # 以字符串形式返回拟合结果
    def result(self):
        result = 'y = {} + {} * x'.format(self.__a, self.__b)
        return result

    # 绘出结果曲线
    def paint(self):
        mx = min(self.__x)
        my = max(self.__y)
        left = round(mx - 0.2 * (my - mx))
        right = round(my + 0.2 * (my - mx))
        step = (right - left)/20
        x = np.arange(left, right, step)
        y = []
        for i in x:
            temp = self.__a + self.__b * i
            y.append(temp)
        plt.plot(x, y, label="拟合曲线")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.ylim(min(y)-1, max(y)+1)
        plt.legend()
        plt.show()

    # 根据拟合曲线求f(x0)的近似
    def fx(self, x0):
        return self.__a + self.__b * x0

    # 增加新节点
    def add(self, x0, y0):
        if x0 not in self.__x:
            self.__x.append(x0)
            self.__y.append(y0)
            self.__do()
            return True
        return False
