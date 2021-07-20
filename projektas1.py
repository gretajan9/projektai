import os, random, string
from tkinter import *

def SlaptazodzioGeneratorius():
    slaptazodis= ""
    lowercase= 'abcdefghijklmnopqrstuvwxyz'
    uppercase= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + lowercase
    mix= '0123456789'+lowercase+uppercase+'@#$%&*'
    c1 = Entry(langas, font=('Arial', 14), width=10)

    if v.get()==1:
        for i in range(0, 6):
            slaptazodis= slaptazodis + random.choice(lowercase)
    elif v.get()== 2:
        for i in range(0, 10):
            slaptazodis =slaptazodis+random.choice(uppercase)
    else:
        for i in range(0, 16):
            slaptazodis =slaptazodis+random.choice(mix)


    rezultatas["text"] = slaptazodis


langas= Tk()
langas.geometry ('600x400')

virsutinis = Frame(langas)


pavadinimas = Label(langas, text= "Iveskite slaptazodi")
laukas = Entry(langas)


pagrindinisPavadinimas = Label(langas ,text='Slaptazodzio generatorius',font=('Arial',30),fg='Black')
pagrindinisPavadinimas.config(anchor=CENTER)
pagrindinisPavadinimas.pack()
t2 = Label(langas,text='slaptazodis:',font=('Arial',14),background ="blue")

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

pasirinkimai = [("Low Strength", 1), ("Medium Strenght", 2), ("High Strength", 3)]

def ShowChoice():
    print(v.get())

tekstas = Label(langas,
         text="Pasirinkti slaptazodzio stiprumo lygi:",
         padx = 20).pack()

for pasirinkimas, val in pasirinkimai:
    choice = Radiobutton(langas,
                   text=pasirinkimas,
                   justify=LEFT,
                   padx = 20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(side = 'top', anchor = 'w')


mygtukas = Button (virsutinis, text= "Generuoti", command= SlaptazodzioGeneratorius)
mygtukas.pack(side=BOTTOM)
rezultatas= Label(langas, text= "")
rezultatas.pack()

virsutinis.pack()
langas.mainloop()