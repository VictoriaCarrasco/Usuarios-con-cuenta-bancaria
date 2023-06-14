class CuentaBancaria:
    def __init__ (self, tasa_interes,balance):
        self.tasa_interes = tasa_interes
        self.balance = balance


    def hacer_deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance >= amount:
                self.balance -= amount 
        else: 
            print ("Fondos Insuficientes: Cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print ("Este es tu estado de cuenta. Balance: $", self.balance)
        return self 
        
    def mostrar_interes (self):
        print ("Este es tu interes:", self.balance)
        return self 

    def generar_interes (self):
        if self.balance > 0: 
            interes= self.balance * self.tasa_interes
            self.balance += interes
        self.mostrar_interes()
        return self 


print ("___________________________________________")


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuentas = []
        
    def crear_cuenta(self, tasa_interes, balance):
        cuenta = CuentaBancaria(tasa_interes, balance)
        self.cuentas.append(cuenta)
        return cuenta  

    def hacer_deposito(self, cuenta, amount):
        cuenta.hacer_deposito(amount)
        return self 

    def hacer_giro(self, cuenta, amount):
        cuenta.retiro(amount)
        return self 

    def transferir_dinero(self, cuenta_origen, other_user, amount):
        cuenta_origen.retiro(amount)
        other_user.hacer_deposito(amount)
        return self

    def mostrar_balance_usuario (self, cuenta):
        print(self.nombre,"$", cuenta.balance)
        return self


Usuario1=Usuario("Guido van Rossum", "guido@python.com")     
cuenta1 = Usuario1.crear_cuenta (tasa_interes=0.02, balance=0)
cuenta2=  Usuario1.crear_cuenta (tasa_interes=0.02, balance=0)

Usuario1.hacer_deposito(cuenta2, 100)
Usuario1.hacer_deposito(cuenta1, 200)
Usuario1.hacer_deposito(cuenta2, 150)
Usuario1.hacer_giro(cuenta1, 50)
Usuario1.mostrar_balance_usuario(cuenta1)
Usuario1.mostrar_balance_usuario(cuenta2)


