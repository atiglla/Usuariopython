from User import User

alex=User("Alex")
mary=User("Mary")
jose=User("Jose")

alex.hacer_deposito(1500)
alex.hacer_deposito(1500)
alex.hacer_deposito(1500)
alex.hacer_retiro(1400)
alex.mostrar_balance_usuario()

mary.hacer_deposito(1000)
mary.hacer_deposito(1000)
mary.hacer_retiro(200)
mary.hacer_retiro(200)
mary.mostrar_balance_usuario()

jose.hacer_deposito(2000)
jose.hacer_retiro(100)
jose.hacer_retiro(100)
jose.hacer_retiro(100)
jose.mostrar_balance_usuario()

alex.trannsfer_dinero(jose,50)
alex.mostrar_balance_usuario()
jose.mostrar_balance_usuario()

