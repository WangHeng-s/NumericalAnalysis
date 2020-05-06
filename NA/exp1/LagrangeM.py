import numpy as np
import matplotlib.pyplot as plt


# Lagrange插值法
class LagrangeM:
    __x: list
    __y: list

    def __init__(self, xt, yt):
        self.__x = xt[:]
        self.__y = yt[:]

    # 返回Lagrange基函数l(x)的值
    # @return List
    def __getlx(self, x0):
        n = len(self.__x)
        lx = []
        for k in range(n):
            indexs = [i for i in range(n) if i != k]
            numberate = np.prod([x0 - self.__x[i] for i in indexs])
            denominator = np.prod([self.__x[k] - self.__x[i] for i in indexs])
            lx.append(numberate / denominator)
        return lx

    # L(x0)
    def fx(self, x0):
        n = len(self.__x)
        lx = self.__getlx(x0)
        result = sum(lx[i] * self.__y[i] for i in range(n))
        return result

    # 添加插值节点
    def add(self, x0, y0):
        self.__x.append(x0)
        self.__y.append(y0)

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
            temp = self.fx(i)
            y.append(temp)
        plt.plot(x, y, label="拟合曲线")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.ylim(min(y)-1, max(y)+1)
        plt.legend()
        plt.show()