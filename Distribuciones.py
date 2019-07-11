# Modulos
import scipy.stats as Static
import numpy as np
import tkinter as Tk
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import  ttk
from PIL import Image, ImageTk

########################### DISTRIBUCIONES DISCRETAS ########################### 

def Poisson(media):
	# mu: Media
	mu =  float(media.get()) # parametro de forma 
	poisson = Static.poisson(mu) # Distribución
	x = np.arange(poisson.ppf(0.01),poisson.ppf(0.99))
	fmp = poisson.pmf(x) # Función de Masa de Probabilidad
	plt.plot(x, fmp, '--')
	plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
	plt.title('Distribución Poisson')
	plt.ylabel('Probabilidad')
	plt.xlabel('Valores')
	plt.show()

def Binomial(proba,num):
	# p: Probabilidad de exito
	# N: Numero de ensayos 
	N = int(num.get())
	p = float(proba.get())
	binomial = Static.binom(N, p) # Metodo de scipy.stats que devuelve un probabilidad binomial
	x = np.arange(binomial.ppf(0.01),binomial.ppf(0.99)) #Arreglo del eje de las x desde 0.01 a 0.99
	fmp = binomial.pmf(x) # Función de Masa de Probabilidad sacada desde el arreglo del eje de las x
	plt.plot(x, fmp, '--') # Graficando la distribucion en base a la Funcion de Masa de Probabilidad
	#Personalizacion de la grafica
	plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
	plt.title('Distribución Binomial')
	plt.ylabel('Probabilidad')
	plt.xlabel('Valores')
	plt.show() # Muestra Grafica

def Geometrica(proba):
	# p: Probabilidad de Exito
	p =  float(proba.get()) # parametro de forma 
	geometrica = Static.geom(p) # Distribución
	x = np.arange(geometrica.ppf(0.01),geometrica.ppf(0.99))
	fmp = geometrica.pmf(x) # Función de Masa de Probabilidad
	plt.plot(x, fmp, '--')
	plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
	plt.title('Distribución Geométrica')
	plt.ylabel('Probabilidad')
	plt.xlabel('Valores')
	plt.show()

def HiperGeometrica(Me,ne,Ne):
	# n: Conjunto de elementos con exito 
	# M: Conjunto Total
	# N: Muestra de N elementos
	n = int(ne.get())
	M = int(Me.get())
	N = int(Ne.get())
	hipergeometrica = Static.hypergeom(M, n, N) # Distribución
	x = np.arange(0, n+1)
	fmp = hipergeometrica.pmf(x) # Función de Masa de Probabilidad
	plt.plot(x, fmp, '--')
	plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
	plt.title('Distribución Hipergeométrica')
	plt.ylabel('Probabilidad')
	plt.xlabel('Valores')
	plt.show()

def Bernoulli():
	# Solo demuestra que hay 50% de exito y 50% de fracaso
	# p: Probabilidad de Exito
	p =  0.5 # parametro de forma 
	bernoulli = Static.bernoulli(p)
	x = np.arange(-1, 3)
	fmp = bernoulli.pmf(x) # Función de Masa de Probabilidad
	fig, ax = plt.subplots()
	ax.plot(x, fmp, 'bo')
	ax.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
	ax.set_yticks([0., 0.2, 0.4, 0.6, 0.8, 1])
	plt.title('Distribución Bernoulli')
	plt.ylabel('Probabilidad')
	plt.xlabel('Valores')
	plt.show()

########################### DISTRIBUCIONES CONTINUAS ###########################

def Normal(media,sig):
	# mu: Media
	# sigma: Desviacion Estandar
	mu = float(media.get())
	sigma = float(sig.get()) 
	normal = Static.norm(mu, sigma)
	x = np.linspace(normal.ppf(0.01),normal.ppf(0.99), 100)
	fp = normal.pdf(x) # Función de Probabilidad
	plt.plot(x, fp)
	plt.title('Distribución Normal')
	plt.ylabel('Probabilidad')
	plt.xlabel('valores')
	plt.show()

