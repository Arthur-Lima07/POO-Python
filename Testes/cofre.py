class CofreDigital:
    def __init__(self, senha_inicial: str):
        if isinstance(senha_inicial, str) and len(senha_inicial) == 4 :
            self.senha = senha_inicial
        else:
            print("Senha inválida! A senha deve ter exatamente 4 dígitos. Definida como '0000'.")
            self.__senha = "0000"
        self.saldo = 0.0
        self.esta_aberto = False

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, value):
        if isinstance(value, str) and len(value) == 4:
            self.__senha = value
        else:
            raise RuntimeError("A senha deve ser uma string não-vazia")

    @property
    def saldo(self):
        if self.esta_aberto == True:
            return self.__saldo
        else:
            raise RuntimeError("Acesso negado: abra o cofre para visualizar o saldo.")

    @saldo.setter
    def saldo(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__saldo = float(value)
        else:
            raise RuntimeError("O saldo deve ser um valor númerico e não-negativo")

    @property
    def esta_aberto(self):
        return self.__esta_aberto

    @esta_aberto.setter
    def esta_aberto(self, value):
        self.__esta_aberto = bool(value)

    def abrir(self, senha_digitada):
        if self.__senha == senha_digitada:
            print("Cofre aberto com sucesso!")
            self.esta_aberto = True
        else:
            raise RuntimeError("Senha incorreta!")

    def fechar(self):
        if self.esta_aberto == True:
            print("Cofre fechado")
            self.__esta_aberto = False
        else:
            raise RuntimeError("Para fechar o cofre, ele deve estar aberto")

    def depositar(self, other):
        if isinstance(other, (int,float)):
            if other > 0:
                if self.esta_aberto == True:
                    self.__saldo += other
                    print(f"Depósito de R$ {other} efetuado.")
                else:
                    raise RuntimeError("Operação negada: O cofre está fechado!")
            else:
                raise RuntimeError("Operação negada: O valor do deposito deve ser maior que 0")
        else:
            raise RuntimeError("Operação negada: O valor do deposito deve ser numérico")

    def sacar(self, other):
        if isinstance(other, (int,float)):
            if other > 0:
                if self.saldo >= other:
                    if self.esta_aberto == True:
                        self.__saldo -= other
                        print(f"Saque de R$ {other} efetuado.")
                    else:
                        raise RuntimeError("Operação negada: O cofre está fechado")
                else:
                    raise RuntimeError("O valor do saque deve ser menor que o saldo")
            else:
                raise RuntimeError("O valor do saque deve ser maior que zero")
        else:
            raise RuntimeError("Operação negada: O valor do saque deve ser numérico")


if __name__ == "__main__":
    meu_cofre = CofreDigital("1234")
    meu_cofre.abrir("1234")
    meu_cofre.depositar(100.0)
    print(f"Saldo atual: R$ {meu_cofre.saldo:.2f}")
    meu_cofre.sacar(20)
    print(f"Saldo atual: R$ {meu_cofre.saldo:.2f}")
    meu_cofre.fechar()

    try:
        meu_cofre.depositar(100.0)
    except Exception as e:
        print(f"Erro: {e}")
    try:
        meu_cofre.abrir("1234")
        meu_cofre.depositar(-100.0)
    except Exception as e:
        print(f"Erro: {e}")
    try:
        meu_cofre.abrir("1234")
        meu_cofre.depositar("100.0")
    except Exception as e:
        print(f"Erro: {e}")
    try:
        meu_cofre.abrir("1234")
        meu_cofre.depositar(50.0)
        meu_cofre.sacar(200.0)
    except Exception as e:
        print(f"Erro: {e}")
    try:
        meu_cofre.abrir("1234")
        meu_cofre.sacar("20.0")
    except Exception as e:
        print(f"Erro: {e}")
    try:
        meu_cofre.abrir("1234")
        meu_cofre.sacar(-20.0)
    except Exception as e:
        print(f"Erro: {e}")
    try:
        meu_cofre.fechar()
    except Exception as e:
        print(f'Erro: {e}')
    try:
        meu_cofre.abrir('1234')
        meu_cofre.depositar(100.0)
        meu_cofre.fechar()
        meu_cofre.depositar(50.0)
        meu_cofre.sacar(50.0)
    except Exception as e:
        print(f'Erro: {e}')
