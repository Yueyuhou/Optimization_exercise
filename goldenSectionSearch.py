import matplotlib.pyplot as plt
import numpy as np
import math


def plotTargetFunction(x_, y_):
    x = x_
    y = y_
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='X', ylabel='Y', title='ex7.3')
    ax.grid(False)

    plt.show()
    return ax

def resultShow(x_, y_, record_a, record_b, f_value_a, f_value_b):
    x = x_
    y = y_
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='X', ylabel='Y', title='ex7.3')

    ax.scatter(record_a, f_value_a, c='r', label='a')
    ax.scatter(record_b, f_value_b, c='b', label='b')
    plt.show()

def function(i):
    return 8 * math.exp(1 - i) + 7 * math.log(i)


def goldenSectionSearch(f, ini_area_, target_length):
    rho = 0.382

    ini_area = ini_area_ if ini_area_[0] < ini_area_[1] else ini_area_.reverse()
    a = []
    a.append(ini_area[0])
    b = []
    b.append(ini_area[1])

    current_length0 = b[0] - a[0]

    ite_num = 0
    while current_length0 * math.pow(1 - rho, ite_num) > target_length:
        ite_num += 1

    for i in range(ite_num):
        current_length = b[-1] - a[-1]
        temp_a = a[-1] + current_length * rho
        temp_b = b[-1] - current_length * rho

        current_a = a[-1]
        current_b = b[-1]

        if (f(temp_a) < f(temp_b)):
            b.append(temp_b)
            a.append(current_a)
        else:
            a.append(temp_a)
            b.append(current_b)

    func_value_a = [f(i) for i in a]
    func_value_b = [f(i) for i in b]

    return a, b, func_value_a, func_value_b



def fibonacciMethod():
    pass

ini_area_ = [1, 2]
target_length = 0.23
x = np.linspace(1, 2, 20)
f = function
y = [f(i) for i in x]

#plotTargetFunction(x, y)
record_a, record_b, f_value_a, f_value_b = goldenSectionSearch(f, ini_area_, target_length)
resultShow(x, y, record_a, record_b, f_value_a, f_value_b)

