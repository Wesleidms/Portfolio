import tkinter as tk

# Função para adicionar caracteres na entrada
def clicar(valor):
    entrada.insert(tk.END, valor)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.configure(bg="#222")

# Entrada de texto
entrada = tk.Entry(janela, font=("Arial", 20), bd=4, relief=tk.RIDGE, justify="right")
entrada.pack(padx=10, pady=20, fill="x")

# Botões
botoes = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C",)
]

for linha in botoes:
    frame = tk.Frame(janela, bg="#222")
    frame.pack(expand=True, fill="both")
    for btn in linha:
        if btn == "=":
            comando = calcular
        elif btn == "C":
            comando = limpar
        else:
            comando = lambda x=btn: clicar(x)

        tk.Button(frame, text=btn, font=("Arial", 18), command=comando,
                  bg="#333", fg="white", relief=tk.FLAT).pack(side="left", expand=True, fill="both", padx=1, pady=1)

# Rodapé
tk.Label(janela, text="Criado por Weslei – Projeto educacional", font=("Arial", 8), bg="#222", fg="#888").pack(pady=10)

janela.mainloop()