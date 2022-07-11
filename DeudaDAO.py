from Deuda import deuda
from conexion import Conexion
from beautifultable import beautifultable

class deudaDAO:
    def __init__(self) -> None:
        pass
    
    def eliminarDeuda(self, ID_deuda):       
        Conexion.cursor.execute("delete from DEUDA where ID_deuda=:1", [ID_deuda])
        Conexion.connection.commit()
        return "Deuda eliminada correctamente"
        
    def buscarDeuda(self, ID_deuda):
        Conexion.cursor.execute("select * from DEUDA where ID_deuda =:1", [ID_deuda])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return deuda (row[0], row[1], row[2], row[3], row[4])
    
    def insertarDeuda(self, Deuda):      
        Conexion.cursor.execute("""insert into deuda(ID_deuda, titulo_libro, dias_retraso, monto_deuda) values(:Prut,:pnom,:pap,:pci)""",[Deuda.ID_deuda, Deuda.Titulo_libro, Deuda.Dias_retraso, Deuda.Monto_deuda])
        Conexion.connection.commit()
        return "Los datos fueron ingresados de forma correcta"
      
            
    def obtenerDeuda(self)->None:
        tabla=beautifultable()
        tabla.columns.header=["ID_Deuda", "Titulo_libro", "Dias_retraso", "Monto_deuda", "ID_prestamo"]
        for row in Conexion.cursor.execute("Select*from deuda order by 1"):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("Deuda no ingresada")