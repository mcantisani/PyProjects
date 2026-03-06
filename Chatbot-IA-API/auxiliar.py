# listas são estruturas de dados que armazenam uma coleção de elementos, que podem ser de tipos diferentes. 
# Elas são mutáveis, ou seja, é possível modificar seus elementos após a criação da lista. 
# As listas são definidas usando colchetes [] e os elementos são separados por vírgulas. Exemplo:        

lista = []
nomes = ["Maria", "João", "Ana", "Pedro"]
print(nomes[0]) #acessar o primeiro elemento da lista
nomes.append("Carla") #adicionar um elemento no final da lista
print(nomes)

# dicionários são estruturas de dados que armazenam pares de chave-valor.
# Eles são mutáveis e definidos usando chaves {}. Cada par chave-valor é separado por vírgula, 
# e a chave e o valor são separados por dois pontos. Exemplo:
dicionario = {}
pessoa = {"nome": "Maria", "idade": 30, "cidade": "São Paulo"}
print(pessoa["idade"]) #acessar o valor da chave "nome"
pessoa["profissão"] = "Engenheira" #adicionar um novo par chave-valor ao dicionário
print(pessoa)
pessoa["hobby"] = "Cozinhar" #adicionar um novo par chave-valor ao dicionário
print(pessoa)

# um exemplo do uso de listas com dicionários é:

mensagem1 = {"role": "human", "content": "Você é um assistente útil e amigável."}
mensagem2 = {"role": "assistant", "content": "Qual é a capital da França?"}
mensagem3 = {"role": "human", "content": "A capital da França é Paris."}

lista_mensagens = [mensagem1, mensagem2, mensagem3]
print(lista_mensagens)

nova_mensagem = {"role": "assistant", "content": "Obrigado por me informar!"}
lista_mensagens.append(nova_mensagem)
print(lista_mensagens)