def Uniforme():
	uniforme = Static.uniform()
	x = np.linspace(uniforme.ppf(0.01),uniforme.ppf(0.99), 50)
	fp = uniforme.pdf(x) # Función de Probabilidad
	fig, ax = plt.subplots()
	ax.plot(x, fp, '--')
	ax.vlines(x, 0, fp, colors='b', lw=5, alpha=0.5)
	ax.set_yticks([0., 0.2, 0.4, 0.6, 0.8, 1., 1.2])
	plt.title('Distribución Uniforme')
	plt.ylabel('Probabilidad')
	plt.xlabel('Valores')
	plt.show()

def Exponencial():
	# No recibe parametros
	exponencial = Static.expon()
	x = np.linspace(exponencial.ppf(0.01),exponencial.ppf(0.99), 100)
	fp = exponencial.pdf(x) # Función de Probabilidad
	plt.plot(x, fp)
	plt.title('Distribución Exponencial')
	plt.ylabel('Probabilidad')
	plt.xlabel('Valores')
	plt.show()

########################### DISTRIBUCIONES INFO ###########################

def InfoPoi():
	Ventana1 = Tk()
	Ventana1.title("Distribución Poisson")
	Ventana1.geometry("980x400")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/poi.png")
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=0,y=0)
	Ventana1.mainloop()

def InfoBi():
	Ventana1 = Tk()
	Ventana1.title("Distribución Binomial")
	Ventana1.geometry("968x282")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/bi.png")
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=0,y=0)
	Ventana1.mainloop()

def InfoGeo():
	Ventana1 = Tk()
	Ventana1.title("Distribución Geométrica")
	Ventana1.geometry("960x310")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/geo.png")
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=0,y=0)
	Ventana1.mainloop()

def InfoHiper():
	Ventana1 = Tk()
	Ventana1.title("Distribución Hipergeométrica")
	Ventana1.geometry("985x535")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/hiper.png")
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=0,y=0)
	Ventana1.mainloop()

def InfoNor():
	Ventana1 = Tk()
	Ventana1.title("Distribución Normal")
	Ventana1.geometry("965x290")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/nor.png")
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=0,y=0)
	Ventana1.mainloop()

def InfoBer():
	Ventana1 = Tk()
	Ventana1.title("Distribución Bernoulli")
	Ventana1.geometry("964x345")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/ber.png")
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=0,y=0)
	Bernoulli()
	Ventana1.mainloop()

def InfoUni():
	Ventana1 = Tk()
	Ventana1.title("Distribución Uniforme")
	Ventana1.geometry("730x445")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/uni.png")
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=0,y=0)
	Uniforme()
	Ventana1.mainloop()

def InfoExp():
	Ventana1 = Tk()
	Ventana1.title("Distribución Exponencial")
	Ventana1.geometry("960x284")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/exp.png")
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=0,y=0)
	Exponencial()
	Ventana1.mainloop()

########################### PESTANAS DE LA GUI ###########################

def Pois(Poi):
	titulo = Label(Poi,text="Distribución Poisson",font=("Arial",24)).place(x=40,y=15)
	consi = Label(Poi,text="Valores para su funcionamiento son números enteros o reales").place(x=40,y=55)
	info = Button(Poi,text="Info",command=InfoPoi).place(x=490,y=20)
	media = StringVar()
	media.set("3.6")
	etiqueta = Label(Poi,text="Media (μ): ").place(x=80,y=110)
	entrada = Entry(Poi,width=10,textvariable= media).place(x=160,y=110)
	#Intento de Atrapar excepcion
	try:
		float(media.get())
	except Exception as e:
		error = Label(Poi,text="Error").place(x=10,y=10)
	else:
		btn = Button(Poi,text="Graficar",command=lambda : Poisson(media)).place(x=300,y=105) #Para pasar argumentos en una funcion

