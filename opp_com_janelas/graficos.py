class GeradorDeGrafico:
    def exibir(self, equacao, raiz_1, raiz_2):
        try:
            import matplotlib.pyplot as plt
        except ModuleNotFoundError:
            print("Para exibir o grafico, instale matplotlib com: pip install matplotlib")
            return

        x_vertice, y_vertice = equacao.calcular_vertice()
        pontos_referencia = [x_vertice]

        if raiz_1 is not None:
            pontos_referencia.append(raiz_1)
        if raiz_2 is not None:
            pontos_referencia.append(raiz_2)

        menor_x = min(pontos_referencia) - 5
        maior_x = max(pontos_referencia) + 5
        intervalo = (maior_x - menor_x) / 200
        valores_x = [menor_x + indice * intervalo for indice in range(201)]
        valores_y = [equacao.calcular_y(valor_x) for valor_x in valores_x]

        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.plot(valores_x, valores_y, label="f(x) = ax^2 + bx + c")
        plt.scatter([x_vertice], [y_vertice], color="orange", label="Vertice")

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