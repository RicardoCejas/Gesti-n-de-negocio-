from abc import ABC, abstractmethod

class MetodoDePago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass
