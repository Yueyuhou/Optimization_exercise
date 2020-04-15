import math


def secantMethod(grad, x0, max_itNum=100, threshold=0.001):
    if grad(x0) < 1e-5:
        return x0

    x1 = x0 + 1
    it_num = 0

    while True:
        grad_x0, grad_x1 = grad(x0), grad(x1)
        x2 = (grad_x1 * x0 - grad_x0 * x1) * 1.0 / (grad_x1 - grad_x0)
        grad_x2 = grad(x2)

        if math.abs(grad_x2 - grad_x1) * 1.0 / grad_x1 < threshold:
            return x2
        if it_num > max_itNum - 1:
            return x2

        x0 = x1
        x1 = x2
        it_num = it_num + 1
