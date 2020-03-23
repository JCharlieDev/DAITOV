#******************************************************************************************#
# Codigo para DAITOV (Dispositivo de Asistencia Intercativo para la Terapia Ocupacional del Vestir
#
# Desarrollador: Karina Reyes
#
# Ultima actualizacion: 26 de febrero de 2020
#
# Version: 2.1
#******************************************************************************************#


#libreria para GUI
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#libreria para tablas
from tkintertable import TableCanvas, TableModel

#libreria para base de datos
import sqlite3
from sqlite3 import Error

#libreria para imagenes
import cv2

#libreria para audio
import pygame

#libreria tiempo
import time

tiempo_prendas=1
tiempo_broches=1




class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

        
class RegistrarUsuario(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.lbl_P=ttk.Label(self,text="Nombre del paciente:")
        self.lbl_P.grid(column=0,row=0)
        self.In_NombrePaciente=ttk.Entry(self)
        self.In_NombrePaciente.grid(column=1,row=0)

        self.lbl_PAP=ttk.Label(self,text="Apellido paterno del paciente:")
        self.lbl_PAP.grid(column=0,row=1)
        self.In_ApellidoPaterno=ttk.Entry(self)
        self.In_ApellidoPaterno.grid(column=1,row=1)


        self.lbl_PAM=ttk.Label(self,text="Apellido materno del paciente:")
        self.lbl_PAM.grid(column=0,row=2)
        self.In_ApellidoMaterno=ttk.Entry(self)
        self.In_ApellidoMaterno.grid(column=1,row=2)

        

        lbl_DV=ttk.Label(self,text="Género:")
        lbl_DV.grid(column=0,row=4)


        f0 = ttk.Frame(self, height=2, relief=SUNKEN)
        f0.grid(column=1,row=4)

        self.opcionGenero = IntVar()
        self.radG0=ttk.Radiobutton(f0, text="Masculino", variable=self.opcionGenero, value=0)#, command=seleccionar(1))
        self.radG1=ttk.Radiobutton(f0, text="Femenino", variable=self.opcionGenero, value=1)#, command=seleccionar(1))
        
        self.radG0.grid(column=0, row=1)
        self.radG1.grid(column=1, row=1)
        
        

        self.lbl_FN=ttk.Label(self,text="Fecha de nacimiento del paciente:")
        self.lbl_FN.grid(column=0,row=5)
        self.In_FechaNacimientoPaciente=ttk.Entry(self)
        self.In_FechaNacimientoPaciente.grid(column=1,row=5)

        self.lbl_T=ttk.Label(self,text="Nombre del terapeuta:")
        self.lbl_T.grid(column=0,row=6)
        self.In_NombreTerapeuta=ttk.Entry(self)
        self.In_NombreTerapeuta.grid(column=1,row=6)

        self.lbl_DC=ttk.Label(self,text="Nivel de discapacidad cognitiva:")
        self.lbl_DC.grid(column=0,row=7)
   
        #self.f1 =ttk. Frame(self)

        f1 = ttk.Frame(self, height=2, relief=SUNKEN)
        f1.grid(column=1,row=8)
        f2 = ttk.Frame(self)
        f2.grid(column=1,row=10)
        f3 = ttk.Frame(self)
        f3.grid(column=1,row=12)
        f4 = ttk.Frame(self)
        f4.grid(column=1,row=14)
        f5 = ttk.Frame(self)
        f5.grid(column=1,row=16)
        

        self.opcionDC = IntVar()
        self.radC0=ttk.Radiobutton(f1, text="Nulo", variable=self.opcionDC, value=0)#, command=seleccionar(1))
        self.radC1=ttk.Radiobutton(f1, text="Bajo", variable=self.opcionDC, value=1)#, command=seleccionar(1))
        self.radC2=ttk.Radiobutton(f1, text="Medio", variable=self.opcionDC, value=2)#, command=seleccionar(2))
        self.radC3=ttk.Radiobutton(f1, text="Alto", variable=self.opcionDC, value=3)#, command=seleccionar(3))
        self.radC0.grid(column=0, row=1)
        self.radC1.grid(column=1, row=1)
        self.radC2.grid(column=2, row=1)
        self.radC3.grid(column=3, row=1)

        lbl_DV=ttk.Label(self,text="Nivel de discapacidad visual:")
        lbl_DV.grid(column=0,row=9)

        
   
        self.opcionDV = IntVar()
        radV0=ttk.Radiobutton(f2, text="Nulo", variable=self.opcionDV, value=0)#, command=seleccionar(1))
        radV1=ttk.Radiobutton(f2, text="Bajo", variable=self.opcionDV, value=1)#, command=seleccionar(1))
        radV2=ttk.Radiobutton(f2, text="Medio", variable=self.opcionDV, value=2)#, command=seleccionar(2))
        radV3=ttk.Radiobutton(f2, text="Alto", variable=self.opcionDV, value=3)#, command=seleccionar(3))
        radV0.grid(column=0, row=1)
        radV1.grid(column=1, row=1)
        radV2.grid(column=2, row=1)
        radV3.grid(column=3, row=1)

    
        lbl_DA=ttk.Label(self,text="Nivel de discapacidad auditiva:")
        lbl_DA.grid(column=0,row=11)

        
    
        self.opcionDA = IntVar()
        radA0=ttk.Radiobutton(f3, text="Nulo", variable=self.opcionDA, value=0)#, command=seleccionar(1))
        radA1=ttk.Radiobutton(f3, text="Bajo", variable=self.opcionDA, value=1)#, command=seleccionar(1))
        radA2=ttk.Radiobutton(f3, text="Medio", variable=self.opcionDA, value=2)#, command=seleccionar(2))
        radA3=ttk.Radiobutton(f3, text="Alto", variable=self.opcionDA, value=3)#, command=seleccionar(3))
        radA0.grid(column=0, row=1)
        radA1.grid(column=1, row=1)
        radA2.grid(column=2, row=1)
        radA3.grid(column=3, row=1)

        lbl_DMG=ttk.Label(self,text="Nivel de discapacidad motriz gruesa:")
        lbl_DMG.grid(column=0,row=13)

        
    
        self.opcionDMG = IntVar() 
        radMG0=ttk.Radiobutton(f4, text="Nulo", variable=self.opcionDMG, value=0)#, command=seleccionar(1)) 
        radMG1=ttk.Radiobutton(f4, text="Bajo", variable=self.opcionDMG, value=1)#, command=seleccionar(1))
        radMG2=ttk.Radiobutton(f4, text="Medio", variable=self.opcionDMG, value=2)#, command=seleccionar(2))
        radMG3=ttk.Radiobutton(f4, text="Alto", variable=self.opcionDMG, value=3)#, command=seleccionar(3))
        radMG0.grid(column=0, row=1)
        radMG1.grid(column=1, row=1)
        radMG2.grid(column=2, row=1)
        radMG3.grid(column=3, row=1)

        lbl_DMF=ttk.Label(self,text="Nivel de discapacidad motriz fina:")
        lbl_DMF.grid(column=0,row=15)

        
    
        self.opcionDMF = IntVar() 
        radMF0=ttk.Radiobutton(f5, text="Nulo", variable=self.opcionDMF, value=0)#, command=seleccionar(1))
        radMF1=ttk.Radiobutton(f5, text="Bajo", variable=self.opcionDMF, value=1)#, command=seleccionar(1))
        radMF2=ttk.Radiobutton(f5, text="Medio", variable=self.opcionDMF, value=2)#, command=seleccionar(2))
        radMF3=ttk.Radiobutton(f5, text="Alto", variable=self.opcionDMF, value=3)#, command=seleccionar(3))
        radMF0.grid(column=0, row=1)
        radMF1.grid(column=1, row=1)
        radMF2.grid(column=2, row=1)
        radMF3.grid(column=3, row=1)

    
        self.btn_Registrar=ttk.Button(self, text="Registrar",command=self.Registrar_Datos)
        self.btn_Registrar.grid(column=3,row=17)

        self.btn_Cancelar=ttk.Button(self, text="Limpiar",command=self.Limpiar)
        self.btn_Cancelar.grid(column=4,row=17)

    
    
    def Limpiar(self):
        self.In_NombrePaciente.delete(0,tk.END)
        self.In_ApellidoPaterno.delete(0,tk.END)
        self.In_ApellidoMaterno.delete(0,tk.END)
        self.In_FechaNacimientoPaciente.delete(0,tk.END)
        self.In_NombreTerapeuta.delete(0,tk.END)

    def Registrar_Datos (self):
        conn = sqlite3.connect('C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Database//db_DAITOV.db')
        cursor = conn.cursor()
        Paciente_Nombre=self.In_NombrePaciente.get()
        Paciente_ApellidoP=self.In_ApellidoPaterno.get()
        Paciente_ApellidoM=self.In_ApellidoMaterno.get()
        
        if Paciente_Nombre!='':
            Paciente_Nombre=Paciente_Nombre.upper()
            Paciente_ApellidoP=Paciente_ApellidoP.upper()
            Paciente_ApellidoM=Paciente_ApellidoM.upper()
            

            FechaNac=self.In_FechaNacimientoPaciente.get()

            
            Terapeuta=self.In_NombreTerapeuta.get().upper()
            

            GeneroInt=self.opcionGenero.get()
            NivDC=self.opcionDC.get()
            NivDV=self.opcionDV.get()
            NivDA=self.opcionDA.get()
            NivDMF=self.opcionDMF.get()
            NivDMG=self.opcionDMG.get()

            Genero="F"
            if GeneroInt==0:
                Genero="M"
            
            cursor.execute("SELECT COUNT (*) FROM tb_Usuarios where Nombre='"+Paciente_Nombre+"' AND ApellidoPaterno='"+Paciente_ApellidoP+"' AND ApellidoMaterno='"+Paciente_ApellidoM+"';")
            rows = cursor.fetchall()
            for row  in rows:
                for data in row:
                    existe=data
                
    
            if existe==0:
                cursor.execute("SELECT COUNT (*) FROM tb_Usuarios ;")
                rows = cursor.fetchall()
                for row in rows:
                    for data in row:
                        dato=data
                        messagebox.showinfo(message="Datos "+ str(dato))
                    
                        if dato>0:
                            cursor.execute("SELECT MAX (ID_Usuario) FROM tb_Usuarios;" )
                            rows = cursor.fetchall()
                            for row in rows:
                                for columns in rows:
                                    for data in columns:
                                        #messagebox.showinfo(message="Data: "+ str(data))
                                        NEXT_ID=1+int(data)
                        else:
                            NEXT_ID=1
                        mensaje="INSERT INTO tb_Usuarios VALUES ("+str(NEXT_ID)+",'"+Paciente_Nombre+",'"+Paciente_ApellidoP+",'"+Paciente_ApellidoM+"','"+str(FechaNac)+"','"+Genero+"','"+Terapeuta+"',"+str(NivDC)+","+str(NivDV)+","+str(NivDA)+","+str(NivDMF)+","+str(NivDMG)+");"
                        datos_Usuario=[(NEXT_ID,Paciente_Nombre,Paciente_ApellidoP,Paciente_ApellidoM,FechaNac,Genero,NivDC,NivDV,NivDA,NivDMF,NivDMG,Terapeuta)]
                    
                        try:
                            messagebox.showinfo(message=datos_Usuario)
                        
                            try:
                                sql = '''INSERT INTO tb_Usuarios VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
                                cursor.executemany(sql, datos_Usuario)
                                messagebox.showinfo(message="Paciente Registrado con exito")
                                
                                self.Limpiar()
                            except sqlite3.IntegrityError as e:
                                messagebox.showinfo(message=('sqlite error: ',e.args[0]))# column name is not unique
                            conn.commit()


                        
                        
                        except Error as e:
                            messagebox.showinfo(message=e)
            else:
                messagebox.showinfo(message="Este registro ya existe")
            
        
    
        conn.close()



class VerUsuario(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        conn = sqlite3.connect('C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Database//db_DAITOV.db')
        cursor = conn.cursor()

        self.lbl_P=ttk.Label(self,text="Nombre del paciente:")
        self.lbl_P.place(x=0,y=0)

        #Mostrar la lista de datos disponibles
        lista=[]
        cursor.execute("SELECT Nombre,ApellidoPaterno,ApellidoMaterno FROM tb_Usuarios;" )
        rows = cursor.fetchall()
        
        
        for row in rows: 
            lista.append(row)
                
            

        self.combo = ttk.Combobox(self)
        self.combo["values"] = lista

        self.combo.place(x=120, y=0)
        
        self.greet_button = ttk.Button(
            self, text="Buscar Información", command=self.say_hello)
        self.greet_button.place(x=120,y=30)
        

        self.greet_label = ttk.Label(self)
        self.greet_label.pack()

        #Creacion de la tabla

        self.tframe = Frame(self)
        self. tframe.place(y=60)
        self.table = TableCanvas(self.tframe)
        self.table.show()

        self.table.model.columnlabels["1"] = "Fecha"
        self.table.model.columnlabels["2"] = "Actividad 1"
        self.table.model.columnlabels["3"] = "Actividad 2"
        self.table.model.columnlabels["4"] = "Actividad 3"
        self.table.model.columnlabels["5"] = "Actividad 4"
        self.table.model.columnlabels["6"] = "Errores"


        self.tframe1 = Frame(self)
        self. tframe1.place(y=350)
        self.tb_Resultados = TableCanvas(self.tframe1)
        self.tb_Resultados.show()

        self.tb_Resultados.model.columnlabels["1"] = "Prenda"
        self.tb_Resultados.model.columnlabels["2"] = "Conpletada"
        self.tb_Resultados.model.columnlabels["3"] = "Tiempo"
        self.tb_Resultados.model.columnlabels["4"] = "Número de Intentos"
        
        
        conn.close()
    
    def say_hello(self):
        self.greet_label["text"] = \
            "¡Hola, {}!".format(self.combo.get())

class ProgramarActividad(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        conn = sqlite3.connect('C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Database//db_DAITOV.db')
        cursor = conn.cursor()

        self.lbl_P=ttk.Label(self,text="Nombre del paciente:")
        self.lbl_P.place(x=10, y=0)
   

        #Mostrar la lista de datos disponibles
        lista=[]
        cursor.execute("SELECT Nombre,ApellidoPaterno,ApellidoMaterno FROM tb_Usuarios;" )
        rows = cursor.fetchall()

        for row in rows:
            lista.append(row)


        self.combonombre = ttk.Combobox(self,state="readonly")
        self.combonombre["values"] = lista
        self.combonombre.place(x=150, y=0)

        self.checkboxAuditivo_value = tk.BooleanVar(self)
        self.checkboxVisual_value = tk.BooleanVar(self)
        self.checkboxHaptica_value = tk.BooleanVar(self)
        

        self.lbl_Retro=ttk.Label(self,text="Retroalimentación:")
        self.lbl_Retro.place(x=10, y=20)

        self.checkboxAuditivo = ttk.Checkbutton(self, text="Auditiva",variable=self.checkboxAuditivo_value)
        self.checkboxAuditivo.place(x=40, y=40)

        self.checkboxVisual = ttk.Checkbutton(self, text="Visual",variable=self.checkboxVisual_value)
        self.checkboxVisual.place(x=40, y=60)

        self.checkboxHaptica = ttk.Checkbutton(self, text="Háptica",variable=self.checkboxHaptica_value)
        self.checkboxHaptica.place(x=40, y=80)

        #Seleccionar/ordenar actividades

        self.lbl_Retro=ttk.Label(self,text="Seleccionar actividades:")
        self.lbl_Retro.place(x=10, y=100)

        self.lbl_Calor=ttk.Label(self,text="Calor:")
        self.lbl_Calor.place(x=10, y=120)
        

        self.f1 = ttk.Frame(self, height=2, relief=SUNKEN)
        self.f1.place(x=60, y=120)

        self.opcionCalor = IntVar()
        self.radC0=ttk.Radiobutton(self.f1, text="No", variable=self.opcionCalor, value=0)#, command=seleccionar(1))
        self.radC1=ttk.Radiobutton(self.f1, text="1o", variable=self.opcionCalor, value=1)#, command=seleccionar(1))
        self.radC2=ttk.Radiobutton(self.f1, text="2o", variable=self.opcionCalor, value=2)#, command=seleccionar(2))
        self.radC3=ttk.Radiobutton(self.f1, text="3o", variable=self.opcionCalor, value=3)#, command=seleccionar(3))
        self.radC4=ttk.Radiobutton(self.f1, text="4o", variable=self.opcionCalor, value=4)#, command=seleccionar(3))
        self.radC0.grid(column=0, row=1)
        self.radC1.grid(column=1, row=1)
        self.radC2.grid(column=2, row=1)
        self.radC3.grid(column=3, row=1)
        self.radC4.grid(column=4, row=1)



        self.lbl_Calor=ttk.Label(self,text="Frio:")
        self.lbl_Calor.place(x=10, y=140)
        self.f2 = ttk.Frame(self, height=2, relief=SUNKEN)
        self.f2.place(x=60, y=140)

        self.opcionFrio = IntVar()
        self.radF0=ttk.Radiobutton(self.f2, text="No", variable=self.opcionFrio, value=0)#, command=seleccionar(1))
        self.radF1=ttk.Radiobutton(self.f2, text="1o", variable=self.opcionFrio, value=1)#, command=seleccionar(1))
        self.radF2=ttk.Radiobutton(self.f2, text="2o", variable=self.opcionFrio, value=2)#, command=seleccionar(2))
        self.radF3=ttk.Radiobutton(self.f2, text="3o", variable=self.opcionFrio, value=3)#, command=seleccionar(3))
        self.radF4=ttk.Radiobutton(self.f2, text="4o", variable=self.opcionFrio, value=4)#, command=seleccionar(3))
        self.radF0.grid(column=0, row=1)
        self.radF1.grid(column=1, row=1)
        self.radF2.grid(column=2, row=1)
        self.radF3.grid(column=3, row=1)
        self.radF4.grid(column=4, row=1)

        self.lbl_Calor=ttk.Label(self,text="Lluvia:")
        self.lbl_Calor.place(x=10, y=160)

        self.f3 = ttk.Frame(self, height=2, relief=SUNKEN)
        self.f3.place(x=60, y=160)

        self.opcionLluvia = IntVar()
        self.radL0=ttk.Radiobutton(self.f3, text="No", variable=self.opcionLluvia, value=0)#, command=seleccionar(1))
        self.radL1=ttk.Radiobutton(self.f3, text="1o", variable=self.opcionLluvia, value=1)#, command=seleccionar(1))
        self.radL2=ttk.Radiobutton(self.f3, text="2o", variable=self.opcionLluvia, value=2)#, command=seleccionar(2))
        self.radL3=ttk.Radiobutton(self.f3, text="3o", variable=self.opcionLluvia, value=3)#, command=seleccionar(3))
        self.radL4=ttk.Radiobutton(self.f3, text="4o", variable=self.opcionLluvia, value=4)#, command=seleccionar(3))
        self.radL0.grid(column=0, row=1)
        self.radL1.grid(column=1, row=1)
        self.radL2.grid(column=2, row=1)
        self.radL3.grid(column=3, row=1)
        self.radL4.grid(column=4, row=1)

        
        self.lbl_Calor=ttk.Label(self,text="Piyama:")
        self.lbl_Calor.place(x=10, y=180)

        self.f4 = ttk.Frame(self, height=2, relief=SUNKEN)
        self.f4.place(x=60, y=180)

        self.opcionPiyama = IntVar()
        self.radP0=ttk.Radiobutton(self.f4, text="No", variable=self.opcionPiyama, value=0)#, command=seleccionar(1))
        self.radP1=ttk.Radiobutton(self.f4, text="1o", variable=self.opcionPiyama, value=1)#, command=seleccionar(1))
        self.radP2=ttk.Radiobutton(self.f4, text="2o", variable=self.opcionPiyama, value=2)#, command=seleccionar(2))
        self.radP3=ttk.Radiobutton(self.f4, text="3o", variable=self.opcionPiyama, value=3)#, command=seleccionar(3))
        self.radP4=ttk.Radiobutton(self.f4, text="4o", variable=self.opcionPiyama, value=4)#, command=seleccionar(3))
        self.radP0.grid(column=0, row=1)
        self.radP1.grid(column=1, row=1)
        self.radP2.grid(column=2, row=1)
        self.radP3.grid(column=3, row=1)
        self.radP4.grid(column=4, row=1)

        
        self.greet_button = ttk.Button(
            self, text="Programar Actividad", command=self.ProgramarActividad1)
        self.greet_button.place(x=15,y=210)
        

        self.greet_label = ttk.Label(self)
        self.greet_label.pack()

        conn.close()
    
    def ProgramarActividad1(self):

        conn = sqlite3.connect('C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Database//db_DAITOV.db')
        cursor = conn.cursor()

        ID_Programacion=0
        
        cursor.execute("SELECT COUNT (*) FROM TB_ProgramacionTarea ;")
        rows = cursor.fetchall()
        for row in rows:
            for data in row:
                dato=data
                if dato>0:
                        cursor.execute("SELECT MAX (ID_Usuario) FROM tb_Usuarios;" )
                        rows = cursor.fetchall()
                        for row in rows:
                            for columns in rows:
                                for data in columns:
                                    ID_Programacion=1+int(data)
                else:
                        ID_Programacion=1

        USUARIO=self.combonombre.get()

        
        datos_Usuario=USUARIO.split()
        texto="SELECT ID_Usuario,Genero FROM TB_Usuarios WHERE Nombre= '"+datos_Usuario[0]+"' AND ApellidoPaterno= '"+datos_Usuario[1]+"' AND ApellidoMaterno= '"+datos_Usuario[2]+"' ;"
        cursor.execute(texto)
        rows = cursor.fetchall()
        contador=0
        for row in rows:
            for data in row:
                if contador==0:
                    ID_Usuario=str(data)
                    contador=1
                else:
                    Genero=str(data)


        Escenario="clima_"

        if Genero=="F":
            Escenario=Escenario+"niña"
        else:
            Escenario=Escenario+"niño"

        

        

        AV=self.checkboxVisual_value.get()
        AA=self.checkboxAuditivo_value.get()
        AH=self.checkboxHaptica_value.get()
        
        A1=""
        A2=""
        A3=""
        A4=""

        if self.opcionCalor.get()==1:
            A1="calor"
        else:
            if self.opcionLluvia.get()==1:
                A1="lluvia"
            else:
                if self.opcionFrio.get()==1:
                    A1="frio"
                else:
                    if self.opcionPiyama.get()==1:
                        A1="noche"
                        
        if self.opcionCalor.get()==2:
            A2="calor"
        else:
            if self.opcionLluvia.get()==2:
                A2="lluvia"
            else:
                if self.opcionFrio.get()==2:
                    A2="frio"
                else:
                    if self.opcionPiyama.get()==2:
                        A2="noche"
                        
        if self.opcionCalor.get()==3:
            A3="calor"
        else:
            if self.opcionLluvia.get()==3:
                A3="lluvia"
            else:
                if self.opcionFrio.get()==3:
                    A3="frio"
                else:
                    if self.opcionPiyama.get()==3:
                        A3="noche"

        if self.opcionCalor.get()==4:
            A4="calor"
        else:
            if self.opcionLluvia.get()==4:
                A4="lluvia"
            else:
                if self.opcionFrio.get()==4:
                    A4="frio"
                else:
                    if self.opcionPiyama.get()==4:
                        A4="noche"
        
            
        #self.greet_label["text"] = \
            #"INSERT INTO TB_actividades VALUES= {},{},{},{},{},{},{},{},{} !".format(ID_Programacion,ID_Usuario,Escenario,AA,AV,AH,A1,A2,A3,A4)
        
        datos_programacion=[(ID_Programacion,int(ID_Usuario),Escenario,AA,AV,AH,A1,A2,A3,A4)]
        print (datos_programacion)

        try:
            sql = '''INSERT INTO TB_ProgramacionTarea VALUES (?,?,?,?,?,?,?,?,?,?)''' #agregar datos programacion
            cursor.executemany(sql,datos_programacion)
            messagebox.showinfo(message="Tarea Registrado con exito")
            #self.Limpiar()
        except sqlite3.IntegrityError as e:
            messagebox.showinfo(message=('sqlite error: ',e.args[0]))# column name is not unique
        conn.commit()


        
class IniciarActividad(ttk.Frame):

    PSF=0#Prenda Superior Frio
    PSL=0#Prenda Superior Lluvia 
    PSC=0#Prenda Superior Calor
    PSN=0#Prenda Superior Noche
    PIF=0#Prenda Inferior Frio
    PIL=0#Prenda Inferior Lluvia 
    PIC=0#Prenda Inferior Calor
    PIN=0#Prenda Inferior Noche
    ZIF=0#Zapato Izquierdo Frio
    ZIL=0#Zapato Izquierdo Lluvia 
    ZIC=0#Zapato Izquierdo Calor
    ZDF=0#Zapato Derecho Frio
    ZDL=0#Zapato Derecho Lluvia 
    ZDC=0#Zapato Derecho Calor

    PSB1=0#Prenda Superior Broche 1
    PSB2=0#Prenda Superior Broche 2
    PSB3=0#Prenda Superior Broche 3
    
    PIB1=0#Prenda Inferior Broche 1

    ZDB1=0#Zapato Derecho Broche 1
    ZDB2=0#Zapato Derecho Broche 2
    ZDB3=0#Zapato Derecho Broche 3
    ZDB4=0#Zapato Derecho Broche 4

    ZIB1=0#Zapato Izquierdo Broche 1
    ZIB2=0#Zapato Izquierdo Broche 2
    ZIB3=0#Zapato Izquierdo Broche 3
    ZIB4=0#Zapato Izquierdo Broche 4
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.greet_button = ttk.Button(
            self, text="Iniciar Actividad", command=self.secuencia)
        self.greet_button.grid(column=0,row=1)


        image_inicio=tk.PhotoImage(file="C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Images//Inicio.png")
        background_label = tk.Label(self,image=image_inicio)
        background_label.photo = image_inicio
        background_label.grid(column=0,row=0)

    def Audio1(self,nombre_archivo):

        Archivo_audio="C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Audio//Dialogos//Intro//"+nombre_archivo+".mp3"
        Archivo_imagen="C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Images//Imagen//"+nombre_archivo+".png"


##        imagen=tk.PhotoImage(file=Archivo_imagen)
##        background_label = tk.Label(self,image=imagen)
##        background_label.photo = imagen
##        background_label.grid(column=0,row=0)
        
        pygame.mixer.init()
        pygame.mixer.music.load(Archivo_audio)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy() == True:


            continue
        

    def Audio2(self):    
        pygame.mixer.init()
        pygame.mixer.music.load("Vestirnos.mp3")
        pygame.mixer.music.play()
        i=0
        while pygame.mixer.music.get_busy() == True:
            if (i==0):
                image_hola=tk.PhotoImage(file="Vestirnos.png")
                background_label = tk.Label(self,image=image_hola)
                background_label.photo = image_hola
                background_label.grid(column=0,row=0)
                i=1
                
            continue

    def titulos(self,Prefijo, NumActividad,NumOportunidad,Indicador):

        texto=""
        numerico=NumActividad+NumOportunidad+Indicador
        if numerico<10:
            texto=Prefijo+"0"+str(numerico)
        else:
            texto=Prefijo+ str(numerico)

        return texto

    def revisarPrenda(self,Prefijo,Prenda):

        #Leer prendas

        P=0

        if Prenda=="Superior":
            P=self.PSL*1+self.PSC*2+self.PSF*4+self.PSN*8
        elif Prenda=="Inferior":
            P=self.PIL*1+self.PIC*2+self.PIF*4+self.PSN*8
        elif Prenda=="ZapatoIzquierdo":
            P=self.ZIL*1+self.ZIC*2+self.ZIF*4
        elif Prenda=="ZapatoDerecho":
            P=self.ZDL*1+self.ZDC*2+self.ZDF*4
        else:
            P=16 #Error
                        
        return P

   
    def revisarBroches(self,Prenda):

        #Leer entradas de broches de prendas

        if Prenda=="Superior":
            PSB=self.PSB1*1+self.PSB2*2+self.PSB3*4
            return PSB
        elif Prenda=="Inferior":
            PIB=self.PIB1
            return PIB
        elif Prenda=="ZapatoDerecho":
            ZDB=self.ZDB1*1+ZDB2*2+self.ZDB3*4+self.ZDB4*8
            return ZDB
        elif Prenda=="ZapatoIzquierdo":
            ZIB=self.ZIB1*1+ZIB2*2+self.ZIB3*4+self.ZIB4*8
            return ZIB
        else:
            return 16 #Error
        

    def ColocarPrenda (self,Prefijo,Prenda):

        Error=4
        Esperando=40
        RE=0#Resultado esperado de lectura de prendas
        REZI=0#Resultado esperado de lectura de zapato izquierdo
        REZD=0#Resultado esperado de lectura de zapato derecho

        if Prefijo=="L":
            RE=1
            REZI=8
            REZD=8
        elif Prefijo=="C":
            RE=2
            REZI=16
            REZD=16
        elif Prefijo=="F":
            RE=4
            REZI=32
            REZD=32
        else:
            RE=8
            
            

        if Prenda=="Superior":
            Error=5
            Esperando=7
        elif Prenda=="Inferior":
            Error=6
            Esperando=10
        
        elif Prenda=="zapato":
            Error=4
            Esperando=13

        else:

            if Prefijo=="L":
                RE=9
            elif Prefijo=="C":
                RE=18
            elif Prefijo=="F":
                RE=36
            
            
        
          

        OP=0#Oportunidad Prenda 

        P=self.revisarPrenda(Prefijo,Prenda)
        
        print("Resultados de Lectura de: ", Prenda,"-",Prefijo," P=" ,P)
        if (P==0):
            while (OP<3):# &  PS==0):
               #Revisamos si se coloco la prenda correcta
               P=self.revisarPrenda(Prefijo,Prenda)
               OP=OP+1
               if (P!=RE):
                        
                        #self.PSN=1 #provocar prenda equivocada
                        
                        #revisamos que no se haya colocado la prenda incorrecta
                        if (P>0):
                            titulo=self.titulos("E"+Prefijo, 0,0,OP)
                            print(titulo)
                            if OP==1:
                                titulo=self.titulos("E"+Prefijo, 0,Error,OP)
                                print(titulo)
                        #si no hay ninguna prenda colocada
                        else:
                            titulo=self.titulos(Prefijo, 0,Esperando,OP)
                            print(titulo)
                               

                        #self.Audio1(titulo)#Descripcion Prenda Superior
                        #Esperar 'x' Segundos a que coloque la prenda
                        time.sleep(tiempo_prendas)


        P=self.revisarPrenda(Prefijo,Prenda)
        PrendaColocada=0
        if (P==RE):
             PrendaColocada=1
                        
         
        
        return PrendaColocada

    def RevisarBroche(self,Prenda,BrochesListos):
        ResultadoBrochesListos=[(1,2,4,8),(3,5,6,9,10,12),(7,11,14),(15)];

        Listo=0
        #Leerbroches
        Lectura=self.revisarBroches(Prenda)

        #revisar si coincide con algun numero de ResultadoBrochesListos[BrochesListos]
        if Lectura in ResultadoBrochesListos[BrochesListos]:
            Listo=1
            
        return Listo

    def ColocarBrochesPrenda (self,Prefijo,CantidadBroches,Prenda):

        #Resultado de broche listo (0-> NO 1->SI)
        B1=0
        B2=0
        B3=0
        B4=0

        if Prenda=="Superior":
            Mensaje=17
        elif Prenda=="Inferior":
            Mensaje=20
        elif Prenda=="ZapatoDerecho":
            Mensaje=21 #Mensaje=23
        elif Prenda=="ZapatoIzquierdo":
            Mensaje=21 #Mensaje=23


            
        for NumeroBroche in range(CantidadBroches):
            print ("Numero de Broche ="+str(NumeroBroche))

            OB=0 #Oportunidad para abrochar el broche
            
            while (OB<4):
                OB=OB+1
                
                
                if (NumeroBroche==0):
                    Broche=self.RevisarBroche(Prenda,0)
                   
                
                elif(NumeroBroche==1):
                
                    if(B1==1):
                        Broche=self.RevisarBroche(Prenda,1)
                        #revisamos si hay dos broches listos
                    else:
                        Broche=self.RevisarBroche(Prenda,0)
                        #revisamos un broche

                    

                elif (NumeroBroche==2):
                    
                    if(B1*B2==1):
                        Broche=self.RevisarBroche(Prenda,2)
                        #revisamos si hay tres broches
                    elif (B1+B2==1):
                        Broche=self.RevisarBroche(Prenda,1)
                        #revisamos si hay dos broches
                    else:
                        Broche=self.RevisarBroche(Prenda,0)
                        #revisamos si hay un broche

                elif (NumeroBroche==3):
                    if (B1*B2*B3==1):
                        Broche=self.RevisarBroche(Prenda,3)
                        #revisamos si hay cuatro broches
                    elif (B1+B2+B3==2):
                        Broche=self.RevisarBroche(Prenda,2)
                        #revisamos si hay tres broches
                    elif (B1+B2+B3==1):
                        Broche=self.RevisarBroche(Prenda,1)
                        #revisamos si hay cuatro broches
                    else:
                        Broche=self.RevisarBroche(Prenda,0)
                        #revisamos si hay un broche
                        


##                if (OB<3):
##
##                        if(Broche<1):
##                            titulo=self.titulos(Prefijo, 0,Mensaje,NumeroBroche)
##                            print(titulo)
##                            #self.Audio1(titulo)#Descripcion Prenda Superior
##                            #Esperar 'x' Segundos a que coloque la prenda
##                            time.sleep(tiempo_broches)
##                        else:
##                            print("Guardar Broche logrado en la oportunidad", str(OB), "y en el tiempo", str(OB*5))
##                            #Mensaje de motivacion
##                        
##                            
##                else:
##                        if(Broche<1):
##                            print("Guardar broche no logrado")
##                        else:
##                            print("Guardar Broche logrado en la oportunidad 3 y en el tiempo maximo"
##                            #Mensaje de motivacion

                    
                    


        


    def secuencia(self):

##        #Saludo
        self.Audio1("I01")#Hola
        self.Audio1("I02")#Jugar
        self.Audio1("I03")#Vestirnos
        self.Audio1("I04")#Comencemos

         
        #Abrir base de datos
        conn = sqlite3.connect('C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Database//db_DAITOV.db')
        cursor = conn.cursor()
        rows = cursor.fetchall()



        #Leer Tarea
        Query="SELECT * FROM TB_ProgramacionTarea WHERE   ID_Programacion = (SELECT MAX(ID_Programacion)  FROM TB_ProgramacionTarea);" 

        cursor.execute(Query)
        rows = cursor.fetchall()


        
        for row  in rows:
            Id_Usuario=row[1]
            Escenario=row[2]
            #Apoyos activados
            ApoyoAuditivo=row[3]
            ApoyoVisual=row[4]
            ApoyoHaptico=row[5]
            #Leer las actividades
            lista_Actividades=[row[6],row[7],row[8],row[9]]
            print ("Id_Usuario=", Id_Usuario)
            print ("Escenario=", Escenario)
            print ("ApoyoAuditivo=", ApoyoAuditivo)
            print ("ApoyoVisual=", ApoyoVisual)
            print ("ApoyoHaptico=", ApoyoHaptico)
            print("Secuencia=",lista_Actividades)
                

        CA=0 #Contador de actividad
        #Realizar cada Actividad dentro de la tarea
        for Actividad in lista_Actividades:
            if Actividad != "":
                #Buscar Info de prendas

                CA=CA+1
                
                Query="SELECT * FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
                cursor.execute(Query)
                rows = cursor.fetchall()
                for row  in rows:
                    Actividad1=row[2]
                    PrendaSuperior=row[3]
                    PS_Cierre=row[4]
                    PS_NumCierres=row[5]
                    PrendaInferior=row[6]
                    PI_Cierre=row[7]
                    PI_NumCierres=row[8]
                    Zapato=row[9]
                    Z_Cierre=row[10]
                    Z_NumCierres=row[11]

#################################################################
####################### Inicio de Actividad (print en pantalla)  ##########################################

            #Iniciar Actividad
                    
            
            Prefijo=""

            if Actividad=="noche":
                Prefijo="N"
            elif Actividad=="calor":
                Prefijo="C"
            elif Actividad=="frio":
                Prefijo="F"
            else:
                Prefijo="L"


            #Encender luz
            if ApoyoVisual==1:
                if Prefijo=="N":
                    print ("encender foco noche")
                elif Prefijo=="C":
                    print ("encender foco calor")
                elif Prefijo=="F":
                    print ("encender foco frio")
                else:
                    print("encender foco lluvia")
                    
            
            #Encender apoyo haptico
            if ApoyoHaptico==1:
                if Prefijo=="C":
                    print ("encender calentón")
                elif Prefijo=="F":
                    print ("encender abanico")
                else:
                    print("encender aspersor")

            #Anunciar la actividad
            if Prefijo!="N":
                titulo=self.titulos(Prefijo, CA,0,0)
            else:
                titulo=self.titulos(Prefijo, 0,1,0)
##            self.Audio1(titulo)#Clima
            print (titulo)
            
                

            

            #Quitar la ropa anterior
            if CA>1:
                print("quitar ropa anterior")
                

            #Describir atuendo
            titulo=self.titulos(Prefijo, 0,4,0)
##            self.Audio1(titulo)#?Me ayudas?
            print (titulo)

            titulo=self.titulos(Prefijo, 0,5,0)
##            self.Audio1(titulo)#Necesitamos prenda Superior
            print (titulo)

            titulo=self.titulos(Prefijo, 0,6,0)
##            self.Audio1(titulo)#Necesitamos prenda Inferior
            print (titulo)

            if Prefijo!="N":
                titulo=self.titulos(Prefijo, 0,7,0)
##                self.Audio1(titulo)#Necesitamos zapatos
            print (titulo)

##            **************************************************************************************************************
            #Prenda Superior

            #revisar si el atuendo lleva prenda Superior
            Query="SELECT PS FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
            cursor.execute(Query)
            rows = cursor.fetchall()
            for row  in rows:
                 #print ("Tipo de prenda="+ str(row[0]))
                 Prenda=row[0]

            if (Prenda!=""):
                 #Colocar prenda Superior
                PS=self.ColocarPrenda(Prefijo,"Superior")

                PS=1#BORRAR**
                if PS==1:
                     print("La prenda Superior para: "+ Prefijo +" se ha colocado correctamente")

                 #Revisar la cantidad de broches mediante query
                Query="SELECT PSNC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
                cursor.execute(Query)
                rows = cursor.fetchall()
                for row  in rows:
                    print ("numero de broches="+ str(row[0]))
                    CantidadBroches=row[0]
             
                if PS==1:
                    #Abrochar prenda
                    self.ColocarBrochesPrenda(Prefijo,CantidadBroches,"Superior")
                    
             
##            **************************************************************************************************************
            #Prenda Inferior
            
            Query="SELECT PI FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
            cursor.execute(Query)
            rows = cursor.fetchall()
            for row  in rows:
                print ("Tipo de prenda="+ str(row[0]))
                Prenda=row[0]

            if (Prenda!=""):

                #Colocar prenda Superior
                PI=self.ColocarPrenda(Prefijo,"Inferior")

                PI=1#BORRAR**
                if PI==1:
                     print("La prenda Inferior para: "+ Prefijo +" se ha colocado correctamente")


                 #Revisar la cantidad de broches mediante query
                Query="SELECT PINC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
                cursor.execute(Query)
                rows = cursor.fetchall()
                for row  in rows:
                    print ("numero de broches en PI="+ str(row[0]))
                    CantidadBroches=row[0]
             
                if PI==1:
                    self.ColocarBrochesPrenda(Prefijo,CantidadBroches,"Inferior")

            #Zapato1

            #revisar si el atuendo lleva prenda Zapatos
            Query="SELECT Z FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
            cursor.execute(Query)
            rows = cursor.fetchall()
            for row  in rows:
                 print ("Tipo de prenda="+ str(row[0]))
                 Prenda=row[0]

            if (Prenda!=""):
                 #Colocar primer zapatos
                Z=self.ColocarPrenda(Prefijo,"zapato")

                #Leer zapato Derecho e Izquierdo
                ZD=1#BORRAR**
                ZI=1#BORRAR**

                
                
                if ZD==1:
                     print("El zapato para: "+ Prefijo +" se ha colocado correctamente")
                elif ZD==1:
                     print("El zapato para: "+ Prefijo +" se ha colocado correctamente")

                 #Revisar la cantidad de broches mediante query
                Query="SELECT ZNC FROM TB_ACTIVIDADES WHERE   Escenario = '"+ Escenario + "' AND Actividad = '"+ Actividad +"'"
                cursor.execute(Query)
                rows = cursor.fetchall()
                for row  in rows:
                    print ("numero de broches="+ str(row[0]))
                    CantidadBroches=row[0]
             
                if ZI==1:
                    #Abrochar prenda
                    print("Abrochar zapato Izquierdo")
                    #self.ColocarBrochesPS(Prefijo,CantidadBroches,"zapato")
                elif ZD==1:

                    print("Abrochar zapato Derecho ")
                    

            

            #Apagar apoyo haptico
            print ("Apagar todos los apoyos hápticos")

            #A jugar
                
####################### Fin de de Actividad (print en pantalla)  ##########################################




        
        
 

class AboutFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        background_image=tk.PhotoImage(file="C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Images//Inicio.png")
        background_label = tk.Label(self, image=background_image)
        background_label.photo = background_image
        background_label.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Versión 2.0 ")
        self.label.pack()
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Silvia Karina Reyes Lio ")
        self.label.pack()


        self.label = ttk.Label(self)
        self.label["text"] = ("Instituto Tecnológico de Ensenada")
        self.label.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Maestría en Ciencias en Ingeniería Mecatrónica")
        self.label.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Sistemas Cognitivos")
        self.label.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Dir. Dra. Cristina Ramírez Fernández")
        self.label.pack()


        self.label = ttk.Label(self)
        self.label["text"] = ("Co Dir. Dr. Ismael Hernández Capuchin")
        self.label.pack()
 


class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)


        
        
        self.notebook = ttk.Notebook(self,width=800,height=500)
        
        
        self.RegistrarUsuario = RegistrarUsuario(self.notebook)
        self.notebook.add(
            self.RegistrarUsuario, text="Registrar Usuario", padding=5)
        
        self.VerUsuario = VerUsuario(self.notebook)
        self.notebook.add(
            self.VerUsuario, text="Ver Info Usuario", padding=5)

        self.ProgramarActividad = ProgramarActividad(self.notebook)
        self.notebook.add(
            self.ProgramarActividad, text="Programar Tarea", padding=5)

        self.IniciarActividad = IniciarActividad(self.notebook)
        self.notebook.add(
            self.IniciarActividad, text="Iniciar Tarea", padding=5)

        self.AboutFrame = AboutFrame(self.notebook)
        self.notebook.add(
            self.AboutFrame, text="Acerca de", padding=5)    
        
        self.notebook.pack(padx=1, pady=1)
        self.pack()




main_window = tk.Tk()
bit = main_window.iconbitmap('C://Users//MSI//Desktop//GitHub Repos//DAITOV//Resources//Images//DaitovIcon.ico')
main_window.title("DAITOV")
FullScreenApp(main_window)
app = Application(main_window)
app.mainloop()