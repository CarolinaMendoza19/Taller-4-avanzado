class prestamos:
    def __init__(self, id_rut, Codigo ) -> None:
        self.__ID_rut=id_rut
        self.__Codigo=Codigo
        


    @property
    def id_rut(self):
        return self.__ID_rut
    
    @property
    def Codigo(self):
        return self.__Codigo
    
