from Tipo_persona import tipo_persona
from conexion import Conexion
from beautifultable import beautifultable

class tipo_personaDAO:
    def __init__(self) -> None:
        pass
    def eliminarTipo_Persona(self, ID_persona):
        if self.buscarTipo_persona(ID_persona) != None:
            Conexion.cursor.execute("delete from TIPO_PERSONA where ID_persona=:1", [ID_persona])
            Conexion.connection.commit()
            return "Se ha eliminado correctamente"
        else:
            return "No se ha podido crear"

    def buscarTipo_persona(self, ID_persona)->tipo_persona:
        Conexion.cursor.execute("select * from TIPO_PERSONA where ID_persona =:1", [ID_persona])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return tipo_persona (row[0], row[1])
        
    
    def obtenerTipo_persona(self)->None:
        tabla=beautifultable()
        tabla.columns.header=["ID_persona", "Nombre"]
        for row in Conexion.cursor.execute("Select*from tipo_persona order by 1"):
            tabla.rows.append(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("Tipo persona no ingresado")


