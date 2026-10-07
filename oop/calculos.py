import math


class EquacaoSegundoGrau:
    def __init__(self, coeficiente_a, coeficiente_b, coeficiente_c):
        """Função que recebe as entradas da formula de Bhaskara"""
        if coeficiente_a == 0:
            raise ValueError("O coeficiente a deve ser diferente de zero.")

        self.coeficiente_a = coeficiente_a
        self.coeficiente_b = coeficiente_b
        self.coeficiente_c = coeficiente_c

    def calcular_delta(self):
        return self.coeficiente_b ** 2 - 4 * self.coeficiente_a * self.coeficiente_c

    def calcular_raizes(self):
        delta = self.calcular_delta()
        denominador = 2 * self.coeficiente_a

        if delta < 0:
            return None, None

        if delta == 0:
            raiz = -self.coeficiente_b / denominador
            return raiz, raiz

        raiz_delta = math.sqrt(delta)
        raiz_1 = (-self.coeficiente_b + raiz_delta) / denominador
        raiz_2 = (-self.coeficiente_b - raiz_delta) / denominador
        return raiz_1, raiz_2

    def calcular_y(self, valor_x):
        return (
            self.coeficiente_a * valor_x ** 2
            + self.coeficiente_b * valor_x
            + self.coeficiente_c
        )

    def calcular_vertice(self):
        valor_x = -self.coeficiente_b / (2 * self.coeficiente_a)
        return valor_x, self.calcular_y(valor_x)
