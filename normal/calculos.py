import math


def calcular_delta(coeficiente_a, coeficiente_b, coeficiente_c):
    return coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c


def calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c):
    delta = calcular_delta(coeficiente_a, coeficiente_b, coeficiente_c)
    denominador = 2 * coeficiente_a

    if delta < 0:
        return delta, None, None

    if delta == 0:
        raiz = -coeficiente_b / denominador
        return delta, raiz, raiz

    raiz_delta = math.sqrt(delta)
    raiz_1 = (-coeficiente_b + raiz_delta) / denominador
    raiz_2 = (-coeficiente_b - raiz_delta) / denominador
    return delta, raiz_1, raiz_2