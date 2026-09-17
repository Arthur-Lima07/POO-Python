class ContaBancaria:
    def __init__(self, titular : str, saldo_inicial = 0.0):
        if isinstance(titular, str):
            self.titular = titular
        else: 
            raise RuntimeError("O nome do titular deve ser um texto")
        self.saldo = float(saldo_inicial)

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if isinstance(value, (float, int)) and value >= 0:
            self.__saldo = value
        else:
            raise RuntimeError("O valor do saldo deve ser um número não-negativo")

    def depositar(self, value):
        if isinstance(value,(float, int)) and value > 0:
            self.__saldo += value
            print(f"Deposito de R$ {value:.2f} realizado com sucesso.")
        else:
            raise RuntimeError("O valor depositado deve ser um número e maior que zero")
        
    def sacar(self, value):
        if isinstance(value,(float, int)) and self.saldo > value > 0       :
            self.__saldo -= value
            print(f"Saque de R$ {value:.2f} realizado com sucesso.")
        else:
            raise RuntimeError("O valor retirado deve ser um número maior que zero e que o saldo atual")
            
    def __add__(self, other):
        if isinstance(other, ContaBancaria):
            novo_saldo = self.saldo + other.saldo
            other.saldo = 0
            novo_titular = (f'{self.titular} & {other.titular}')
            return ContaBancaria(novo_titular, novo_saldo)
        else:
            raise RuntimeError("Ambos os objetos devem ser contas bancarias")
        
    def __str__(self):
        return (f'Conta de: [{self.titular}]; Saldo: [{self.saldo}]')

if __name__ == '__main__':
    c1 = ContaBancaria("Ana", 500.0)
    c2 = ContaBancaria("Carlos", 200.0)
    print(c1)  # Saída esperada: Conta de Ana - Saldo: R$ 500.0

    #   Testando encapsulamento e métodos de depósito/saque
    c1.depositar(150.0)
    c1.sacar(100.0)
    print(c1.saldo)  # Saída esperada: 550.0

# Tentativa de acesso direto ao atributo privado deve falhar (ex: AttributeError)
try:
    print(c1.__saldo)
except Exception as e:
    print(f'Erro: {e}')
# Testando o método __add__ (fusão de contas)
conta_total = c1 + c2
print(conta_total)  # Deve refletir a soma ou a operação definida na lógica do dunder method