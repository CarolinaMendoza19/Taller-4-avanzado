class prestamos:
    def __init__(self,ID_Prestamo, ID_Rut, ID_Libro) -> None:
        self.__ID_Prestamo=ID_Prestamo
        self.__ID_Rut=ID_Rut
        self.__ID_Libro=ID_Libro


    @property
    def ID_Prestamo(self):
        return self.__ID_Prestamo

    @property
    def ID_Rut(self):
        return self.__ID_Rut
    
    @property
    def ID_Libro(self):
        return self.__ID_Libro
    
