import tkinter as tk
from tkinter import messagebox, ttk

from calculos import EquacaoSegundoGrau
from entrada import LeitorDeEntrada
from graficos import GeradorDeGrafico
from resultados import ExibidorDeResultados


class JanelaBhaskara:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Formula de Bhaskara")
        self.janela.resizable(False, False)
        self.leitor = LeitorDeEntrada()
        self.exibidor = ExibidorDeResultados()
        self.gerador = GeradorDeGrafico()
        self.equacao = None
        self.raiz_1 = None
        self.raiz_2 = None

        quadro = ttk.Frame(janela, padding=20)
        quadro.grid()

        ttk.Label(quadro, text="Equacao: ax^2 + bx + c = 0", font=("TkDefaultFont", 12, "bold")).grid(
            column=0, row=0, columnspan=2, pady=(0, 15)
        )

        self.campos = {}
        for indice, letra in enumerate(("a", "b", "c"), start=1):
            ttk.Label(quadro, text=f"Coeficiente {letra}:").grid(column=0, row=indice, sticky="w", pady=4)
            campo = ttk.Entry(quadro, width=22)
            campo.grid(column=1, row=indice, pady=4)
            self.campos[letra] = campo

        ttk.Button(quadro, text="Calcular", command=self.calcular).grid(column=0, row=4, pady=15, sticky="ew")
        ttk.Button(quadro, text="Limpar", command=self.limpar).grid(column=1, row=4, pady=15, sticky="ew")
        ttk.Button(quadro, text="Exibir grafico", command=self.exibir_grafico).grid(
            column=0, row=5, columnspan=2, sticky="ew"
        )

        self.resultado = tk.StringVar(value="Informe os coeficientes e clique em Calcular.")
        ttk.Label(quadro, textvariable=self.resultado, justify="left").grid(
            column=0, row=6, columnspan=2, sticky="w", pady=(15, 0)
        )
        self.campos["a"].focus()

    def calcular(self):
        try:
            coeficiente_a, coeficiente_b, coeficiente_c = self.leitor.ler_coeficientes(
                self.campos["a"].get(), self.campos["b"].get(), self.campos["c"].get()
            )
        except ValueError as erro:
            messagebox.showerror("Dados invalidos", str(erro), parent=self.janela)
            return

        self.equacao = EquacaoSegundoGrau(coeficiente_a, coeficiente_b, coeficiente_c)
        delta = self.equacao.calcular_delta()
        self.raiz_1, self.raiz_2 = self.equacao.calcular_raizes()
        self.resultado.set(self.exibidor.criar_texto(self.equacao, delta, self.raiz_1, self.raiz_2))

    def limpar(self):
        # Apaga os campos, zera o calculo guardado e devolve o foco ao coeficiente a
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.equacao = None
        self.raiz_1 = None
        self.raiz_2 = None
        self.resultado.set("Informe os coeficientes e clique em Calcular.")
        self.campos["a"].focus()

    def exibir_grafico(self):
        if self.equacao is None:
            messagebox.showwarning("Calculo necessario", "Calcule a equacao antes de exibir o grafico.", parent=self.janela)
            return

        self.gerador.exibir(self.equacao, self.raiz_1, self.raiz_2)


def main():
    janela = tk.Tk()
    JanelaBhaskara(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()