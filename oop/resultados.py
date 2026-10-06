class ExibidorDeResultados:
    def criar_texto(self, equacao, delta, raiz_1, raiz_2):
        texto = (
            f"Equacao: ({equacao.coeficiente_a})x^2 + "
            f"({equacao.coeficiente_b})x + ({equacao.coeficiente_c}) = 0\n"
        )
        texto += f"Delta: {delta}\n\n"

        if delta < 0:
            return texto + "A equacao nao possui raizes reais."
        elif delta == 0:
            return texto + f"A equacao possui uma raiz real:\nx = {raiz_1}"

        return texto + f"A equacao possui duas raizes reais:\nx1 = {raiz_1}\nx2 = {raiz_2}"