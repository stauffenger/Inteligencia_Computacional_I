import arvore_busca_ic_1

class Caminho:
	def __init__(self, nome):
		self.nome = nome
		self.baixo = None	
		self.esquerda = None
		self.cima = None
		self.direita = None

	def definir_caminho_sem_custo(self, baixo, esquerda, cima, direita):
		self.baixo = baixo	
		self.esquerda = esquerda
		self.cima = cima
		self.direita = direita

def definir_caminho_do_labirinto_sem_custo(labirinto):
	for no in labirinto:
		if no.nome == "A":
			no.definir_caminho_sem_custo(labirinto[1], None, None, labirinto[4])
		elif no.nome == "B":
			no.definir_caminho_sem_custo(labirinto[2], None, labirinto[0], labirinto[5])
		elif no.nome == "C":
			no.definir_caminho_sem_custo(None, None, labirinto[1], None)
		elif no.nome == "D":
			no.definir_caminho_sem_custo(None, None, None, labirinto[7])
		elif no.nome == "E":
			no.definir_caminho_sem_custo(None, labirinto[0], None, labirinto[8])
		elif no.nome == "F":
			no.definir_caminho_sem_custo(labirinto[6], labirinto[1], None, None)
		elif no.nome == "G":
			no.definir_caminho_sem_custo(labirinto[7], None, labirinto[5], labirinto[10])
		elif no.nome == "H":
			no.definir_caminho_sem_custo(None, labirinto[3], labirinto[6], None)
		elif no.nome == "I":
			no.definir_caminho_sem_custo(labirinto[9], labirinto[4], None, labirinto[12])
		elif no.nome == "J":
			no.definir_caminho_sem_custo(None, None, labirinto[8], labirinto[13])
		elif no.nome == "L":
			no.definir_caminho_sem_custo(labirinto[11], labirinto[6], None, None)
		elif no.nome == "M":
			no.definir_caminho_sem_custo(None, None, labirinto[10], labirinto[15])
		elif no.nome == "N":
			no.definir_caminho_sem_custo(None, labirinto[8], None, None)
		elif no.nome == "O":
			no.definir_caminho_sem_custo(labirinto[14], labirinto[9], None, labirinto[16])
		elif no.nome == "P":
			no.definir_caminho_sem_custo(labirinto[15], None, labirinto[13], labirinto[17])
		elif no.nome == "Q":
			no.definir_caminho_sem_custo(None, labirinto[11], labirinto[14], None)
		elif no.nome == "R":
			no.definir_caminho_sem_custo(None, labirinto[13], None, None)
		elif no.nome == "S":
			no.definir_caminho_sem_custo(None, labirinto[14], None, None)

def inicializar_labirinto_sem_custo(labirinto):
	alfabeto = ord("A")
	for i in range(19):
		nome = chr(alfabeto)
		if not(nome == "K"):
			labirinto.append(Caminho(nome))
		alfabeto += 1
	definir_caminho_do_labirinto_sem_custo(labirinto)

def inicializar_pilha_abertos_sem_custo(labirinto, pilha_de_abertos):
	no_raiz = arvore_busca_ic_1.ArvoreBusca(labirinto[0].nome, [], None)
	pilha_de_abertos.append(no_raiz)

def inicializar_fila_abertos_sem_custo(labirinto, fila_de_abertos):
	no_raiz = arvore_busca_ic_1.ArvoreBusca(labirinto[0].nome, [], None)
	fila_de_abertos.insert(0, no_raiz)

class CaminhoComCusto:
	def __init__(self, nome):
		self.nome = nome
		self.lista_de_ligacoes = []

	def definir_caminho_com_custo(self, caminho_a_adicionar, custo_do_caminho):
		self.lista_de_ligacoes.extend(caminho_a_adicionar, custo_do_caminho)