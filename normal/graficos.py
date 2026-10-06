def exibir_grafico(coeficiente_a, coeficiente_b, coeficiente_c, raiz_1, raiz_2):
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        print("Para exibir o grafico, instale matplotlib com: pip install matplotlib")
        return

    x_vertice = -coeficiente_b / (2 * coeficiente_a)
    pontos_referencia = [x_vertice]

    if raiz_1 is not None:
        pontos_referencia.append(raiz_1)
    if raiz_2 is not None:
        pontos_referencia.append(raiz_2)

    menor_x = min(pontos_referencia) - 5
    maior_x = max(pontos_referencia) + 5
    intervalo = (maior_x - menor_x) / 200
    valores_x = [menor_x + indice * intervalo for indice in range(201)]
    valores_y = [coeficiente_a * x ** 2 + coeficiente_b * x + coeficiente_c for x in valores_x]

    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.plot(valores_x, valores_y, label="f(x) = ax^2 + bx + c")
    plt.scatter([x_vertice], [coeficiente_a * x_vertice ** 2 + coeficiente_b * x_vertice], color="orange", label="Vertice")

    if raiz_1 is not None:
        plt.scatter([raiz_1], [0], color="red", label="Raiz real")
    if raiz_2 is not None and raiz_2 != raiz_1:
        plt.scatter([raiz_2], [0], color="red")

    plt.title("Grafico da Equacao do Segundo Grau")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.legend()
    plt.show()