def Bino(Bi):
	titulo = Label(Bi,text="Distribución Binomial",font=("Arial",24)).place(x=40,y=0)
	consi = Label(Bi,text="Valores para su funcionamiento son números: ").place(x=40,y=35)
	co = Label(Bi,text=" -Reales entre 1 y 0 para la probabilidad").place(x=40,y=55)
	c = Label(Bi,text=" -Enteros para el número de ensayos").place(x=40,y=75)
	info = Button(Bi,text="Info",command=InfoBi).place(x=490,y=20)
	proba = StringVar()
	proba.set("0.4")
	etiqueta = Label(Bi,text="Probabilidad de Éxito: ").place(x=60,y=110)
	entrada = Entry(Bi,width=10,textvariable= proba).place(x=210,y=110)
	num = StringVar()
	num.set("30")
	etiqueta2 = Label(Bi,text="Numero de Ensayos: ").place(x=60,y=140)
	entrada2 = Entry(Bi,width=10,textvariable= num).place(x=210,y=140)
	btn = Button(Bi,text="Graficar",command=lambda : Binomial(proba,num)).place(x=360,y=120) #Para pasar argumentos en una funcion

def Geo(Geome):
	titulo = Label(Geome,text="Distribución Geométrica",font=("Arial",24)).place(x=40,y=15)
	consi = Label(Geome,text="Valores para su funcionamiento son números reales entre 1 y 0").place(x=40,y=55)
	info = Button(Geome,text="Info",command=InfoGeo).place(x=490,y=20)
	proba = StringVar()
	proba.set("0.3")
	etiqueta = Label(Geome,text="Probabilidad de Éxito: ").place(x=40,y=100)
	entrada = Entry(Geome,width=10,textvariable= proba).place(x=180,y=100)
	btn = Button(Geome,text="Graficar",command=lambda : Geometrica(proba)).place(x=310,y=95) #Para pasar argumentos en una funcion

def HiperGeo(Hiper):
	#Titulo e info
	titulo = Label(Hiper,text="Distribución Hipergeométrica",font=("Arial",24)).place(x=40,y=15)
	consi = Label(Hiper,text="Valores para su funcionamiento son números enteros").place(x=40,y=55)
	info = Button(Hiper,text="Info",command=InfoHiper).place(x=490,y=20)

	M = StringVar()
	M.set("30")
	etiqueta = Label(Hiper,text="Conjunto Total: ").place(x=60,y=80)
	entrada = Entry(Hiper,width=10,textvariable= M).place(x=210,y=80)
	n = StringVar()
	n.set("12")
	etiqueta2 = Label(Hiper,text="Conjunto de Éxitos: ").place(x=60,y=110)
	entrada2 = Entry(Hiper,width=10,textvariable= n).place(x=210,y=110)
	N = StringVar()
	N.set("10")
	etiqueta3 = Label(Hiper,text="Conjunto Muestra: ").place(x=60,y=140)
	entrada3 = Entry(Hiper,width=10,textvariable= N).place(x=210,y=140)
	btn = Button(Hiper,text="Graficar",command=lambda : HiperGeometrica(M,n,N)).place(x=360,y=105) #Para pasar argumentos en una funcion
	
def Normalita(No):
	titulo = Label(No,text="Distribución Normal",font=("Arial",24)).place(x=40,y=15)
	consi = Label(No,text="Valores para su funcionamiento son números reales y/o enteros").place(x=40,y=55)
	info = Button(No,text="Info",command=InfoNor).place(x=490,y=20)
	media = StringVar()
	media.set("0")
	etiqueta = Label(No,text="Media (μ): ").place(x=60,y=100)
	entrada = Entry(No,width=10,textvariable= media).place(x=210,y=100)
	sigma = StringVar()
	sigma.set("0.2")
	etiqueta2 = Label(No,text="Desviación Estándar: ").place(x=60,y=130)
	entrada2 = Entry(No,width=10,textvariable= sigma).place(x=210,y=130)
	btn = Button(No,text="Graficar",command=lambda : Normal(media,sigma)).place(x=360,y=110) #Para pasar argumentos en una funcion


