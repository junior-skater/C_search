import requests
import json
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

global Cedula
global valores
global diccionario

class acciones():


	def verificar(self):
		global Cedula
		self.Num=cedula.get()
		self.Num2=[x for x in self.Num if x.isdigit() == True]
		self.Cedula=str(''.join(self.Num2))
	
	def peticion(self):
		global valores
		global diccionario
		parametro={"cedula":self.Cedula}
		url='https://api.adamix.net/apec/cedula/'
		self.response=requests.get(url+self.Cedula)
		self.diccionario=self.response.json()
		self.valores=self.diccionario.values()
		valores=list(self.valores)
		diccionario=self.diccionario

	def Ced(self,num,N1,N2,N3,Birth,Bplace,sex,EC,IDCO):
		raiz=Toplevel()
		raiz.title("CEDULA")
		raiz.iconbitmap('hola.ico')
		Frame(raiz, width=400, height=350, bg="#F0D58C").pack(fill="both", expand=True)
		raiz.resizable(0,0)
		Label(raiz, font="Impact 14", text='Republica Dominicana', bg='#F0D58C').place(x="125",y="1")
		Label(raiz, font="Impact 13", text='Junta Central Electoral', bg='#F0D58C').place(x="130",y="25")
		Label(raiz, font="Impact 12", text='Cedula de identidad y electoral', bg='#F0D58C').place(x="110",y="50")
		Label(raiz, font="TimesNewRoman 12", text=num, bg='#F0D58C').place(x="180",y="95")
		Label(raiz, font="Impact 11", text='Lugar de nacimiento:', bg='#F0D58C').place(x="180",y="130")
		Label(raiz, font="TimesNewRoman 10", text=Bplace, bg='#F0D58C').place(x="180",y="150")
		Label(raiz, font="Impact 11", text='Fecha de nacimiento:', bg='#F0D58C').place(x="180",y="170")
		Label(raiz, font="TimesNewRoman 10", text=Birth, bg='#F0D58C').place(x="180",y="190")
		Label(raiz, font="Impact 11", text='Sexo:', bg='#F0D58C').place(x="180",y="210")
		Label(raiz, font="TimesNewRoman 10", text=sex, bg='#F0D58C').place(x="180",y="230")
		Label(raiz, font="Impact 11", text="Estado civil", bg='#F0D58C').place(x="180",y="250")
		Label(raiz, font="TimesNewRoman 10", text=EC, bg='#F0D58C').place(x="180",y="270")
		Label(raiz, font="Impact 11", text="IDColegio", bg='#F0D58C').place(x="180",y="290")
		Label(raiz, font="TimesNewRoman 10", text=IDCO, bg='#F0D58C').place(x="180",y="310")
		Label(raiz, font="TimesNewRoman 10", text=N1, bg='#F0D58C').place(x="5",y="290")
		Label(raiz, font="TimesNewRoman 10", text=N2, bg='#F0D58C').place(x="5",y="310")
		Label(raiz, font="TimesNewRoman 10", text=N3, bg='#F0D58C').place(x="45",y="310")
		photo=ImageTk.PhotoImage(Image.open("foto.jpg"))
		Label(raiz, image=photo).place(x="5",y="80")
		raiz.mainloop()
ACN=acciones()

raiz=Tk()
def Boton():
	ACN.verificar()
	ACN.peticion()
	global valores
	global diccionario
	num,N1,N2,N3,Birth,Bplace,EC,IDCO=[valores[i] for i in (0,1,2,3,4,5,8,12)]
	sex=diccionario['IdSexo']
	pic=diccionario['foto']
	#EC=diccionario['']
	nomfoto=("foto.jpg")
	imagen=requests.get(pic).content
	with open(nomfoto, "wb") as handler:
		handler.write(imagen)
	ACN.Ced(num,N1,N2,N3,Birth,Bplace,sex,EC,IDCO)

raiz.title("Welcome to C-search")
raiz.iconbitmap('hola.ico')
Frame(raiz, width=500, height=300, bg="#a4bbab").pack(fill="both", expand=True)
raiz.resizable(0,0)
Label(raiz, font="Impact 22", text='introduzca el numero', bg='#a4bbab').place(x="100",y="20")
Label(raiz, font="Impact 22", text='de cedula que desea verificar:', bg='#a4bbab').place(x="60",y="60")
cedula=Entry(raiz, font="14", justify="center")
cedula.place(x="50",y="200")
BT=Button(raiz, text="verificar", font="Impact 14", command=Boton).place(x="350",y="190")
raiz.mainloop()

