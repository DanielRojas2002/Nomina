class Nomina:
    numeroDePersonas=0
    nacionalidad="Mexicana"
    

    def __init__(self,nombre,departamento,cuotadiaria,horastotalesextras,diaslaborados,primadominical):
        self.__nombre=nombre
        self.__departamento=departamento
        self.__cuotadiaria=cuotadiaria
        self.__horastotalesextras=horastotalesextras
        self.__diaslaborados=diaslaborados
        self.__primadominical=primadominical
        Nomina.numeroDePersonas+=1