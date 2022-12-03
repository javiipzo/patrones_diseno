from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List



class Bateria:
    conectado=False
    cargando=False
    carga=0
    tiempo=0
    notifica=''
    def __init__(self):
        self.conectado=False
        self.cargando=False
        self.carga=100
        self.tiempo=0
        self.notifica=''
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
        self.carga-=2
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


if __name__ == "__main__":
    # The client code.

    subject = Concrete_Bateria()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.do_smt()
    subject.cargar()

    subject.detach(observer_a)

    subject.desconectar()