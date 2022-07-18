from Deuda import deuda
from conexion import Conexion
from beautifultable import BeautifulTable

class deudaDAO:
    def __init__(self) -> None:
        pass
    
    def eliminarDeuda(self, ID_deuda):       
        Conexion.cursor.execute("delete from DEUDA where ID_deuda=:1", [ID_deuda])
        Conexion.connection.commit()
        return "Deuda eliminada correctamente"
        
    def buscarDeuda(self, ID):
        tabla=BeautifulTable()
        tabla.columns.header=["ID_Deuda", "Titulo_libro", "Dias_retraso", "Monto_deuda", "ID_prestamo"]
        for row in Conexion.cursor.execute("Select * from deuda where id_deuda = :1 order by 1",[ID]):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("No existe una deuda con el id proporcionado")
    
    def insertarDeuda(self, Deuda):      
        Conexion.cursor.execute("""insert into deuda(ID_deuda, titulo_libro, dias_retraso, monto_deuda,Id_prestamo) values(:Prut,:pnom,:pap,:pci, :idp)""",[Deuda.ID_deuda, Deuda.Titulo_libro, Deuda.Dias_retraso, Deuda.Monto_deuda, Deuda.ID_prestamo])
        Conexion.connection.commit()
        return "Los datos fueron ingresados de forma correcta"
      
            
    def obtenerDeuda(self):
        tabla=BeautifulTable()
        tabla.columns.header=["ID_Deuda", "Titulo_libro", "Dias_retraso", "Monto_deuda", "ID_prestamo"]
        for row in Conexion.cursor.execute("Select * from deuda order by 1"):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("Deuda no ingresada")