usuarios = []
contas = []
id_usuario = 1
id_conta = 1

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.id = id_usuario
        id_usuario += 1

class Conta:
    def __init__(self, usuario):
        self.numero = id_conta
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUE = 3
        id_conta += 1

def criar_usuario(nome, cpf):
    global id_usuario
    usuario = Usuario(nome, cpf)
    usuarios.append(usuario)
    id_usuario += 1
    return usuario.id

def criar_conta(id_usuario):
    global id_conta
    usuario = None
    for u in usuarios:
        if u.id == id_usuario:
            usuario = u
            break
    if not usuario:
        return False, "Usuário não encontrado."
    conta = Conta(usuario)
    contas.append(conta)
    id_conta += 1
    return conta.numero, conta.saldo

def depositar(numero_conta, valor):
    conta = None
    for c in contas:
        if c.numero == numero_conta:
            conta = c
            break
    if not conta:
        return False, "Conta não encontrada."
    if valor <= 0:
        return False, "Valor inválido."
    conta.saldo += valor
    conta.extrato += f"Depósito: R$ {valor:.2f}\n"
    return True, f"Depósito de R$ {valor:.2f} efetuado com sucesso."

def sacar(numero_conta, valor):
    conta = None
    for c in contas:
        if c.numero == numero_conta:
            conta = c
            break
    if not conta:
        return False, "Conta não encontrada."
    excedeu_saldo = valor > conta.saldo
    excedeu_limite = valor > conta.limite
    excedeu_saque = conta.numero_saques >= conta.LIMITE_SAQUE
    if excedeu_saldo:
        return False, "Saldo insuficiente."
    elif excedeu_limite:
        return False, "Valor do saque excede o limite permitido."
    elif excedeu_saque:
        return False, "Número máximo de saques atingido."
    elif valor <= 0:
        return False, "Valor inválido."
    conta.saldo -= valor
    conta.numero_saques += 1
    conta.extrato += f"Saque: R$ {valor:.2f}\n"
    return True, f"Saque de R$ {valor:.2f} efetuado com sucesso."

def extrato(numero_conta):
    conta = None
    for c in contas:
        if c.numero == numero_conta:
            conta = c
            break
    if not conta:
        return False, "Conta não encontrada."
    return True, conta.extrato, conta.saldo



