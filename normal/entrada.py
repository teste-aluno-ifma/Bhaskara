def ler_numero(mensagem):
    while True:
        texto_digitado = input(mensagem).strip()
        try:
            return float(texto_digitado.replace(",", "."))
        except ValueError:
            print(
                f"'{texto_digitado}' nao e um numero valido. Use apenas digitos, "
                f"podendo usar virgula ou ponto para casas decimais (ex.: 2,5)."
            )


def ler_coeficientes():
    print("Equacao do segundo grau: ax^2 + bx + c = 0")

    while True:
        coeficiente_a = ler_numero("Digite o valor de a: ")
        if coeficiente_a != 0:
            break
        print("O coeficiente a deve ser diferente de zero. Digite outro valor.")

    coeficiente_b = ler_numero("Digite o valor de b: ")
    coeficiente_c = ler_numero("Digite o valor de c: ")
    return coeficiente_a, coeficiente_b, coeficiente_c
