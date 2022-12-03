class Base:
    nombre=''
    numero=0
    tiempo=0.0
    base_comp=None
    def __init__(self,name,numero,tiempo):
        self.nombre=name
        self.numero=numero
        self.tiempo=tiempo
        
class ud_admin:
    def __init__(self,nombre,unidades):
        self.nombre=nombre
        self.unidades=unidades
        self.tiempo=float((sum(e.tiempo for e in unidades))/len(unidades))
        self.numero=sum(e.numero for e in unidades)

class jerarquia:

    def __init__(self,uds,uds_admin):
        self.dic={}
        for i in range(len(uds)):
            self.dic[uds[i].nombre]=uds[i]
        for i in range(len(uds_admin)):
            self.dic[uds_admin[i].nombre]=uds_admin[i]

