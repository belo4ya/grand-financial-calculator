import numpy as np
import sympy as sp


def npv(npv_, f, c, i, t):
    """
    Внутренняя стоимость (текущая)

    :param npv_: внутренняя стоимость (текущая)
    :param f: номинальная стоимость
    :param c: купонная выплата
    :param i: % ставка
    :param t: кол-во купонных периодов
    """
    return sp.Eq(npv_, c * (1 - (1 + i) ** -t) / i + f * (1 + i) ** -t)


def brate(brate_, p, f):
    """
    Курс облигации

    :param brate_: курс облигации
    :param p: рыночная цена
    :param f: номинальная стоимость
    """
    return sp.Eq(brate_, p / f * 100)


def duration(duration_, p_0, f, c, i, n):
    """
    Дюрация облигации

    :param duration_: дюрация облигации
    :param p_0: внутренняя стоимость (текущая)
    :param f: номинальная стоимость
    :param c: купонная выплата
    :param i: % ставка
    :param n: кол-во купонных периодов
    """
    t = np.arange(1, n + 1)
    return sp.Eq(duration_, (np.sum(t * c / (1 + i) ** t) + n * f / (1 + i) ** n) / p_0)
