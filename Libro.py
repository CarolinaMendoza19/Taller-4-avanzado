class libro:
    def __init__(self, id_codigo, Titulo, Autor, Fecha_entrega, Fecha_prestamo ) -> None:
        self.__ID_codigo=id_codigo
        self.__Titulo=Titulo
        self.__Autor=Autor
        self.__Fecha_entrega=Fecha_entrega
        self.__Fecha_prestamo=Fecha_prestamo

    @property
    def id_codigo(self):
        return self.__ID_codigo

    @property
    def Titulo(self):
        return self.__Titulo
    
    @property
    def Autor(self):
        return self.__Autor
    
    @property
    def Fecha_entrega(self):
        return self.__Fecha_entrega
    
    @property
    def Fecha_prestamo(self):
        return self.__Fecha_prestamo
    

    

    