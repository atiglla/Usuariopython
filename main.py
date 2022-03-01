from User import User

alex=User("Alex")
mary=User("Mary")
jose=User("Jose")

alex.hacer_deposito(1500).hacer_deposito(1500).hacer_deposito(1500).hacer_retiro(1400).mostrar_balance_usuario()

mary.hacer_deposito(1000).hacer_deposito(1000).hacer_retiro(200).hacer_retiro(200).mostrar_balance_usuario()

jose.hacer_deposito(2000).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).mostrar_balance_usuario()

alex.trannsfer_dinero(jose,50).mostrar_balance_usuario()

jose.mostrar_balance_usuario()

