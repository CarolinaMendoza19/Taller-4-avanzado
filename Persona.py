class persona:
    def __init__(self, id_rut, Nombre, Apellido, Ciudad, Direccion,Telefono, ID_TipoPersona):
        self.__ID_rut=id_rut
        self.__Nombre=Nombre
        self.__Apellido=Apellido
        self.__Ciudad=Ciudad
        self.__Direccion=Direccion
        self.__Telefono=Telefono
        self.__ID_TipoPersona=ID_TipoPersona


    @property
    def id_rut(self):
        return self.__ID_rut
    
    @property
    def Nombre(self):
        return self.__Nombre
    
    @property
    def Apellido(self):
        return self.__Apellido
    
    @property
    def Ciudad(self):
        return self.__Ciudad
    
    @property
    def Direccion(self):
        return self.__Direccion

    @property
    def Telefono(self):
        return self.__Telefono
    @property
    def ID_TipoPersona(self):
        return self.__ID_TipoPersona
    
    
    

    
