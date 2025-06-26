class Nodo: 
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
      self.tabela = [None for _ in range(10)]
    
    def funcao_hash(self, sigla):
      if sigla == 'DF':
         return 7
      else:
         return (ord(sigla[0]) + ord(sigla[1])) % 10
    
    def inserir(self, sigla, nomeEstado):
       pos = self.funcao_hash(sigla)
       novo_nodo = Nodo(sigla, nomeEstado)
       novo_nodo.proximo = self.tabela[pos]
       self.tabela[pos] = novo_nodo
    
    def imprimir(self):
       for i in range(10):
          print(f"Posição {i}:", end=" ")
          atual = self.tabela[i]
          if not atual:
             print("None")
          else:
             while atual:
                print(f"{atual.sigla}", end=" -> ")
                atual = atual.proximo
             print("None")

estados = [
   ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), 
   ("AM", "Amazonas"), ("BA", "Bahia"), ("CE", "Ceará"), 
   ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), 
   ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), 
   ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"), 
   ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), 
   ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"),
   ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
   ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
   ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
]

estado_ficticio = ("PJ", "Pessoa João")

tabela = TabelaHash()

print("\n[Saída 1] Tabela Hash antes de inserir informação:")
tabela.imprimir()

print("\n[Saída 2] Tabela hash após inserir os 26 estados + DF:")
for sigla, nome in estados:
    tabela.inserir(sigla, nome)
tabela.imprimir()

print("\n[Saída 3] Tabela hash após inserir os 26 estados + DF + estado fictício:")
tabela.inserir(estado_ficticio[0], estado_ficticio[1])
tabela.imprimir()

        
        