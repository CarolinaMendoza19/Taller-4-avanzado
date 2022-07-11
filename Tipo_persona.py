class tipo_persona:
    def __init__(self, ID_persona, Nombre) -> None:
        self.__ID_persona=ID_persona
        self.__Nombre=Nombre
       

    @property
    def ID_persona(self):
        return self.__ID_persona
    
    @property
    def Nombre(self):
        return self.__Nombre
