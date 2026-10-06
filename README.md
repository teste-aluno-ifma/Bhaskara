# 🧮 Bhaskara

Calculadora da fórmula de Bhaskara (equação do 2º grau), implementada **três vezes** com o
mesmo recorte de responsabilidades — pra comparar estilo procedural contra orientado a objetos,
terminal contra interface gráfica, sem nunca misturar cálculo com entrada/saída.

> O objetivo deste projeto nunca foi a fórmula em si — é mostrar **separação de responsabilidades**
> na prática. Escrito como teste do Copilot CLI.

## As três versões

| Pasta | Estilo | Interface |
|---|---|---|
| [`normal/`](normal/) | Funções soltas | Terminal |
| [`oop/`](oop/) | Classe `EquacaoSegundoGrau` | Janela (tkinter) |
| [`opp_com_janelas/`](opp_com_janelas/) | Classe `EquacaoSegundoGrau` | Janela (tkinter) |

Todas resolvem `ax² + bx + c = 0`: calculam o delta, as raízes reais (zero, uma ou duas) e,
se quiser, plotam o gráfico da parábola com a raiz e o vértice marcados.

## O contrato entre módulos

Cada versão segue a mesma divisão, e a regra nunca muda de uma pasta pra outra:

```
main.py        orquestra — só chama os outros, não calcula nem lê nada sozinho
entrada.py     o único arquivo que lê dado do usuário (input() ou campo da janela)
calculos.py    matemática pura — sem print, sem input, sem import de interface
resultados.py  formata o texto de saída a partir do que calculos.py devolveu
graficos.py    desenha o gráfico com matplotlib — opcional, nunca derruba o programa
```

`graficos.py` degrada sozinho se o `matplotlib` não estiver instalado: mostra um aviso
pedindo pra instalar e segue em frente, em vez de travar com `ModuleNotFoundError`.

## Como rodar

```bash
git clone https://github.com/teste-aluno-ifma/Bhaskara.git
cd Bhaskara
python3 -m venv .venv && source .venv/bin/activate
pip install matplotlib   # opcional — só pra quem quiser ver o gráfico

python normal/main.py    # versão de terminal
python oop/main.py       # versão com janela
```

A versão com janela usa `tkinter`, que já vem com o Python na maioria das instalações — no
Linux, se faltar, instale com `sudo apt install python3-tk` (Debian/Ubuntu).

## Testando os casos

| Entrada (a, b, c) | Delta | Resultado |
|---|---|---|
| 1, -5, 6 | 1 | duas raízes reais (2 e 3) |
| 1, 2, 1 | 0 | uma raiz real (-1) |
| 1, 0, 1 | -4 | nenhuma raiz real |
