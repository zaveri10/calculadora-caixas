import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        C_maior = float(entry_c_maior.get())
        L_maior = float(entry_l_maior.get())
        A_maior = float(entry_a_maior.get())

        C_menor = float(entry_c_menor.get())
        L_menor = float(entry_l_menor.get())
        A_menor = float(entry_a_menor.get())

        if C_menor == 0 or L_menor == 0 or A_menor == 0:
            raise ZeroDivisionError

        total = (C_maior / C_menor) + (L_maior / L_menor) + (A_maior / A_menor)
        total_int = int(total)  # ou round(total) se preferir arredondar
        resultado_label.config(text=f"Cabem {total_int} peças dentro da caixa.")
    except ValueError:
        messagebox.showerror("Erro", "Insira apenas números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "As medidas da caixa menor não podem ser zero.")

def resetar():
    for entry in entradas:
        entry.delete(0, tk.END)
    resultado_label.config(text="")

# Janela
root = tk.Tk()
root.title("Calculadora de Peças na Caixa")
root.geometry("380x600")

entradas = []

# Título Caixa Maior
tk.Label(root, text="Caixa Maior (dimensões em mm)", font=("Helvetica", 10, "bold")).pack(pady=5)

tk.Label(root, text="Comprimento:").pack()
entry_c_maior = tk.Entry(root)
entry_c_maior.pack()
entradas.append(entry_c_maior)

tk.Label(root, text="Largura:").pack()
entry_l_maior = tk.Entry(root)
entry_l_maior.pack()
entradas.append(entry_l_maior)

tk.Label(root, text="Altura:").pack()
entry_a_maior = tk.Entry(root)
entry_a_maior.pack()
entradas.append(entry_a_maior)

# Título Caixa Menor
tk.Label(root, text="Caixa Menor (dimensões em mm)", font=("Helvetica", 10, "bold")).pack(pady=10)

tk.Label(root, text="Comprimento:").pack()
entry_c_menor = tk.Entry(root)
entry_c_menor.pack()
entradas.append(entry_c_menor)

tk.Label(root, text="Largura:").pack()
entry_l_menor = tk.Entry(root)
entry_l_menor.pack()
entradas.append(entry_l_menor)

tk.Label(root, text="Altura:").pack()
entry_a_menor = tk.Entry(root)
entry_a_menor.pack()
entradas.append(entry_a_menor)

# Botões
tk.Button(root, text="Calcular", command=calcular).pack(pady=15)
tk.Button(root, text="Resetar", command=resetar).pack()

# Resultado
resultado_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), wraplength=300)
resultado_label.pack(pady=20)

root.mainloop()
