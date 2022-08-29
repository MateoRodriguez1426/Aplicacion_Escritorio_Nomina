from tkinter import ttk
from tkinter import *
import sqlite3

class product:                          #Clase Nomina
    def __init__(self, window):         #Constructor que hace que cada vez que se inicia la clase, ejecute una instancia que le de nombre a la ventana de la aplicacion  
        self.wind = window
        self.wind.title('Products Aplication')
        
        #Aqui se va a crear el frame es decir el lugar donde se van a  poder acomodar lo elemetos
        frame = LabelFrame(self.wind, text = 'Register a new Product')
        frame.grid(row = 0, column = 0, columnspan= 3, pady=20)
        
        #Entrada de datos/input  = Nombre
        
        
        Label(frame, text = 'Name: ').grid(row =1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column = 1)
        
        #Apellidos
        
        Label(frame, text = 'Last Name: ').grid(row =2, column = 0)
        self.lname = Entry(frame)
        self.lname.grid(row=2, column = 1)
        
        #Documento de Identidad
        Label(frame, text = 'Id Document: ').grid(row =3, column = 0)
        self.document = Entry(frame)
        self.document.grid(row=3, column = 1)
        
        
        #Salario
        Label(frame, text = 'Basic Wage: ').grid(row =4, column = 0)
        self.wage = Entry(frame)
        self.wage.grid(row=4, column = 1)
        
        #Dias Trabajados
        Label(frame, text = 'Worked Days: ').grid(row =5, column = 0)
        self.workdays = Entry(frame)
        self.workdays.grid(row=5, column = 1)
        
      
        #Entrada de Productos
        ttk.Button(frame, text= ' SaveProduct ').grid(row = 6, columnspan= 2, sticky =W + E)
        

        #Tabla
        self.tree = ttk.Treeview(height = 20, columns= 6)
        self.tree.grid(row = 7, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor= CENTER)
        self.tree.heading('#1', text = 'Last Name', anchor= CENTER)
        
        '''
        self.tree.heading('#2', text = 'Id Document', anchor= CENTER)
        self.tree.heading('#3', text = 'Wage', anchor= CENTER)
        self.tree.heading('#4', text = 'Worked Days', anchor= CENTER)
        '''
        
if __name__ == '__main__':
    window = Tk()
    application = product (window)
    window.mainloop() 
