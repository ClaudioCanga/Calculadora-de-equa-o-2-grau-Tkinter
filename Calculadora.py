import tkinter as tk
from tkinter import ttk
from fractions import Fraction
from math import sqrt
from PIL import Image, ImageTk

def calcular_raizes():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        discriminante = b**2 - 4*a*c

        passos = []

        if discriminante > 0:
            raiz1 = (-b + sqrt(discriminante)) / (2*a)
            raiz2 = (-b - sqrt(discriminante)) / (2*a)
            passos.append(f"Discriminante = {discriminante}, maior que zero.")
            passos.append(f"Raízes: {Fraction(raiz1).limit_denominator()}, {Fraction(raiz2).limit_denominator()}")
        elif discriminante == 0:
            raiz = -b / (2*a)
            passos.append(f"Discriminante = {discriminante}, igual a zero.")
            passos.append(f"Raiz dupla: {Fraction(raiz).limit_denominator()}")
        else:
            parte_real = -b / (2*a)
            parte_imaginaria = sqrt(abs(discriminante)) / (2*a)
            raiz1 = complex(parte_real, parte_imaginaria)
            raiz2 = complex(parte_real, -parte_imaginaria)
            passos.append(f"Discriminante = {discriminante}, menor que zero.")
            passos.append(f"Raízes complexas: {raiz1}, {raiz2}")

        # Exibir os passos na label de resultado
        label_resultado.config(text="\n".join(passos))
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos para os coeficientes!")

# Criar janela
root = tk.Tk()
root.title("Calculadora de Equação do Segundo Grau")
root.geometry("500x400")
root.configure(bg="#FFFFFF")

# Imagem da equação quadrática
equacao_image = Image.open("C:\\Users\\Eduardo\\Documents\\Cláudio\\Projectos python\\equacao_quadratica.png")
equacao_image = equacao_image.resize((200, 100))
equacao_image = ImageTk.PhotoImage(equacao_image)
equacao_label = tk.Label(root, image=equacao_image, bg="#FFFFFF")
equacao_label.place(relx=0.5, rely=0.1, anchor="center")

# Criar frame
frame = ttk.Frame(root, style="DarkTheme.TFrame", padding=10)
frame.place(relx=0.5, rely=0.6, anchor="center")

# Criar labels
label_a = ttk.Label(frame, text="Coeficiente a:", style="DarkTheme.TLabel")
label_a.grid(row=0, column=0, padx=5, pady=5)
label_b = ttk.Label(frame, text="Coeficiente b:", style="DarkTheme.TLabel")
label_b.grid(row=1, column=0, padx=5, pady=5)
label_c = ttk.Label(frame, text="Coeficiente c:", style="DarkTheme.TLabel")
label_c.grid(row=2, column=0, padx=5, pady=5)
label_resultado = ttk.Label(frame, text="", style="DarkTheme.TLabel", wraplength=300)
label_resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Criar entry
entry_a = ttk.Entry(frame)
entry_a.grid(row=0, column=1, padx=5, pady=5)
entry_b = ttk.Entry(frame)
entry_b.grid(row=1, column=1, padx=5, pady=5)
entry_c = ttk.Entry(frame)
entry_c.grid(row=2, column=1, padx=5, pady=5)

# Botão de calcular
btn_calcular = ttk.Button(frame, text="Calcular", command=calcular_raizes, style="DarkTheme.TButton")
btn_calcular.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Aplicar estilo
style = ttk.Style()
style.configure("DarkTheme.TLabel", background="#FFFFFF", foreground="#333333", font=("Arial", 10))
style.configure("DarkTheme.TEntry", fieldbackground="#424242", foreground="#FFFFFF", font=("Arial", 10))
style.configure("DarkTheme.TButton", background="#757575", foreground="#FFFFFF", font=("Arial", 10))
style.configure("DarkTheme.TFrame", background="#FFFFFF", relief="raised", borderwidth=2)

# Rodar aplicação
root.mainloop()