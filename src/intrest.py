import sympy as sp


def simple_interest(s, s_0, i, t):
    """
    Простой процент
    """
    return sp.Eq(s, s_0 * (1 + t * i))


def compound_interest(s, s_0, i, t):
    """
    Сложный процент
    """
    return sp.Eq(s, s_0 * (1 + i) ** t)


def continuous_interest_sf(s, s_0, i, t):
    """
    Непрерывный процент (через e)
    """
    return sp.Eq(s, s_0 * sp.E ** (i * t))


def continuous_interest_lf(s, s_0, i, t, m):
    """
    Непрерывный процент (через сложный)
    """
    return sp.Eq(s, s_0 * (1 + i / m) ** (m * t))


def equivalent_rates(interests, ies, s, s_0, t, m):
    """
    Эквивалентные ставки
    """
    interest_l, interest_r = interests
    i_l, i_r = ies

    equation = sp.Eq(interest_l(s, s_0, i_l, t), interest_r(s, s_0, i_r, t, m))
    return [sp.solve(equation, i_l), sp.solve(equation, i_r)]


def effective_rate(i, t):
    """
    Эффективная ставка (через сложный)
    """
    return (1 + i / t) ** t - 1
