class Nodo: 
  def __init__(self, numero, cor):
    self.numero = numero
    self.cor = cor
    self.proximo = None

class ListaEncadeada:
  def __init__(self):
    self.head = None
    self.contador_verde = 1
    self.contador_amarelo = 201

  def inserirSemPrioridade(self, novo_nodo):
    if self.head is None:
      self.head = novo_nodo
    else:
      atual = self.head
      while atual.proximo is not None:
        atual = atual.proximo
      atual.proximo = novo_nodo

  def inserirComPrioridade(self, novo_nodo):
    if self.head is None or self.head.cor == 'V':
      novo_nodo.proximo = self.head
      self.head = novo_nodo
    else:
      atual = self.head
      while atual.proximo is not None and atual.proximo.cor == 'A':
        atual = atual.proximo
      novo_nodo.proximo = atual.proximo
      atual.proximo = novo_nodo
  
  def inserir(self):
    while True: 
      cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
      if cor == 'A':
        numero = self.contador_amarelo
        self.contador_amarelo += 1
        nodo = Nodo(numero, cor)
        self.inserirComPrioridade(nodo)
        break
      elif cor == 'V':
        numero = self.contador_verde
        self.contador_verde += 1
        nodo = Nodo(numero, cor)
        self.inserirSemPrioridade(nodo)
        break
      else:
        print("Cor inválida. Por favor, digite 'A' ou 'V'.")

  def imprimirListaEspera(self):
    atual = self.head
    if not atual:
      print("Fila de espera vazia.")
      return
    print("\n Lista de espera:")
    while atual: 
      print(f"Cartão {atual.cor}{atual.numero}")
      atual = atual.proximo
    print("---------------------------\n")

  def atenderPaciente(self):
    if self.head is None:
      print("Fila de espera vazia.")
    else:
      atendido = self.head
      print(f"Chamando paciente com cartão {atendido.cor}{atendido.numero}")
      self.head = self.head.proximo

def menu():
  lista = ListaEncadeada()
  while True:
    print("\nMenu:")
    print("1. Inserir paciente na lista de espera")
    print("2. Mostrar pacientes na lista de espera")
    print("3. Chamar paciente")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
      lista.inserir()
    elif opcao == '2':
      lista.imprimirListaEspera()
    elif opcao == '3':
      lista.atenderPaciente()
    elif opcao == '4':
      print("Saindo do programa.")
      break
    else:
      print("Opção inválida. Tente novamente.")

menu()