def NA_Para(NA):
	titulo = Label(NA,text="Distribuciones",font=("Arial",24)).place(x=190,y=15)
	consi = Label(NA,text="Para ver el comportamiento de las distribuciones pulse el botón correspondiente").place(x=40,y=55)
	Berno = Button(NA,text="Bernoulli",command=InfoBer).place(x=20,y=100)
	Uni = Button(NA,text="Uniforme",command=InfoUni).place(x=245,y=100)
	Exp = Button(NA,text="Exponencial",command=InfoExp).place(x=450,y=100)

########################### CREDITOS ###########################

def Creditos():
	Ventana1 = Tk()
	Ventana1.title("Créditos")
	Ventana1.geometry("500x200")
	Ventana1.resizable(width=False,height=False)
	im = Image.open("Info/proteco.png")
	im = im.resize((100,100),Image.ANTIALIAS)
	ph = ImageTk.PhotoImage(im,master=Ventana1)
	label = Label(Ventana1,image=ph).place(x=20,y=20)
	MARIO = Label(Ventana1,text="Mario Alberto Vásquez Cancino ").place(x=140,y=35)
	MARIO1 = Label(Ventana1,text="Becario PROTECO Generación 37").place(x=160,y=55)
	MARIO2 = Label(Ventana1,text="Unánse al programa está super padre :)").place(x=140,y=75)
	PROTECO = Label(Ventana1,text="Info en Facebook: Proteco").place(x=160,y=95)

	RAUL = Label(Ventana1,text="Agradecimientos especiales a Raul E. Lopez Briega:").place(x=20,y=140)
	RAUL1 = Label(Ventana1,text="-Por tan buen blog, base para poder realizar este programa.").place(x=40,y=160)
	Ventana1.mainloop()

########################### PESTANA DE BIENVENIDA ###########################

def Welcome(Bienvenido):
	titulo = Label(Bienvenido,text="Bienvenido",font=("Arial",24)).place(x=40,y=15)
	consi = Label(Bienvenido,text="Este programa educativo y de licencia libre, te permitirá descubrir el compor-").place(x=40,y=55)
	consi1 = Label(Bienvenido,text="tamiento de algunas de las distribuciones más importantes de probabilidad").place(x=40,y=75)
	consi2 = Label(Bienvenido,text="y estadística.").place(x=40,y=95)	
	enjoy = Label(Bienvenido,text="Disfrútalo",font=("Verdana",20)).place(x=40,y=120)
	cre = Button(Bienvenido,text="Créditos",command=Creditos).place(x=470,y=128)

########################### GUI ###########################

Ventana = Tk()
Ventana.title("Distribuciones de Probabilidad")
Ventana.geometry("573x200")
Ventana.resizable(width=False,height=False)
Pestanas = ttk.Notebook(Ventana)
Pestanas.pack(fill="both",expand="yes") #Las ventanas se van a expandir en toda la ventana

#Creando pestanas
Bienvenido = ttk.Frame(Pestanas)
Poi = ttk.Frame(Pestanas)
Bi = ttk.Frame(Pestanas)
Geome = ttk.Frame(Pestanas)
Hiper = ttk.Frame(Pestanas)
No = ttk.Frame(Pestanas)
NA = ttk.Frame(Pestanas)
Pestanas.add(Bienvenido,text="Bienvenido")
Pestanas.add(Poi,text="Poisson")
Pestanas.add(Bi,text="Binomial")
Pestanas.add(Geome,text="Geométrica")
Pestanas.add(Hiper,text="Hipergeométrica")
Pestanas.add(No,text="Normal")
Pestanas.add(NA,text="Sin Parámetros")

Welcome(Bienvenido)
Pois(Poi)
Bino(Bi)
Geo(Geome)
HiperGeo(Hiper)
Normalita(No)
NA_Para(NA)

Ventana.mainloop()
