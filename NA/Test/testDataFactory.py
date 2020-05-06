# 通过本程序更新实验中所使用的数据
# 不同实验的数据更新写为函数，数据修改的过程：修改函数->调用函数


# 插值数据
def testDataExp1():
    ls1 = [['1', '2', '3', '4', '5'], ['1', '2', '3', '4', '5']]
    ls2 = [['10', '11', '12', '13', '14', '15', '16'], ['100', '121', '144', '169', '196', '225', '256']]
    ls3 = [['100', '121', '144', '169', '196', '225', '256'], ['10', '11', '12', '13', '14', '15', '16']]
    ls4 = [['-2', '-1', '1', '2'], ['5', '3', '17', '21']]
    ls5 = [['1', '2', '3', '4', '5'], ['1.1', '1.9', '3.2', '4.1', '4.5']]
    with open('插值数据.csv', 'w', encoding='utf-8') as f:
        for s in ls2:
            f.write(','.join(s)+'\n')


# 数值积分数据
def testDataExp2():
    ls1 = [['0', '10', '5'], ['sin']]
    ls2 = [['1', '100', '18'], ['q']]
    ls3 = [['0', '100', '18'], ['l']]
    ls4 = [['0', '1', '1024'], ['f5']]
    with open('数值积分.csv', 'w', encoding='utf-8') as f:
        for s in ls3:
            f.write(','.join(s)+'\n')


testDataExp2()
print('done')