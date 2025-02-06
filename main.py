import textwrap

# Configuração do banco
AGENCIA = "0001"
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500


class Usuario:
    """Representa um usuário do banco."""

    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __repr__(self):
        return f"{self.nome} ({self.cpf})"


class ContaBancaria:
    """Representa uma conta bancária."""

    def __init__(self, usuario):
        self.agencia = AGENCIA
        self.numero_conta = len(banco.contas) + 1
        self.usuario = usuario
        self.saldo = 0
        self.saques_realizados = 0
        self.transacoes = []

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: R$ {valor:.2f}")
            print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\n❌ O valor precisa ser positivo!")

    def sacar(self, valor):
        """Realiza um saque, respeitando limites."""
        if self.saques_realizados >= LIMITE_SAQUES:
            print("\n❌ Limite de saques diários atingido!")
            return
        if valor > self.saldo:
            print("\n❌ Saldo insuficiente!")
            return
        if valor > LIMITE_VALOR_SAQUE:
            print(f"\n❌ O saque máximo permitido é R$ {LIMITE_VALOR_SAQUE:.2f}!")
            return

        self.saldo -= valor
        self.saques_realizados += 1
        self.transacoes.append(f"Saque: R$ {valor:.2f}")
        print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        """Exibe o extrato da conta."""
        print("\n📜 Extrato Bancário")
        print("-" * 30)
        for transacao in self.transacoes:
            print(transacao)
        print("-" * 30)
        print(f"💰 Saldo atual: R$ {self.saldo:.2f}")


class Banco:
    """Gerencia contas e usuários."""

    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        """Cria um novo usuário no banco."""
        cpf = input("Informe seu CPF (somente números): ").strip()
        if any(usuario.cpf == cpf for usuario in self.usuarios):
            print("\n❌ CPF já cadastrado!")
            return

        nome = input("Nome completo: ").strip()
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        endereco = input(
            "Endereço (logradouro, número - bairro - cidade/estado): "
        ).strip()

        usuario = Usuario(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(usuario)
        print("\n✅ Usuário criado com sucesso!")

    def criar_conta(self):
        """Cria uma nova conta bancária para um usuário existente."""
        cpf = input("Informe o CPF do titular da conta: ").strip()
        usuario = next((user for user in self.usuarios if user.cpf == cpf), None)

        if not usuario:
            print("\n❌ Usuário não encontrado. Cadastre-o primeiro!")
            return

        conta = ContaBancaria(usuario)
        self.contas.append(conta)
        print(
            f"\n✅ Conta criada com sucesso! Agência: {conta.agencia} | Conta: {conta.numero_conta}"
        )

    def buscar_conta_por_cpf(self, cpf):
        """Busca uma conta bancária pelo CPF do usuário."""
        return next((conta for conta in self.contas if conta.usuario.cpf == cpf), None)


banco = Banco()


def menu():
    """Exibe o menu do sistema."""
    return textwrap.dedent("""
        [1] Criar Usuário
        [2] Criar Conta Corrente
        [3] Depositar
        [4] Sacar
        [5] Extrato
        [0] Sair
        => """).strip()


def realizar_deposito():
    """Realiza um depósito em uma conta existente."""
    cpf = input("Informe o CPF do titular da conta: ").strip()
    conta = banco.buscar_conta_por_cpf(cpf)

    if conta:
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            conta.depositar(valor)
        except ValueError:
            print("\n❌ Valor inválido! Digite um número válido.")
    else:
        print("\n❌ Conta não encontrada!")


def realizar_saque():
    """Realiza um saque em uma conta existente."""
    cpf = input("Informe o CPF do titular da conta: ").strip()
    conta = banco.buscar_conta_por_cpf(cpf)

    if conta:
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            conta.sacar(valor)
        except ValueError:
            print("\n❌ Valor inválido! Digite um número válido.")
    else:
        print("\n❌ Conta não encontrada!")


def exibir_extrato():
    """Exibe o extrato bancário de um usuário."""
    cpf = input("Informe o CPF do titular da conta: ").strip()
    conta = banco.buscar_conta_por_cpf(cpf)

    if conta:
        conta.exibir_extrato()
    else:
        print("\n❌ Conta não encontrada!")


def main():
    """Loop principal do sistema bancário."""
    while True:
        opcao = input(menu())

        if opcao == "1":
            banco.criar_usuario()
        elif opcao == "2":
            banco.criar_conta()
        elif opcao == "3":
            realizar_deposito()
        elif opcao == "4":
            realizar_saque()
        elif opcao == "5":
            exibir_extrato()
        elif opcao == "0":
            print("\n👋 Obrigado por usar nosso sistema bancário!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
