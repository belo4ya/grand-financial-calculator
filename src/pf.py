import numpy as np
import numpy_financial as npf
import sympy as sp


def npv(npv_, i, values):
    """
    Приведенная стоимость

    :param npv_: приведенная стоимость
    :param i: % ставка
    :param values: поток платежей
    """
    return sp.Eq(npv_, npf.npv(i, values))


def irr(irr_, values):
    """
    Внутрення норма доходности, %

    :param irr_: внутрення норма доходности, %
    :param values: поток платежей
    """
    return sp.Eq(irr_, npf.irr(values))


def rent(npv_, c, i, t, mode=0):
    """
    Рента

    :param npv_: приведенная стоимость
    :param c: фиксированный платеж
    :param i: % ставка
    :param t: кол-во периодов платежа
    :param mode: 0 - упреждающая, 1 - запаздывающая
    """
    if mode == 0:
        expr = c * (1 + 1 / i) * (1 - (1 + i) ** -t)
    else:
        expr = (c * (1 - (1 + i) ** -t)) / i

    return sp.Eq(npv_, expr)


def duration(duration_, i, values):
    """
    Дюрация

    :param duration_: дюрация (средневзвешенное по дисконтированным значениям)
    :param i: % ставка
    :param values: поток платежей
    """
    values = np.asarray(values)
    t = np.arange(1, len(values) + 1)
    discounted_values = values / (1 + i) ** t
    return sp.Eq(duration_, np.sum(discounted_values * t) / np.sum(discounted_values))
