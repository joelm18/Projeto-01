class Register:

  #Método construtor da classe
  def __init__(self, name, age, balance, cpf):
    self.nome = name
    self.idade = age
    self.saldo = balance
    self.cpf = cpf
  # Cadastra o usuário
  def register(self, name, age, balance, cpf):
    self.nome = name
    self.idade = age
    self.saldo = balance
    self.cpf = cpf
    
  # Consulta o saldo da galera
  def get_balance(self, balance):
    self.saldo = balance
    return balance

  def update_balance(self, new_balance):
    self.saldo = new_balance