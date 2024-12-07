class ContaBancaria:
    def __init__(self,titular,saldo,limite):
        self.titular = str(titular)
        self.saldo = float(saldo)
        self.limite = float(limite)

    def depositar(self,valor):
        if valor >= 0:
            self.saldo += float(valor)
            print(1)
        else:
            print(0)

    def levantar(self,valor):
        if valor >= self.saldo+self.limite:
            print(0)
        else:
            self.saldo-=valor
            print(1)

    def exibir_saldo(self):
        print(format(self.saldo,".2f"))

    def exibir_info(self):
        print(self.titular, self.saldo, self.limite)


conta = ContaBancaria("João", 1000.00, 500.00)
conta.depositar(-500.00)
conta.depositar(500.00)
conta.levantar(1200.00)
conta.levantar(1200.00)
conta.exibir_saldo()
conta.exibir_info()
