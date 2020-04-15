# exercise 8.1
import numpy as np


def function(point):
    x1 = point[0]
    x2 = point[1]
    return x1 + 0.5 * x2 + 0.5 * x1**2 + x2**2 + 3
def gradient_f(x):
    return np.array([1+x[0], 0.5 + 2*x[1]])

def phi_function(x, alpha):
    grad_f = gradient_f(x)
    x = x - alpha * grad_f
    return function(x)

def gradient_phi(point, alpha): #phi(alpha) function
    x1 = point[0]
    x2 = point[1]

    grad1 = (alpha-1)*(1+x1)**2
    grad2 = 0.5 * (alpha-0.5) * (1+4*x2)**2
    return grad1 + grad2

def secantMethod4Alpha(alpha1, alpha2, x, threshold, max_iter_num):
    for i in range(max_iter_num):
        grad1 = gradient_phi(x, alpha1)
        grad2 = gradient_phi(x, alpha2)

        alpha_temp = (grad2 * alpha1 - grad1 * alpha2) * 1.0 / (grad2 - grad1)

        alpha1 = alpha2
        alpha2 = alpha_temp

        f_value1 = phi_function(x, alpha1)
        f_value2 = phi_function(x, alpha2)

        if abs(f_value1 - f_value2) * 1.0 / f_value1 < threshold:
            break
    return alpha2

def steepestMethod(alpha1, alpha2, x, threshold_1d,threshold_s, max_iter_num):
    for k in range(max_iter_num):
        step_length = secantMethod4Alpha(alpha1, alpha2, x, threshold_1d, max_iter_num)

        x_old = x
        x = x - step_length * gradient_f(x)

        if np.linalg.norm(x-x_old, ord=2) / (np.linalg.norm(x_old, ord=2) + 1e-6) < threshold_s:
            break
    return x

alpha1 = 0
alpha2 = 1
x = np.array([0, 0])
threshold_1d = 0.01
threshold_s = 0.01
max_iter_num = 100
x = steepestMethod(alpha1, alpha2, x, threshold_1d,threshold_s, max_iter_num)
y = function(x)

print(x)
print(y)


















