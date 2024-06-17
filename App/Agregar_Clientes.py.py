import tkinter as tk

#importando los módulos de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *
from Conexion import *


class FormularioMarket:
      
 global base
 base = None
      
 global texBoxIDCliente
 texBoxId = None
 
 global texBoxDNI
 texBoxDNI = None
 
 global texBoxApellido_Nombre
 texBoxApellido_Nombre = None
 
 global texBoxMail
 texBoxMail = None
 
 global texBoxTelefono
 texBoxTelefono = None
 
 global textBoxDireccion
 texBoxDireccion = None
  
 
 
def Formulario():
 global texBoxIDCliente
 global texBoxDNI
 global texBoxApellido_Nombre
 global texBoxMail
 global texBoxTelefono
 global texBoxDireccion
 global base
 global groupBox
 global tree 
 
 try: 
      base = Tk()
      base.geometry("1200x300")
      base.title("Formulario MARKET cba") 
            
      groupBox = LabelFrame(base,text="Datos de Cliente", padx=5,pady=5)
      groupBox.grid(row=0,column=0,padx=10,pady=10)
            
      labelIDCliente=Label(groupBox,text="IDCliente:",width=13,font=("arial",12)).grid(row=0,column=0)
      texBoxIDCliente = Entry(groupBox)
      texBoxIDCliente.grid(row=0,column=1)
            
      labelDNI=Label(groupBox,text="DNI:",width=13,font=("arial",12)).grid(row=1,column=0)
      texBoxDNI = Entry(groupBox)
      texBoxDNI.grid(row=1,column=1)
     
      labelApellido_Nombre=Label(groupBox,text="Apellido_Nombre:",width=13,font=("arial",12)).grid(row=2,column=0)
      texBoxApellido_Nombre = Entry(groupBox)
      texBoxApellido_Nombre.grid(row=2,column=1)
         
           
      labelMail=Label(groupBox,text="Mail:",width=13,font=("arial",12)).grid(row=3,column=0)
      texBoxMail = Entry(groupBox)
      texBoxMail.grid(row=3,column=1)
            
      labelTelefono=Label(groupBox,text="Telefono:",width=13,font=("arial",12)).grid(row=4,column=0)
      texBoxTelefono = Entry(groupBox)
      texBoxTelefono.grid(row=4,column=1)
            
      labelDireccion=Label(groupBox,text="Direccion:",width=13,font=("arial",12)).grid(row=5,column=0)
      texBoxDireccion = Entry(groupBox)
      texBoxDireccion.grid(row=5,column=1)
            
                  
        
      Button(groupBox, text="Guardar",width=10,command=guardarRegistros).grid(row=7,column=0)
      Button(groupBox, text="Modificar",width=10).grid(row=7,column=1)
      Button(groupBox, text="Eliminar",width=10).grid(row=7,column=2)
            
      groupBox = LabelFrame(base,text="Lista de Clientes", padx=8,pady=8,)
      groupBox.grid(row=0,column=1,padx=8,pady=8)
            
            #Crear un treview
            
            #Configuracion de columnas
            
      tree = ttk.Treeview(groupBox,columns=("IdCliente","DNI","Apellido_Nombre","Mail","Telefono","Direccion"),show='headings',height=5,)
      tree.column("# 1",anchor=CENTER)
      tree.heading("# 1",text="IDCliente")
       
      tree.column("# 3",anchor=CENTER)
      tree.heading("# 3",text="DNI")
      
      tree.column("# 2",anchor=CENTER)
      tree.heading("# 2",text="Apellido_Nombre")
            
      tree.column("# 4",anchor=CENTER)
      tree.heading("# 4",text="Mail")
            
      tree.column("# 5",anchor=CENTER)
      tree.heading("# 5",text="Telefono")
            
      tree.column("# 6",anchor=CENTER)
      tree.heading("# 6",text="Direccion")
            
                 
      tree.pack()
            
      
           
      base.mainloop()
             
 except ValueError as error:
      print("Error al mostrar la interfaz, error: {}".format(error))
            
def guardarRegistros():
      global texBoxDNI,texBoxApellido_Nombre,texBoxMail,texBoxTelefono,texBoxDireccion,groupBox
       
       
      try:
             #verificar si los widgets estan inicializados
             
            if texBoxDNI is None or texBoxApellido_Nombre is None or texBoxMail is None or texBoxTelefono is None or texBoxDireccion is None:
                  print("Los widgets no estan inicicializados")
                  return
             
            DNI = texBoxDNI.get()
            Apellido_Nombre = texBoxApellido_Nombre.get()
            Mail = texBoxMail.get()
            Telefono = texBoxTelefono.get()
            Direccion = texBoxDireccion.get()
                         
            Market.ingresarClientes(DNI,Apellido_Nombre,Mail,Telefono,Direccion)
            messagebox.showinfo("Información", "Los datos fueron guardados")
             
             
            texBoxDNI.delete(0,END)
            texBoxApellido_Nombre.delete(0,END)
            texBoxMail.delete(0,END)
            texBoxTelefono.delete(0,END)
            texBoxDireccion.delete(0,END)
                         
      except ValueError as error:
             print("Error al ingresar los datos: {}".format(error))
             
Formulario()