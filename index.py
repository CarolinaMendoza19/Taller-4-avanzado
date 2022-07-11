from conexion import Conexion
from beautifultable import BeautifulTable
import os
import time
from Deuda import deuda
from DeudaDAO import deudaDAO
from Libro import libro
from LibroDAO import libroDAO
from Persona import persona
from PersonaDAO import personaDAO
from Prestamos import prestamos
from PrestamosDAO import prestamosDAO
from Tipo_persona import tipo_persona
from Tipo_personaDAO import tipo_personaDAO

from BaseDato import BaseDato

def validarTipoPersona(mensaje):
    while True:        
        try:
            dato = int(input(mensaje))
            if dato in range(1,3):
                break
            else:
                raise Exception
        except:
            print("solo se permite 1 y 2")
    return dato


os.system('cls')
print ("Iniciando la conexion ...")
Conexion.getConnection()
os.system('cls')


menu = BeautifulTable()
menu.columns.header = ['=== Sistema de prestamos de libro ==='] 
menu.rows.append(['1. Crear tabla '])
menu.rows.append(['2. Eliminar tabla'])
menu.rows.append(['3. Insertar deuda'])
menu.rows.append(['4. Eliminar deuda'])
menu.rows.append(['5. Obtener deuda'])
menu.rows.append(['6. Insertar libro'])
menu.rows.append(['7. Eliminar libro'])
menu.rows.append(['8. Obtener libro'])
menu.rows.append(['9. Insertar persona'])
menu.rows.append(['10. Eliminar persona'])
menu.rows.append(['11. Obtener persona'])
menu.rows.append(['12. Insertar prestamo'])
menu.rows.append(['13. Eliminar prestamo'])
menu.rows.append(['14. Obtener prestamo'])


def crearT():
    os.system('cls')
    bd = BaseDato()
    print('____CREAR TABLAS_____')
    print()
    print(bd.crearTablas())
    print()
    time.sleep(3)

def eliminarT():
    os.system('cls')
    bd = BaseDato()
    print('____ELIMINAR TABLAS_____')
    print()
    print(bd.eliminarTablas())
    print()
    time.sleep(3)

#Deuda
def insertarDeuda():
    os.system('cls')
    deuda1 = deudaDAO()
    print('Nueva deuda')
    print()
    ID_deuda = input('indique el ID_deuda : ')
    Titulo_libro = input('indique el Titulo del libro : ')
    Dias_retraso = input('indique los dias de retraso : ')
    Monto_deuda = input('indique el monto de la deuda : ')
    ID_prestamo = input('indique el prestamo : ')
    print(deuda1.insertarDeuda(deuda(ID_deuda,Titulo_libro,Dias_retraso,Monto_deuda,ID_prestamo)))

def eliminarDeuda():
    os.system('cls')
    deuda2 = deudaDAO()
    print('Eliminar deuda')
    print()
    ID_deuda= input('Indique el id de la deuda a eliminar: ')
    print(deuda2.eliminarDeuda((ID_deuda)))

def obtenerDeuda():
    os.system('cls')
    deuda3 = deudaDAO()
    print('Obtener deuda')
    print()
    ID_deuda= input('Indique el id de la deuda a buscar: ')
    print(deuda3.obtenerDeuda((ID_deuda)))

    

#libro
def insertarLibro():
    os.system('cls')
    libro1 = libroDAO()
    print('Nuevo libro')
    print()
    id_codigo = input('indique el codigo del libro : ')
    Titulo = input('indique el titulo del libro : ')
    Autor = input('indique el autor del libro : ')
    Fecha_entrega = input('indique la fecha de entrega del libro : ')
    Fecha_prestamo = input('indique la fecha de prestamo del libro : ')
    print(libro1.insertarLibro(libro(id_codigo,Titulo,Autor,Fecha_entrega,Fecha_prestamo)))

def eliminarLibro():
    os.system('cls')
    libro2 = libroDAO()
    print('Eliminar libro')
    print()
    id_codigo= input('Indique el id del libro a eliminar: ')
    print(libro2.eliminarLibro((id_codigo)))

#persona
def insertarPersona():
    os.system('cls')
    persona1 = personaDAO()
    print('Nueva persona')
    print()
    rut = input('indique el rut de la persona: ')
    nombre = input('indique el nombre de la persona: ')
    apellido = input('indique el apellido de la persona: ')
    ciudad = input('indique la ciudad de la persona: ')
    direccion = input('indique la direccion de la persona: ')
    telefono = int(input('indique el telefono de la persona: '))
    ID_Tipo_Persona = input('indique el tipo persona: ')
    print(persona1.insertarPersona(persona(rut,nombre,apellido,ciudad,direccion,telefono,ID_Tipo_Persona)))


def eliminarPersona():
    os.system('cls')
    persona2 = personaDAO()
    print('Eliminar persona')
    print()
    id_rut= input('Indique el rut de la persona a eliminar: ')
    print(persona2.eliminarPersona((id_rut)))

#Prestamo
def insertarPrestamo():
    os.system('cls')
    prestamos1 = prestamosDAO()
    print('Nuevo prestamo')
    print()
    rut = input('indique el rut de la persona: ')
    codigo = input('indique el codigo: ')
    print(prestamos1.insertarPrestamos(prestamos(rut,codigo)))

def eliminarPrestamo():
    os.system('cls')
    prestamos2 = prestamosDAO()
    print('Eliminar prestamo')
    print()
    id_rut= input('Indique el rut de la persona a eliminar: ')
    print(prestamos2.eliminarPrestamos((id_rut)))

#Tipo_persona
def insertarTipo_persona():
    os.system('cls')
    tipo_persona1 = tipo_personaDAO()
    print('Nuevo tipo persona')
    print()
    ID_persona = input('indique el ID_persona (1 es alumno y 2 docente) : ')
    Nombre = input('indique el nombre  de la persona: ')
    print(tipo_persona1.insertarTipo_persona(tipo_persona(ID_persona,Nombre)))
        


while True:
    os.system('cls')
    print(menu)
    opcion = input('Opcion: ')
    if opcion == '1':
        crearT()
    elif opcion == '2':
        eliminarT()
    elif opcion == '3':
        insertarDeuda()
    elif opcion =='4':
        eliminarDeuda()
    elif opcion =='5':
        obtenerDeuda()
    elif opcion == '6':
        insertarLibro()
    elif opcion == '7':
        eliminarLibro()
    elif opcion == '8':
        obtenerLibro()
    elif opcion == '9':
        insertarPersona()
    elif opcion == '10':
        eliminarPersona()
    elif opcion == '11':
        obtenerPersona()
    elif opcion == '12':
        insertarPrestamo()
    elif opcion == '13':
        eliminarPrestamo()
    elif opcion == '14':
        obtenerPrestamo()




