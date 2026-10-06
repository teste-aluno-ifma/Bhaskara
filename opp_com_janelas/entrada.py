class LeitorDeEntrada:
    def ler_coeficientes(self, texto_a, texto_b, texto_c):
        try:
            coeficiente_a = float(texto_a.replace(",", "."))
            coeficiente_b = float(texto_b.replace(",", "."))
            coeficiente_c = float(texto_c.replace(",", "."))
        except ValueError as erro:
            raise ValueError("Preencha os tres coeficientes com numeros validos.") from erro

        if coeficiente_a == 0:
            raise ValueError("O coeficiente a deve ser diferente de zero.")

        return coeficiente_a, coeficiente_b, coeficiente_c