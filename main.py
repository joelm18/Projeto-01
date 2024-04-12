from register import Register
import os

clients = []

print("Bem-vindo ao Super mercado!")
print("-----------------------------------------------")
print("Digite uma das opções a seguir:")
print("1 - Cadastrar cliente")
print("2 - Consultar saldo do cliente")
print("3 - Atualizar saldo do cliente")
print("4 - Ver lista de clientes cadastrados")
print("5 - Remover um cliente")
print("6 - Limpar tela")
print("7 - Sair")
print("-----------------------------------------------")

def menu():
    while True:
      try:
        option = int(input("Digite a opção desejada: "))
        if option == 1:
          name = input("Digite o nome do cliente: ")
          age = int(input("Digite a idade do cliente: "))
          balance = float(input("Digite o saldo do cliente: "))
          cpf = int(input("Digite o CPF do cliente: "))
          client = Register(name, age, balance, cpf)
          clients.append(client)

          #Salva o cliente no arquivo ao invés de escolher a opção de salvar
          with open("clients.txt", "a") as file:
            file.write(f" Nome:\t{name}\n Idade:\t{age}\n Saldo:\t{balance}\n CPF:\t{cpf}\n")
          
          print("Cliente cadastrado com sucesso!")
        elif option == 2:
          cpf = int(input("Digite o CPF do cliente: "))
          for client in clients:
            if client.cpf == cpf:
              print(f"Saldo do cliente {client.nome}: R${client.saldo}")
              break
          else:
            print("Cliente não encontrado!")
        elif option == 3:
          cpf = int(input("Digite o CPF do cliente: "))
          new_balance = int(input("Digite o novo saldo do cliente: "))
          for client in clients:
            if client.cpf == cpf:
              client.update_balance(new_balance)
              print("Saldo atualizado com sucesso!")
              break
          else:
            print("Cliente não encontrado!")
        elif option == 4:
          with open("clients.txt", "r") as file:
            for line in file:
              print(line.strip())
        elif option == 5:
          cpf = int(input("Digite o CPF do cliente: "))
          for client in clients:
            if client.cpf == cpf:
              clients.remove(client)
              print("Cliente removido com sucesso!")
              break
          else:
            print("Cliente não encontrado!")
        elif option == 6:
          os.system('cls' if os.name == 'nt' else 'clear')
        elif option == 7:
          print("Obrigado por usar o Super mercado!")
          break
        elif option is "":
          print("A opção precisa ser um inteiro")
        else:
          print("Opção inválida!")
      except ValueError:
        print("Por favor, digite um número inteiro para a opção.")

menu()