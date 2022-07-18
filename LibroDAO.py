from Libro import libro
from conexion import Conexion
from beautifultable import BeautifulTable

class libroDAO:
    def __init__(self) -> None:
        pass

    def eliminarLibro(self, id_codigo):
        Conexion.cursor.execute("delete from LIBRO where id_codigo=:1", [id_codigo])
        Conexion.connection.commit()
        return "Se ha eliminado correctamente"


    def buscarLibro(self, id_codigo)->libro:
        Conexion.cursor.execute("select * from LIBRO where codigo=:1", [id_codigo])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return libro (row[0], row[1], row[2], row[3], row[4])
    
    def insertarLibro(self, Libro):
        
        Conexion.cursor.execute("""
        insert into libro(id_codigo, titulo,autor, fecha_entrega, fecha_prestamo) values(:Prut,:pnom,:pap,:pci,:pdi)  """,[Libro.id_codigo, Libro.Titulo, Libro.Autor, Libro.Fecha_entrega, Libro.Fecha_prestamo])
        Conexion.connection.commit()
        return "Los datos fueron ingresados de forma correcta"
        
        
    def obtenerLibro(self)->None:
        tabla=BeautifulTable()
        tabla.columns.header=["Id Libro", "Titulo", "Autor", "Fecha entrega", "Fecha prestamo"]
        for row in Conexion.cursor.execute("Select id_codigo, titulo, autor,TO_CHAR( fecha_entrega, 'YYYY-MM-DD' ),TO_CHAR( fecha_prestamo, 'YYYY-MM-DD' ) from libro order by 1"):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("Libro no ingresado")