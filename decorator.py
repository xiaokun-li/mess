# _*_ coding:utf-8 _*_

import functools


def wwraper(function):
    def inner(*args, **kwargs):
        print("enhancement...")
        return function(*args, **kwargs)

    return inner


@wwraper
def f1():
    print("f1 function is running...")


@wwraper
def f2():
    print("f2 function is running...")


ff1 = f1

del f1

ff1()
f2()
