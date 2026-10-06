from calculos import calcular_raizes
from entrada import ler_coeficientes
from graficos import exibir_grafico
from resultados import exibir_resultados


def main():
    coeficiente_a, coeficiente_b, coeficiente_c = ler_coeficientes()
    delta, raiz_1, raiz_2 = calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c)

    exibir_resultados(coeficiente_a, coeficiente_b, coeficiente_c, delta, raiz_1, raiz_2)

    resposta = input("\nDeseja exibir o grafico? (s/n): ").strip().lower()
    if resposta == "s":
        exibir_grafico(coeficiente_a, coeficiente_b, coeficiente_c, raiz_1, raiz_2)


if __name__ == "__main__":
    main()