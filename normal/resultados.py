def exibir_resultados(coeficiente_a, coeficiente_b, coeficiente_c, delta, raiz_1, raiz_2):
    print("\n--- Resultado ---")
    print(f"Equacao: ({coeficiente_a})x^2 + ({coeficiente_b})x + ({coeficiente_c}) = 0")
    print(f"Delta: {delta}")

    if delta < 0:
        print("A equacao nao possui raizes reais.")
    elif delta == 0:
        print(f"A equacao possui uma raiz real: x = {raiz_1}")
    else:
        print(f"A equacao possui duas raizes reais:")
        print(f"x1 = {raiz_1}")
        print(f"x2 = {raiz_2}")