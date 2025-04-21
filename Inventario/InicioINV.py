class Inventario:
    def __init__(self,producto,tamaño,peso,cantidad):
        self.producto = producto
        self.tamaño = tamaño
        self.peso = peso
        self.cantidad = cantidad
    def ListaInventario (self):
        print(f"El usuario a ingresado {self.producto} al inventario")
        print(f"El tamaño del producto ingresado el es: {self.tamaño} ")
        print(f"El peso del producto ingresado es {self.peso} ")
        print(f"El usuario a ingresado la cantidad de  {self.cantidad} unidades de {self.producto} ")
        listainventario = [self.producto,self.tamaño,self.peso,self.cantidad]
        



    


