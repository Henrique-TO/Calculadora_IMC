import tkinter as tk

def imc():
    n1 = int(inputt_n1.get())
    n2 = float(inputt_n2.get())
    
    resultado = n1 / (n2**2)
    bah= round(resultado, 1)
    label_resultado['text']= f'resultado é {bah}'

    if resultado >=18.6 and resultado <= 24.9:
        label_imc['text']= 'Você está Normal'
    elif resultado >= 25 and resultado <= 29:
        label_imc['text']= 'Você está em Sobrepeso'
    elif resultado >= 30 and resultado <= 34.9:
        label_imc['text']= 'Você está em Obesidade I'
    elif resultado >= 35 and resultado <= 39.9:
        label_imc['text']= 'Você está em Obesidade II'
    elif resultado > 40:
        label_imc['text']= 'Você está em Obesidade III'
    elif resultado < 18.6:
        label_imc['text']= 'Você está Abaixo do peso'
        




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

Calculo= tk.Label(root, text= f'O calculo é: peso / (altura*altura)')
Calculo.grid (row=6, column=0)

label_imc = tk.Label(root, text= 'Você está em ')
label_imc.grid(row=5, column=1)




#packs

root.mainloop()
