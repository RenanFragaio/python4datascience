#criando e adicionando
'''Um algoritmo que recebe duas listas, uma de nomes e outra de valores de preços. Representando gastos. Ele pega uma planilha de gastos e cria categorias para cada nome, informando o total de gastos de cada categoria.'''

nomes = ['nubank','uber','burgerking','itau','nubank','burgerking','nubank','uber','burgerking','uber']

valores = [8.00,10.00,12.00,15.00,8.00,12.00,8.00,10.00,12.00,10.00]
categorias = [] #uma lista contendo os objetos que serão criados

class Categoria:
  def __init__(self,nome,valor):
    self.nome = nome
    self.valor = valor

def criar_categoria(nome,valor):
  return Categoria(nome,valor)


#1ª vez: criar categoria com o primeiro nome (cancelado por causa do construtor)
'''i=0
categorias.append(criar_categoria(nomes[i],valores[i]))
print("nomes[",i,"] =",nomes[i]," , valores[",i,"] = ",valores[i])
print("categorias[0].valor: ",categorias[i].valor)'''
#i=i+1

#print("len(nomes): ", len(nomes))
for i in range(len(nomes)):
  #2ª vez (agora 1ª vez) em diante: ver se nome já existe na lista de categorias
  #print("iteração: ",i)
  j=0
  existe = False
  #string vazia é falsa. se string não é vazia, ainda não está no final da lista.
  loop = True
  #while(loop == True): é redundante, pois python considera qualquer valor não zero e não vazio como True
  while(loop): 
    try:
      #Não está no final da lista, então continua
      if(categorias[j].nome != False):
        loop = True
        #Verifica se dentro da lista existe o nome. Se existir, pare.
        if(nomes[i] == categorias[j].nome):
          #print("nome já existe na posição: ",j," iteração: ",i)
          #print("categorias[j].valor: ",categorias[j].valor," += valores[i] =",valores[i])
          categorias[j].valor += valores[i]
          existe = True
          loop = False
        j=j+1
      else:
        print("posição vazia.fim da lista, sair")
        loop = False
    except IndexError:
      #deu erro porque o indice não existe. Não continue buscando
      #print("the index does not exist, end search.")
      loop = False 

  '''while(categorias[j].nome != False):
    if(nomes[i] == categorias[j].nome):
      print("nome já existe")
      existe = True
    j=j+1'''

  #a busca foi feita em toda a lista de categorias e o item do vetor "nomes" ñ existe: Criar
  if (existe == False):
    print("nome não existe na lista de categorias\n")
    categorias.append(criar_categoria(nomes[i],valores[i]))
    print("Categoria \"",categorias[i].nome,"\" criada com sucesso!\n")

#imprimindo a lista
j=0
loop = True
while(loop):
  try:
    if(categorias[j].nome != False):
      print("\n",categorias[j].nome,"\n")
      print(categorias[j].valor,"\n")
      j=j+1
    else:
      loop = False
  except IndexError:
    #print("the index does not exist, end search.")
    loop = False

'''while(categorias[j].nome != False):
  print(categorias[j].nome,"\n")
  print(categorias[j].valor,"\n")
  j=j+1'''