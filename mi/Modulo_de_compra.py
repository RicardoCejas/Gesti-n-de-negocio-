from typing import List, Dict
from datetime import datetime
from stock import Stock
from pagar import realizar_pago

class Compra:
    def __init__(self, id: int, productos: List[Dict[str, int]], total: float, fecha: datetime):
        self.id = id
        self.productos = productos  # Lista de diccionarios {producto_id: cantidad}
        self.total = total
        self.fecha = fecha

class SistemaCompras:
    def __init__(self, stock: Stock):
        self.stock = stock
        self.compras: List[Compra] = []

    def realizar_compra(self, productos_cantidades: List[Dict[str, int]]) -> bool:
        total = 0
        for item in productos_cantidades:
            producto_id = item['producto_id']
            cantidad = item['cantidad']
            if not self.stock.verificar_stock(producto_id, cantidad):
                print(f"Stock insuficiente para el producto {producto_id}")
                return False
            total += self.stock.productos[producto_id].precio * cantidad

        if realizar_pago(total):
            compra_id = len(self.compras) + 1
            nueva_compra = Compra(compra_id, productos_cantidades, total, datetime.now())
            self.compras.append(nueva_compra)
            
            for item in productos_cantidades:
                self.stock.actualizar_stock(item['producto_id'], -item['cantidad'])
            
            print(f"Compra realizada con éxito. ID de compra: {compra_id}")
            return True
        else:
            print("Compra cancelada")
            return False

    def mostrar_historial_compras(self):
        if not self.compras:
            print("No hay historial de compras.")
        else:
            print("Historial de compras:")
            for compra in self.compras:
                print(f"ID de compra: {compra.id}, Fecha: {compra.fecha}, Total: ${compra.total}")
                for item in compra.productos:
                    producto = self.stock.productos[item['producto_id']]
                    print(f"  - {producto.nombre}: {item['cantidad']} unidades")