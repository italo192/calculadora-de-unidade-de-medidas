from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
co6 = "#48b3e0"   # blue / azul
fundo = "#3b3b3b"

#janela
janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg=co1)

# divisao da janela
frame_cima = Frame(janela, width=450, height=50, bg=co0, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=220, bg=co0, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=54)

frame_direita = Frame(janela, width=198, height=260, bg=co0, pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)

#style

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#nome do projeto

l_app_nome = Label(frame_cima, text='Calculadora de Unidades de Medidas', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=co0, fg=co6)
l_app_nome.place(x=50, y=10)

#funçoes
unidades = {
    'Massa': [{'Kg': 1000}, {'Hg': 100}, {'Dag': 10}, {'G': 1}, {'Dg': 0.1}, {'Cg': 0.01}, {'Mg': 0.001}],
    'Tempo': [{'Ano': 31536000}, {'Mes': 2592000}, {'Semana': 604800}, {'Dia': 86400}, {'Hr': 3600}, {'Min': 60}, {'Seg': 1}],
    'Comprimento': [{'Km': 1000}, {'Hm': 100}, {'Dam': 10}, {'M': 1}, {'Dm': 0.1}, {'Cm': 0.01}, {'Mm': 0.001}],
    'Area': [{'hectare': 10000}, {'Acre': 4047}, {'Km²': 1000000}, {'Hm²': 10000}, {'Pé²': 0.093}, {'Dam²': 100}, {'M²': 1}, {'Dm²': 0.01}, {'Cm²': 0.0001}, {'Mm²': 0.000001}],
    'Volume': [{'Kl': 1000000000}, {'Hl': 1000000}, {'Dal': 1000}, {'L': 1}, {'Dl': 0.001}, {'Cl': 0.000001}, {'Ml': 0.000000001}],
    'Velocidade': [{'m/s': 1}, {'km/h': 0.277778}, {'ft/s': 0.3048}, {'mph': 0.44704}],
    'Temperatura': [{'C°': 1}, {'F°': 33.8}, {'K°': 273.15}],
    'Energia': [{'joule': 1}, {'quilojoule': 0.001}, {'gram-calorie': 0.239006}, {'quilocaloria': 0.239006},{'watt-hora': 0.000277778},{'quilowatt-hora': 2.7778e-7},{'eletrón-volt': 6.242e+18}],
    'Pressão': [{'pascal': 1}, {'bar': 1e-5}, {'atmosfera': 9.8692e-6}, {'psi': 0.000145038}]
}

