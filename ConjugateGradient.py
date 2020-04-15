'''
This function is for CG method.
'''
from SecantMethod import *
import numpy as np

def CG(init_point, gradFunCg, gradFunSec):
    x_old = init_point
    loop_num = len(x_old)

    g_old = gradFunCg(x_old)

    if g_old < 1e-5:
        return x_old

    d = -1 * g_old

    for i in range(0, loop_num):
        alpha = secantMethod(gradFunSec(d, x_old), 1)
        x_new = x_old + alpha * d
        g_new = gradFunCg(x_new)

        if g_new < 1e-5:
            return x_new

        # Hestenes-Stiefel
        beta = (g_new.T * (g_new - g_old)) / (d.T * (g_new - g_old))
        d = -1 * g_new + beta * d
        x_old = x_new

    return x_new


def ConjugateGradient(init_point, gradFunCg, gradFunSec, flag=False):
    # 如果函数非二次型，就多次调用函数，继续搜索5次
    if flag is False:
        rev = CG(init_point, gradFunCg, gradFunSec)
        return rev
    else:
        rev = init_point
        for i in range(0, 5):
            rev = CG(init_point, gradFunCg, gradFunSec)
        return rev

# f=1.5*x1*x1 + 2*x2*x2 + 1.5*x3*X3 + x1*x3 + 2*x2*x3 - 3*x1 - x3
def gradFunCg(x):
    g1 = 3*x[0] + x[2] - 3
    g2 = 4*x[1] + 2*x[2]
    g3 = x[0] + 2 * x[1] + 3*x[2] - 1
    return np.array([[g1, g2, g3]]).T

def gradFunSec(alpha, d, x_old):
    d1_, d2_, d3_ = d[0], d[1], d[2]
    x1_, x2_, x3_ = x_old[0], x_old[1], x_old[2]
    return gradFunSec_(alpha, d1=d1_, d2=d2_, d3=d3_, x1=x1_, x2=x2_, x3=x3_)

def gradFunSec_(alpha, d1, d2, d3, x1, x2, x3):
    part1 = 3*(x1 + alpha*d1)*d1 + 4*(x2+alpha*d2)*d2 + 3*(x3+alpha*d3)*d3 + d1*(x3+alpha*d3)
    part2 = (x1+alpha*d1)*d3 + 2*d2(x3+alpha*d3) + 2*(x2+alpha*d2)*d3 - 3*d1 - d3
    return part1 + part2
