import arvore_busca_ic_1

class Caminho:
	def __init__(self, nome):
		self.nome = nome
		self.baixo = []	
		self.esquerda = []
		self.cima = []
		self.direita = []

def definir_caminho_do_labirinto_sem_custo(labirinto):
	for no in labirinto:
		if no.nome == "A":
			no.baixo.extend([labirinto[1], None])#i.esquerda =#i.cima = 
			no.direita.extend([labirinto[4], None])
		elif no.nome == "B":
			no.baixo.extend([labirinto[2], None])#i.esquerda =
			no.cima.extend([labirinto[0], None])
			no.direita.extend([labirinto[5], None])
		elif no.nome == "C":#i.baixo =#i.esquerda =
			no.cima.extend([labirinto[1], None])#i.direita =
		elif no.nome == "D":#i.baixo =#i.esquerda =#i.cima = 
			no.direita.extend([labirinto[7], None])
		elif no.nome == "E":#i.baixo =
			no.esquerda.extend([labirinto[0], None])#i.cima = 
			no.direita.extend([labirinto[8], None])
		elif no.nome == "F":
			no.baixo.extend([labirinto[6], None])
			no.esquerda.extend([labirinto[1], None])#i.cima =#i.direita =
		elif no.nome == "G":
			no.baixo.extend([labirinto[7], None])#i.esquerda = 
			no.cima.extend([labirinto[5], None])
			no.direita.extend([labirinto[10], None])
		elif no.nome == "H":#i.baixo = 
			no.esquerda.extend([labirinto[3], None])
			no.cima.extend([labirinto[6], None])#i.direita =
		elif no.nome == "I":
			no.baixo.extend([labirinto[9], None])
			no.esquerda.extend([labirinto[4], None])#i.cima = 
			no.direita.extend([labirinto[12], None])
		elif no.nome == "J":#i.baixo =#i.esquerda = 
			no.cima.extend([labirinto[8], None])
			no.direita.extend([labirinto[13], None])
		elif no.nome == "L":
			no.baixo.extend([labirinto[11], None])
			no.esquerda.extend([labirinto[6], None])#i.cima =#i.direita =
		elif no.nome == "M":#i.baixo =#i.esquerda = 
			no.cima.extend([labirinto[10], None])
			no.direita.extend([labirinto[15], None])
		elif no.nome == "N":#i.baixo = 
			no.esquerda.extend([labirinto[8], None])#i.cima =#i.direita =
		elif no.nome == "O":
			no.baixo.extend([labirinto[14], None])
			no.esquerda.extend([labirinto[9], None])#i.cima = 
			no.direita.extend([labirinto[16], None])
		elif no.nome == "P":
			no.baixo.extend([labirinto[15], None])#i.esquerda = 
			no.cima.extend([labirinto[13], None])
			no.direita.extend([labirinto[17], None])
		elif no.nome == "Q":#i.baixo = 
			no.esquerda.extend([labirinto[11], None])
			no.cima.extend([labirinto[14], None])#i.direita =
		elif no.nome == "R":#i.baixo = 
			no.esquerda.extend([labirinto[13], None])#i.cima =#i.direita =
		elif no.nome == "S":#i.baixo = 
			no.esquerda.extend([labirinto[14], None])#i.cima =#i.direita =

def inicializar_labirinto(labirinto):
	alfabeto = ord("A")
	for i in range(19):
		nome = chr(alfabeto)
		if not(nome == "K"):
			labirinto.append(Caminho(nome))
		alfabeto += 1
	definir_caminho_do_labirinto_sem_custo(labirinto)

def inicializar_pilha_abertos(labirinto, pilha_de_abertos):
	no_raiz = arvore_busca_ic_1.ArvoreBusca(labirinto[0].nome, [], None)
	pilha_de_abertos.append(no_raiz)

def inicializar_fila_abertos(labirinto, fila_de_abertos):
	no_raiz = arvore_busca_ic_1.ArvoreBusca(labirinto[0].nome, [], None)
	fila_de_abertos.insert(0, no_raiz)