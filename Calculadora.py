import tkinter as tk

# Funció per afegir números o operacions
def clicar(valor):
    entrada.insert(tk.END, valor)

# Funció per calcular el resultat
def calcular():
    try:
        resultat = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultat)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Funció per netejar pantalla
def netejar():
    entrada.delete(0, tk.END)

# Crear finestra
finestra = tk.Tk()
finestra.title("Calculadora")
finestra.geometry("350x450")

# Pantalla
entrada = tk.Entry(finestra, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entrada.pack(fill="both", padx=10, pady=10)

# Frame per als botons
frame = tk.Frame(finestra)
frame.pack()

# Llista de botons
botons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

fila = 0
columna = 0

for boto in botons:
    if boto == "=":
        btn = tk.Button(frame, text=boto, width=5, height=2, font=("Arial", 18),
                        command=calcular)
    else:
        btn = tk.Button(frame, text=boto, width=5, height=2, font=("Arial", 18),
                        command=lambda b=boto: clicar(b))

    btn.grid(row=fila, column=columna)
    columna += 1

    if columna > 3:
        columna = 0
        fila += 1

# Botó C (netejar)
btn_clear = tk.Button(finestra, text="C", width=20, height=2,
                      font=("Arial", 18), command=netejar)
btn_clear.pack(pady=10)

# Executar finestra
finestra.mainloop()