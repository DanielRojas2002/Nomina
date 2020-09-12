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

    def Sacanominas(self):
        
        print("Este es tu nombre: ",self.__nombre)
        print("Este es tu depatamento: ",self.__departamento)
        
        if self.__primadominical==1:
            domingo=self.__cuotadiaria*.25
            print("Esto es lo que te pagaran si trabajas el Domingo: ",domingo)
        
        elif self.__primadominical==2:
            domingo=self.__cuotadiaria-self.__cuotadiaria
            
            
        if self.__diaslaborados==1:
            suma=(self.__cuotadiaria/6)*self.__diaslaborados
            print("Este es lo que te pagaremos en el septimo dia: " ,suma)
            
        elif self.__diaslaborados==2:
            suma=(self.__cuotadiaria/6)*self.__diaslaborados
            print("Este es lo que te pagaremos en el septimo dia: ",suma)
        
        elif self.__diaslaborados==3:
            suma=(self.__cuotadiaria/6)*self.__diaslaborados
            print("Este es lo que te pagaremos en el septimo dia: ",suma)
        
        elif self.__diaslaborados==4:
            suma=(self.__cuotadiaria/6)*self.__diaslaborados
            print("Este es lo que te pagaremos en el septimo dia: ",suma)
        
        elif self.__diaslaborados==5:
            suma=(self.__cuotadiaria/6)*self.__diaslaborados
            print("Este es lo que te pagaremos en el septimo dia: ",suma)
            
        elif diaslaborados==6:
            suma=(self.__cuotadiaria/6)*self.__diaslaborados
            print("Este es lo que te pagaremos en el septimo dia: ",suma)
            
        costoporhora=(self.__cuotadiaria/8)
        print("Esto es lo que ganas por hora: ",costoporhora)
        sueldoordinario=self.__cuotadiaria*self.__diaslaborados+domingo+suma
        print("Este es tu sueldo ordinario: ",sueldoordinario)
        
        if self.__horastotalesextras<=0:
            x1=0
            suma1=0
            print("Ordinario : 0 ")
            print("Doble : 0")
            print("Triple : 0")
            totalpercepcion=sueldoordinario
            print("Esto es tu sueldo total: ",totalpercepcion)
        
        elif self.__horastotalesextras>=1:
            xd=(self.__horastotalesextras*costoporhora)
            zd=(self.__horastotalesextras*costoporhora)
            print(f"Ordinario : {xd} ")
            print(f"Doble : {zd} ")
            triple=(self.__horastotalesextras-9)
            
            if triple <=0:
                resta=0
                sumax=(xd+zd+resta)
                print(f"Triple :{resta}")
                print("Esto es lo que te pagaran si trabaste horas dobles o triples: ",sumax)
                totalpercepcion=sueldoordinario+sumax
                print("Esto es tu sueldo total: ",totalpercepcion)
            
            elif triple>0:
                suma2=(triple*costoporhora)
                suma1=(xd+zd+suma2)
                print(f"Triple :{suma2}")
                print("Esto es lo que te pagaran si trabaste horas dobles o triples: ",suma1)
                totalpercepcion=sueldoordinario+suma1
                print("Esto es tu sueldo total: ",totalpercepcion)


opcion=1             
while opcion==1:
    nombre=(input("Cual es tu Nombre: "))
    departamento=(input("Cual es tu Departamento: "))
    cuotadiaria=int(input("Dime tu cuota diaria: "))
    horastotalesextras=int(input("Dime cuantas horas extras haz trabajado : "))
    diaslaborados=int(input("Dime cuantos dias haz laborado : "))
    primadominical=int(input("Trabajasate el Domingo  SI=1  NO=2: "))
    print("-"*100)
    x=Nomina(nombre,departamento,cuotadiaria,horastotalesextras,diaslaborados,primadominical)
    x.Sacanominas()
    print("Esta es tu Nacionalidad: ",x.nacionalidad)
    print("Numero de persona registrada : ",x.numeroDePersonas)
    print("-"*40)
    opcion=int(input("Deseas seguir registrando empleados 1=SI 2 =NO : "))