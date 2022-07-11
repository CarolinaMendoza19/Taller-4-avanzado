class deuda:
    def __init__(self, ID_deuda, Titulo_libro, Dias_retraso, Monto_deuda, ID_prestamo ):
        self.__ID_deuda=ID_deuda
        self.__Titulo_libro=Titulo_libro
        self.__Dias_retraso=Dias_retraso
        self.__Monto_deuda=Monto_deuda
        

    @property
    def ID_deuda(self):
        return self.__ID_deuda

    @property
    def Titulo_libro(self):
        return self.__Titulo_libro 
    
    @property
    def Dias_retraso(self):
        return self.__Dias_retraso
    
    @property
    def Monto_deuda(self):
        return self.__Monto_deuda
    
