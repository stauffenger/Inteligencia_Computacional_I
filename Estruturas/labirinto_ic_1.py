import arvore_busca_ic_1

class Caminho:
	def __init__(self, nome, baixo, esquerda, cima, direita):
		self.nome = nome
		self.baixo = baixo
		self.esquerda = esquerda
		self.cima = cima
		self.direita = direita

def Definir_caminho_labirinto(labirinto):
	for no in labirinto:
		if no.nome == "A":
			no.baixo = labirinto[1]#i.esquerda =#i.cima = 
			no.direita = labirinto[4]
		elif no.nome == "B":
			no.baixo = labirinto[2]#i.esquerda =
			no.cima = labirinto[0]
			no.direita = labirinto[5]
		elif no.nome == "C":#i.baixo =#i.esquerda =
			no.cima = labirinto[1]#i.direita =
		elif no.nome == "D":#i.baixo =#i.esquerda =#i.cima = 
			no.direita = labirinto[7]
		elif no.nome == "E":#i.baixo =
			no.esquerda = labirinto[0]#i.cima = 
			no.direita = labirinto[8]
		elif no.nome == "F":
			no.baixo = labirinto[6]
			no.esquerda = labirinto[1]#i.cima =#i.direita =
		elif no.nome == "G":
			no.baixo = labirinto[7]#i.esquerda = 
			no.cima = labirinto[5]
			no.direita = labirinto[10]
		elif no.nome == "H":#i.baixo = 
			no.esquerda = labirinto[3]
			no.cima = labirinto[6]#i.direita =
		elif no.nome == "I":
			no.baixo = labirinto[9]
			no.esquerda = labirinto[4]#i.cima = 
			no.direita = labirinto[12]
		elif no.nome == "J":#i.baixo =#i.esquerda = 
			no.cima = labirinto[8]
			no.direita = labirinto[13]
		elif no.nome == "L":
			no.baixo = labirinto[11]
			no.esquerda = labirinto[6]#i.cima =#i.direita =
		elif no.nome == "M":#i.baixo =#i.esquerda = 
			no.cima = labirinto[10]
			no.direita = labirinto[15]
		elif no.nome == "N":#i.baixo = 
			no.esquerda = labirinto[8]#i.cima =#i.direita =
		elif no.nome == "O":
			no.baixo = labirinto[14]
			no.esquerda = labirinto[9]#i.cima = 
			no.direita = labirinto[16]
		elif no.nome == "P":
			no.baixo = labirinto[15]#i.esquerda = 
			no.cima = labirinto[13]
			no.direita = labirinto[17]
		elif no.nome == "Q":#i.baixo = 
			no.esquerda = labirinto[11]
			no.cima = labirinto[14]#i.direita =
		elif no.nome == "R":#i.baixo = 
			no.esquerda = labirinto[13]#i.cima =#i.direita =
		elif no.nome == "S":#i.baixo = 
			no.esquerda = labirinto[14]#i.cima =#i.direita =

def Inicializar_labirinto(labirinto):
	alfabeto = ord("A")
	for i in range(19):
		nome = chr(alfabeto)
		if not(nome == "K"):
			labirinto.append(Caminho(nome, None, None, None, None))
		alfabeto += 1
	Definir_caminho_labirinto(labirinto)

def Inicializar_pilha_abertos(labirinto, pilha_de_abertos, arvore_busca):
	no_raiz = arvore_busca_ic_1.Arvore_busca(labirinto[0].nome, [])
	arvore_busca = no_raiz
	pilha_de_abertos.append(no_raiz)

def Inicializar_fila_abertos(labirinto, fila_de_abertos, arvore_busca):
	no_raiz = arvore_busca_ic_1.Arvore_busca(labirinto[0].nome, [])
	arvore_busca = no_raiz
	fila_de_abertos.insert(0, no_raiz)