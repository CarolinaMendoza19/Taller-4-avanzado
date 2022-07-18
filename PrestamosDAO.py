from Prestamos import prestamos
from conexion import Conexion
from beautifultable import BeautifulTable

class prestamosDAO:
    def __init__(self) -> None:
        pass
    def eliminarPrestamos(self, ID_prestamo):
        
        Conexion.cursor.execute("delete from PRESTAMOS where id_prestamo=:1", [ID_prestamo])
        Conexion.connection.commit()
        return "Se ha eliminado correctamente"
        

    def buscarPrestamos(self, ID_Rut)->prestamos:
        tabla=BeautifulTable()
        tabla.columns.header=["Id Prestamo","Rut", "Nombre", "id libro", "titulo libro"]
        for row in Conexion.cursor.execute("SELECT ID_PRESTAMO, p.ID_RUT, pe.Nombre, ID_LIBRO, li.titulo FROM PRESTAMOS p FULL OUTER JOIN LIBRO Li on Li.Id_codigo = p.ID_LIBRO FULL OUTER JOIN PERSONA pe on pe.ID_RUT = p.ID_RUT where p.id_rut = :1", [ID_Rut]):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("No existen prestamos asociados con este rut")
    
    def insertarPrestamos(self, Prestamos):
        Conexion.cursor.execute("""
        insert into prestamos (id_prestamo, id_rut, id_Libro) values(:idp,:Prut,:plib)""",[Prestamos.ID_Prestamo, Prestamos.ID_Rut, Prestamos.ID_Libro])
        Conexion.connection.commit()
        return "Los datos fueron ingresados de forma correcta"
        
        
    def obtenerPrestamos(self):
        tabla=BeautifulTable()
        tabla.columns.header=["Id Prestamo","Rut", "Nombre", "Id Libro", "Titulo Libro"]
        for row in Conexion.cursor.execute("SELECT ID_PRESTAMO, p.ID_RUT, pe.Nombre, ID_LIBRO, li.titulo FROM PRESTAMOS p FULL OUTER JOIN LIBRO Li on Li.Id_codigo = p.ID_LIBRO FULL OUTER JOIN PERSONA pe on pe.ID_RUT = p.ID_RUT where p.id_rut = pe.id_rut order by 1"):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("Prestamo no ingresado")