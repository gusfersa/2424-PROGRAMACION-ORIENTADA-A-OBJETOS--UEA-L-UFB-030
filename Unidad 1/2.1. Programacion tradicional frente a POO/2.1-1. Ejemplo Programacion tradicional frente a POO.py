# Programación Tradicional
# Ejemplo: Gestión de una cuenta bancaria

# Definición de variables globales
balance = 0
interest_rate = 0.05

# Función para depositar dinero en la cuenta
def deposit(amount):
    global balance
    balance += amount

# Función para retirar dinero de la cuenta
def withdraw(amount):
    global balance
    balance -= amount

# Función para calcular el interés y actualizar el saldo
def calculate_interest():
    global balance, interest_rate
    interest = balance * interest_rate
    balance += interest

# Uso de las funciones en la programación tradicional
deposit(1000)
withdraw(500)
calculate_interest()

# Imprimir el saldo final
print("Balance (Traditional):", balance)


# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de una cuenta bancaria

class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0.05):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

# Crear una instancia de la clase BankAccount
account = BankAccount()

# Uso de los métodos en la programación orientada a objetos
account.deposit(1000)
account.withdraw(500)
account.calculate_interest()

# Imprimir el saldo final
print("Balance (OOP):", account.balance)
