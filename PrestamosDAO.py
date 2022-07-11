from Prestamos import prestamos
from conexion import Conexion
from beautifultable import beautifultable

class prestamosDAO:
    def __init__(self) -> None:
        pass
    def eliminarPrestamos(self, id_rut):
        
        Conexion.cursor.execute("delete from PRESTAMOS where id_rut=:1", [id_rut])
        Conexion.connection.commit()
        return "Se ha eliminado correctamente"
        

    def buscarPrestamos(self, id_rut)->prestamos:
        Conexion.cursor.execute("select * from PRESTAMOS where rut =:1", [id_rut])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return prestamos (row[0], row[1])
    
    def insertarPrestamos(self, Prestamos):
        
        Conexion.cursor.execute("""
        insert into prestamos (id_rut, id_codigo) values(:Prut,:pnom)""",[Prestamos.id_rut, Prestamos.Codigo])
        Conexion.connection.commit()
        return "Los datos fueron ingresados de forma correcta"
        
        
    def obtenerPrestamos(self)->None:
        tabla=beautifultable()
        tabla.columns.header=["Rut", "Codigo"]
        for row in Conexion.cursor.execute("Select*from PRESTAMOS order by 1"):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("Prestamo no ingresado")