def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um numero valido.")


def ler_coeficientes():
    print("Equacao do segundo grau: ax^2 + bx + c = 0")

    while True:
        coeficiente_a = ler_numero("Digite o valor de a: ")
        if coeficiente_a != 0:
            break
        print("O coeficiente a deve ser diferente de zero.")

    coeficiente_b = ler_numero("Digite o valor de b: ")
    coeficiente_c = ler_numero("Digite o valor de c: ")
    return coeficiente_a, coeficiente_b, coeficiente_c