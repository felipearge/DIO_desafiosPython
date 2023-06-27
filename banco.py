#variaveis auxiliares
saldo = 0
limite_diario_valor = 500
limite_diario_tran = 3
valor_deposito = 0
aux_tran_diaria = 0
aux_valorTotal_transf = 0

#funções para saque, deposito e extrado
def exibir_opcoes():
  print("**-----------------------------------------**")
  print("**-----------------------------------------**")
  print("**-----------------------------------------**")
  print("Bem vindo ao banco, escolha a sua opção:")
  print("1 - Depositar")
  print("2 - Sacar")
  print("3 - Ver extrato")
  print("4 - Sair")


def saque(valor):
  global saldo, aux_tran_diaria, aux_valorTotal_transf

  if aux_tran_diaria == 3:
      print("Limite de transações de saque atingido")

  if aux_valorTotal_transf == 500 or valor > 500:
      print("Limite do valor de saque atintigo")
  
  if (valor < saldo) and (valor <=500) and (aux_tran_diaria < limite_diario_tran) and (aux_valorTotal_transf < limite_diario_valor):
      saldo = saldo - valor
      aux_tran_diaria += 1
      aux_valorTotal_transf += valor
      print(f"Saque de R$ {valor:.2f} realizado.")
      #print(f"Saldo em conta de R$ {saldo:.2f} \n")
      imprimir_saldo()
    

def deposito(valor):
  global saldo
  saldo = saldo + valor
  ##print(f"Saldo na conta de R$ {saldo:.2f}")
  imprimir_saldo()


def imprimir_saldo():
   print(f"Seu saldo é de R$ {saldo:.2f}\n")


#___________________________________________________

exibir_opcoes()
entrada = 0

while entrada != 4:
  entrada = int(input())

  if entrada == 1:
    #print("Digite o valor a ser depositado: ")
    valor_deposito = int(input("Digite o valor a ser depositado: "))
    deposito(valor_deposito)
  
  elif entrada == 2:
    valor_sacar = int(input("Digite o valor que deseja sacar: "))
    saque(valor_sacar)
  
  elif entrada == 3:
    imprimir_saldo()

  elif entrada == 4:
    print("Atendimento finalizado")
    
  exibir_opcoes()

  exibir_opcoes()

