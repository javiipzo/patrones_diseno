from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List



class Bateria:
    conectado=False
    cargando=False
    carga=0
    tiempo=0

    def __init__(self):
        self.conectado=False
        self.cargando=False
        self.carga=100
        self.tiempo=0
       
    def __notifica():
        return
    def getCarga(self):
        return self.carga
    def getTiempo(self):
        return self.tiempo

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass

class Concrete_Bateria(Bateria):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Bat: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Bat: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def do_smt(self):
        self.carga-=1
        self.tiempo+=1
        print("Estoy utilizando el dispositivo...")
        self.notify()

    def cargar(self):
        self.conectado=True
        self.cargando=True
        self.carga=self.carga+1
        print("El dispositivo se ha puesto a cargar...")
        self.notify()

    def desconectar(self):
        self.conectado=False
        self.cargando=False
        print("El dispositivo ha dejado de cargar...")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Bateria) -> None:
        """
        Receive update from subject.
        """
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Bateria) -> None:
        if subject.tiempo == 30 or subject.tiempo == 60:
            print("AVISO: Tiempo estimado de carga necesario de %s minutos" % subject.tiempo)
        else:
            print("Tiempo estimado de carga necesario de %s min" % subject.tiempo)


class ConcreteObserverB(Observer):
    def update(self, subject: Bateria) -> None:
        if subject.carga == 20 or subject.carga == 50 or subject.carga == 10:
            print("AVISO: Nivel de batería al %s por ciento" % subject.carga)
        else:
            print("Nivel de batería al %s" % subject.carga)

def menu():
    subject = Concrete_Bateria()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    while True:
        print()
        print("1. Comprobar el estado de la batería")
        print("2. Poner a cargar el telefono")
        print("3. Quitar de cargar el telefono")
        print("4. Usar el telefono")
        print("5. Salir")
        print()
        opcion=int(input("Introduce que quieres hacer: "))
        print()
        if opcion == 1:
            subject.notify()
        elif opcion == 2:
            if subject.cargando:
                print("El telefono ya esta cargando...")
            else:
                num=int(input("Cuanto tiempo quiere cargar el dispositivo: "))
                if subject.carga>=100:
                    print("El telefono ya esta al maximo")
                    subject.carga-=1
                    subject.cargar()
                    
                else:
                    for i in range(num):
                        subject.cargar()
                        if subject.carga==100:
                            print("Nivel de batería al máximo.")
                            break
        elif opcion == 3:
            if not subject.cargando:
                print("El telefono no estaba cargando...")
            else:
                subject.desconectar()
        elif opcion == 4:
            num=int(input("Cuanto tiempo quieres usar el telefono"))
            if num>subject.carga:
                opc=input("El movil se acabara quedando sin bateria. Estas seguro? s/n ")
                while opc!='n' and opc!='s':
                    opc=input("El movil se acabara quedando sin bateria. Estas seguro? s/n ")
                if opc=='s':
                    for i in range(num):
                        if subject.carga<=0:
                            print("Se te ha acabado la bateria, no puedes usar el telefono.")
                        else:
                            subject.do_smt()
            else:
                for i in range(num):
                    subject.do_smt()
        elif opcion==5:
            break
    '''
    subject.do_smt()
    subject.cargar()

    subject.detach(observer_a)

    subject.desconectar()
    '''
