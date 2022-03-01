from User import User

alex=User("Alex")
mary=User("Mary")

alex.haceer_deposito(1500)
alex.hacer_retiro(1400)

alex.mostrar_balance_usuario()

alex.trannsfer_dinero(mary,50)

print(alex.soles)
print(mary.soles)