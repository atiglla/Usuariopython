class User:
    def __init__(self, nombre):
        self.nombre=nombre
        self.soles=0

    def hacer_retiro (self, cantidad):
        self.soles-=cantidad
        return self

    def hacer_deposito (self, cantidad):
        self.soles+=cantidad
        return self

    def mostrar_balance_usuario (self):
        print(f"Usuario:{self.nombre}, Balance:{self.soles}")
        return self

    def trannsfer_dinero(self, otro_usuario, cantidad):
        self.soles-=cantidad
        otro_usuario.soles+=cantidad
        return self
