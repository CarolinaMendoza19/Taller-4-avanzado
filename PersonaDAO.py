from Persona import persona
from conexion import Conexion
from beautifultable import beautifultable

class personaDAO:
    def __init__(self) -> None:
        pass
    def eliminarPersona(self, id_rut):
       
        Conexion.cursor.execute("delete from PERSONA where id_rut=:Prut", [id_rut])
        Conexion.connection.commit()
        return "Se ha eliminado correctamente"


    def buscarPersona(self, rut)->persona:
        Conexion.cursor.execute("select * from PERSONA where rut=:1", [rut])
        row=Conexion.cursor.fetchone()
        if row is None:
            return  None
        else:
            return persona (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    
    def insertarPersona(self, Persona):

        Conexion.cursor.execute("""insert into persona(id_rut, nombre, apellido, ciudad, direccion, telefono, id_tipo) values(:Prut,:pnom,:pap,:pci,:pdi,:pte,:idt)""",[Persona.id_rut, Persona.Nombre, Persona.Apellido, Persona.Ciudad, Persona.Direccion, Persona.Telefono, Persona.ID_TipoPersona])
        Conexion.connection.commit()
        return "Los datos fueron ingresados de forma correcta"

        
    def obtenerPersona(self)->None:
        tabla=beautifultable()
        tabla.columns.header=["Rut", "Nombre", "Apellido", "Ciudad", "Direccion", "Telefono", "ID_TipoPersona"]
        for row in Conexion.cursor.execute('SELECT ID_RUT, p.NOMBRE, APELLIDO, CIUDAD, DIRECCION, TELEFONO, t.NOMBRE as "tipo de persona" FROM PERSONA P FULL OUTER JOIN TIPO_PERSONA T ON T.ID_PERSONA = P.ID_TIPO ORDER BY P.NOMBRE'):
            tabla.rows.appedn(row)
        if len(tabla.rows)>0:
            print(tabla)
        else:
            print("Persona no ingresada")

