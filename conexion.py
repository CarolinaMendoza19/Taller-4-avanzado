import cx_Oracle
class Conexion:
    connection = None
    cursor = None

    def __init__(self):
        pass

    @classmethod
    def getConnection(cls):
        cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_6")
        if cls.connection is None:
            conex = cx_Oracle.connect(user="Carolina", password="TallerSistemas2022", dsn="tallerdesarrollosistemasdiurno_high")
            cls.cursor = conex.cursor()
            cls.connection = conex  

    
    
    
    
    
    
    
    
    
    