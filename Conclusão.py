import tkinter as tk

def imc():
    n1 = int(inputt_n1.get())
    n2 = float(inputt_n2.get())
    
    resultado = n1 / (n2**2)
    label_resultado['text']= f'resultado é {resultado}'

root = tk.Tk()
root.title('Calculo IMC')


label_n1 = tk.Label(root, text = 'Peso (kg)')
label_n1.grid(row=0, column=0)

inputt_n1 = tk.Entry(root)
inputt_n1.grid(row=0, column=1)

label_n2 = tk.Label(root, text = 'Altura (Metro e centimetros)')
label_n2.grid(row=1, column=0)

inputt_n2 = tk.Entry(root)
inputt_n2.grid(row=1, column=1)

btn_calcular = tk.Button(root, text = 'Calcula', command=imc)
btn_calcular.grid (row=4, column=1)

label_resultado = tk.Label (root, text = 'Resultado: ')
label_resultado.grid(row=5, column=0)

Calculo= tk.Label(root, text= f'O calculo é peso / (altura*altura)')
Calculo.grid (row=6, column=0)
#packs

root.mainloop()