def mostrar_menu(i):
    unidade_de = []
    unidade_para = []
    unidade_valor = []
    
    for j in unidades[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valor.append(v)   

    c_de['values'] = unidade_de
    c_para['values'] = unidade_para

    l_unidade_nome['text'] = i

    #função que calcula as  conversões
    def calcular():
        a = c_de.get()
        b = c_para.get()

        numero_para_converter = float(e_numero.get())
        
        #conversão de massa
        if i == 'Massa':
            if unidade_para.index(b) <= unidade_de.index(a):
                distancia =unidade_para.index(a) - unidade_de.index(b)
                resultado = numero_para_converter /(10**distancia)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado 
            else:
                distancia =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(10**distancia)
            
            if unidade_de.index(a) < unidade_para.index(b):
                distancia =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(10**distancia)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                distancia =unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter /(10**distancia)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
                
        #conversão de tempo
        elif i == 'Tempo':
            if unidade_para.index(b) <= unidade_de.index(a):
                    tempo =unidade_para.index(a) - unidade_de.index(b)
                    resultado = numero_para_converter /(60**tempo)
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
            else:
                tempo =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(60**tempo)        
                
            if unidade_de.index(a) < unidade_para.index(b):
                tempo =unidade_de.index(b) - unidade_para.index(a)    
                resultado = numero_para_converter *(60**tempo)    
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado      
            else:   
                tempo =unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter /(60**tempo)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
                        
        #conversão de comprimento    
        elif i == 'Comprimento':
            if unidade_para.index(b) <= unidade_de.index(a):
                comprimento =unidade_para.index(a) - unidade_de.index(b)
                resultado = numero_para_converter /(10**comprimento)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                comprimento =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(10**comprimento)
            
            if unidade_de.index(a) < unidade_para.index(b):
                comprimento =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(10**comprimento)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                comprimento =unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter /(10**comprimento)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado

        #conversão de area   
        elif i == 'Area':
            if unidade_para.index(b) <= unidade_de.index(a):
                
                resultado = numero_para_converter *(1e+6)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                
                resultado = numero_para_converter /(1e-6)
            
            if unidade_de.index(a) < unidade_para.index(b):
                
                resultado = numero_para_converter *(1e-6)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                
                resultado = numero_para_converter /(1e+6)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado

        #conversão de volume    
        elif i == 'Volume':
            if unidade_para.index(b) <= unidade_de.index(a):
                volume =unidade_para.index(a) - unidade_de.index(b)
                resultado = numero_para_converter /(10**volume)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                volume =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(10**volume)
            
            if unidade_de.index(a) < unidade_para.index(b):
                volume =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(10**volume)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                volume =unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter /(10**volume)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
                
 
        #conversão de velocidade    
        elif i == 'Velocidade':
            if unidade_para.index(b) <= unidade_de.index(a):
                velocidade =unidade_para.index(a) - unidade_de.index(b)
                resultado = numero_para_converter /(3.6**velocidade)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                velocidade =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(3.6**velocidade)
            
            if unidade_de.index(a) < unidade_para.index(b):
                velocidade =unidade_de.index(b) - unidade_para.index(a)
                resultado = numero_para_converter *(3.6**velocidade)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                velocidade =unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter /(3.6**velocidade)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
                
        #conversão de temperatura
        elif i == 'Temperatura':    
            if a == 'C°':
                if b == 'F°':
                    resultado = (numero_para_converter * 1.8) + 32
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'K°':
                    resultado = numero_para_converter + 273
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                else:
                    resultado = numero_para_converter
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
            elif a == 'F°':
                if b == 'C°':
                    resultado = (numero_para_converter - 32) / 1.8
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'K°':
                    resultado = (numero_para_converter + 459.67) * 1.8
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                else:
                    resultado = numero_para_converter
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
            else:  # a == 'K'
                if b == 'C°':
                    resultado = numero_para_converter - 273
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'F°':
                    resultado = numero_para_converter * 1.8 - 459.67
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                else:
                    resultado = numero_para_converter
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                                 

        #conversão de energia   
        elif i == 'Energia':
            if unidade_para.index(b) <= unidade_de.index(a):
                
                resultado = numero_para_converter *(4184)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                resultado = numero_para_converter /(4184)
            
            if unidade_de.index(a) < unidade_para.index(b):
                resultado = numero_para_converter /(4184)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado
            else:
                resultado = numero_para_converter *(4184)
                resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                l_resultado['text'] = resultado_formatado

        #conversão de pressao  
        elif i == 'Pressão':  
            if a == 'pascal':
                if b == 'bar':
                    resultado = numero_para_converter /  100000
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'atmosfera':
                    resultado = numero_para_converter /  101300
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'psi':
                    resultado = numero_para_converter / 6895
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado                  
                else:
                    resultado = numero_para_converter
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
            elif a == 'bar':
                if b == 'pascal':
                    resultado = numero_para_converter * 100000
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'atmosfera':
                    resultado = numero_para_converter /  1.013
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'psi':
                    resultado = numero_para_converter * 14,504
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado                    
                else:
                    resultado = numero_para_converter
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
            elif a == 'atmosfera':
                if b == 'pascal':
                    resultado = numero_para_converter *  101300
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'bar':
                    resultado = numero_para_converter * 1.013
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'psi':
                    resultado = numero_para_converter * 14,696
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado                   
                else:
                    resultado = numero_para_converter
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
            elif a == 'psi':
                if b == 'pascal':
                    resultado = numero_para_converter * 6895
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'bar':
                    resultado = numero_para_converter / 14,504
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado
                elif b == 'atmosfera':
                    resultado = numero_para_converter / 14,696
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado                    
                else:
                    resultado = numero_para_converter
                    resultado_formatado = "{:.7f}".format(resultado)  # Limitar para 7 casas decimais
                    l_resultado['text'] = resultado_formatado                                         
                                        

                    

    # recebe o valor
    l_info = Label(frame_direita, text='Digite o valor', width=16, height=2, padx=5,pady=3 ,relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=co0, fg=co1)
    l_info.place(x=0, y=110)

    e_numero = Entry(frame_direita, width=9, font=('Ivy 15 bold'), justify='center', relief=SOLID)
    e_numero.place(x=0, y=150)
    b_calcular = Button(frame_direita,command=calcular, text="Calcular" ,width=8 ,height=1 ,relief='raised', overrelief='ridge',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
    b_calcular.place(x=115, y=150)

    l_resultado = Label(frame_direita, text='', width=12, height=1, padx=5,pady=3 ,relief='groove', anchor='center', font=('Ivy 18 bold'), bg=co0, fg=co1)
    l_resultado.place(x=0, y=200)


# esquerda
img_0 = Image.open('imagens/balança.png') 
img_0 = img_0.resize((50,50), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)

b_0 = Button(frame_esquerda,command=lambda:mostrar_menu('Massa') ,text="massa",image=img_0 ,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

img_1 = Image.open('imagens/relogio.png') 
img_1 = img_1.resize((50,50), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)

b_1 = Button(frame_esquerda,command=lambda:mostrar_menu('Tempo') , text="tempo",image=img_1 ,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

img_2 = Image.open('imagens/regua.png') 
img_2 = img_2.resize((44,44), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)

b_2 = Button(frame_esquerda,command=lambda:mostrar_menu('Comprimento') , text="comprimento",image=img_2 ,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

img_3 = Image.open('imagens/area.png') 
img_3 = img_3.resize((50,50), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)

b_3 = Button(frame_esquerda,command=lambda:mostrar_menu('Area') , text="area",image=img_3,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

img_4 = Image.open('imagens/copo.png') 
img_4 = img_4.resize((50,50), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)

b_4 = Button(frame_esquerda,command=lambda:mostrar_menu('Volume') , text="volume",image=img_4 ,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_4.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

img_5 = Image.open('imagens/velocimetro.png') 
img_5 = img_5.resize((50,50), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)

b_5 = Button(frame_esquerda,command=lambda:mostrar_menu('Velocidade') , text="velocidade",image=img_5 ,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_5.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

img_6 = Image.open('imagens/termômetro.png') 
img_6 = img_6.resize((50,50), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)

b_6= Button(frame_esquerda,command=lambda:mostrar_menu('Temperatura') , text="temperatura",image=img_6 ,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_6.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

img_7 = Image.open('imagens/energia.png') 
img_7 = img_7.resize((50,50), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)

b_7 = Button(frame_esquerda,command=lambda:mostrar_menu('Energia') , text="energia",image=img_7 ,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_7.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

img_8 = Image.open('imagens/pressao.png') 
img_8 = img_8.resize((50,50), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)

b_8 = Button(frame_esquerda,command=lambda:mostrar_menu('Pressão') , text="pressão",image=img_8 ,compound= LEFT ,width=130 ,height=50 ,relief='flat', overrelief='solid',anchor='nw', font=('Ivy 10 bold'), bg=co6, fg=co0)
b_8.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)

# direita
l_unidade_nome = Label(frame_direita, text='Unidades', width=16, height=2, padx=0, relief='groove', anchor='center', font=('Ivy 15 bold'), bg=co0, fg=co1)
l_unidade_nome.place(x=0, y=0)

l_d = Label(frame_direita, text='De',height=1, padx=3, relief='groove', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_d.place(x=10, y=70)

c_de = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold'))
c_de.place(x=38, y=70)

l_para = Label(frame_direita, text='Para',height=1, padx=3, relief='groove', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_para.place(x=100, y=70)

c_para = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold'))
c_para.place(x=140, y=70)


janela.mainloop()
