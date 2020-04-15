'''
This function works for 1d-search with the Bisection method.
It should be called in other functions as a part of them.
'''
import math

def biSectionMethod(section, gradFun, maxItmun=100, threshold=0.001):
    old_mid_point = 100000
    itNum = 0
    while True:
        left_point, right_point = section
        mid_point = 0.5 * (right_point + left_point)
        mid_grad = gradFun(mid_point)

        if mid_grad < 1e-5:
            return mid_point

        if math.abs(mid_point - old_mid_point)*1.0/old_mid_point < threshold:
            return mid_point
        if itNum > maxItmun - 1:
            return mid_point

        if mid_grad > 0:
            section = [left_point, mid_point]
        else:
            section = [mid_point, right_point]
        old_mid_point = mid_point
        itNum = itNum + 1









