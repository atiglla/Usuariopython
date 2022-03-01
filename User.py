class User:
    def __init__(self, nombre):
        self.nombre=nombre
        self.soles=0

    def hacer_retiro (self, cantidad):
        self.soles-=cantidad

    def haceer_deposito (self, cantidad):
        self.soles+=cantidad

    def mostrar_balance_usuario (self):
        print(f"Usuario:{self.nombre}, Balance:{self.soles}")

    def trannsfer_dinero(self, otro_usuario, cantidad):
        self.soles-cantidad
        otro_usuario.soles+=cantidad
