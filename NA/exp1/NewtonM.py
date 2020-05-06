import numpy as np
import matplotlib.pyplot as plt


# 差商表
class Table:
    __x: list
    __y: list
    __table: list  # 差商表（列表形式）

    # 初始化x，y和差商表
    def __init__(self, xt, yt):
        self.__x = xt[:]
        self.__y = yt[:]
        tempTable = []
        n = len(xt)
        tempTable.append(yt)
        for k in range(1, n):
            ls = []
            for i in range(0, n - k):
                temp = (tempTable[k-1][i+1] - tempTable[k-1][i])/(xt[k+i] - xt[i])
                ls.append(temp)
            tempTable.append(ls)
        self.__table = tempTable[:]

    # 返回差商表
    def getTable(self):
        return self.__table

    # 增加一个x和对应的y
    def add(self, x0, y0):
        self.__x.append(x0)
        self.__y.append(y0)
        n = len(self.__x)
        self.__table.append([])  # 新增最高阶差商初始化，避免下标越界
        self.__table[0].append(y0)  # 零阶差商增加
        for k in range(1, n):
            i = n - k
            temp = (self.__table[k - 1][i] - self.__table[k - 1][i - 1]) / (self.__x[n - 1] - self.__x[n - 1 - k])
            self.__table[k].append(temp)


# Newton插值法
class NewtonM:
    __table: Table
    __x: list
    __y: list

    # 初始化差商表
    def __init__(self, xt, yt):
        self.__x = xt[:]
        self.__y = yt[:]
        self.__table = Table(xt, yt)

    # 返回N(x0)
    def fx(self, x0):
        n = len(self.__x)
        table = self.__table.getTable()
        bases = [ls[0] for ls in table]
        m = []
        temp = 1
        for i in range(0, n - 1):
            m.append(temp)
            temp = temp * (x0 - self.__x[i])
        m.append(temp)
        result = sum([bases[j] * m[j] for j in range(n)])
        return result

    # 增加新的插值节点
    def add(self, x0, y0):
        self.__x.append(x0)
        self.__y.append(y0)
        self.__table.add(x0, y0)

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
