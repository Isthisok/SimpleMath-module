from math import sqrt

def Power(num: int or float, powerof: int or float) -> float or int:
    __val__ = 1

    if num == 0:
        return 0
    elif powerof == 0:
        return 1
    else:
        while powerof > 0:
            __val__ = __val__*num
            powerof -= 1

        if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

        return __val__

def StandardDeviation(list: list) -> float or int:
    __TopOfFraction__ = 0
    __len__ = len(list)
    __mean__ = sum(list) / __len__

    for num in list:
        __TopOfFraction__ += Power((num - __mean__), 2)

    __val__ = sqrt(__TopOfFraction__/__len__)

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return(__val__)

def LinearEquationY(m: int or float, x: int or float, c: int or float) -> int or float:
    __val__ = (m * x) + c

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def LinearEquationX(y: int or float, m: int or float, c: int or float) -> int or float:
    __val__ = (y - c) / m

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def LinearEquationM(y: int or float, x: int or float, c: int or float) -> int or float:
    __val__ = (y - c) / x

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def LinearEquationC(y: int or float, m: int or float, x: int or float):
    __val__ = (m * x) - y

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def QuadraticEquation(a: int or float, b: int or float, c: int or float) -> int or float or list or bool:
    __discriminant__ = Power(b, 2) - (4*a*c)
    if __discriminant__ > 0:
        __val__ = [
            ((b*(-1))+(sqrt((b*b)-(4*a*c))))/(2*a),
            ((b*(-1))-(sqrt((b*b)-(4*a*c))))/(2*a)
        ]
    if __discriminant__ == 0:
        __val__ = (-b) * 2 * a

    if __discriminant__ < 0:
        __val__ = False

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__
