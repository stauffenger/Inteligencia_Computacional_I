import arvore_busca_ic_1
from enum import Enum

class TipoDeGrafo(Enum):
	MODELO_SEM_CUSTO_1 = 0
	MODELO_COM_CUSTO_1 = 1
	MODELO_COM_CUSTO_2 = 2

class NoGrafoLabirinto:
	def __init__(self, nome):
		self.nome = nome
		self.baixo = None	
		self.esquerda = None
		self.cima = None
		self.direita = None

	def definir_ligacoes_labirinto(self, baixo, esquerda, cima, direita):
		self.baixo = baixo	
		self.esquerda = esquerda
		self.cima = cima
		self.direita = direita

def definir_caminho_do_grafo(grafo, tipo_de_grafo):
	if tipo_de_grafo == TipoDeGrafo.MODELO_SEM_CUSTO_1:
		definir_caminho_do_grafo_sem_custo(grafo, tipo_de_grafo)
	elif tipo_de_grafo == TipoDeGrafo.MODELO_COM_CUSTO_1 or tipo_de_grafo == TipoDeGrafo.MODELO_COM_CUSTO_2:
		definir_caminho_do_grafo_com_custo(grafo, tipo_de_grafo)

def definir_caminho_do_grafo_sem_custo(grafo, tipo_de_grafo):
	if tipo_de_grafo == TipoDeGrafo.MODELO_SEM_CUSTO_1:
		for nome, no in grafo.items():
			if nome == "A":
				no.definir_ligacoes_labirinto(grafo["B"], None, None, grafo["E"])
			elif nome == "B":
				no.definir_ligacoes_labirinto(grafo["C"], None, grafo["A"], grafo["F"])
			elif nome == "C":
				no.definir_ligacoes_labirinto(None, None, grafo["B"], None)
			elif nome == "D":
				no.definir_ligacoes_labirinto(None, None, None, grafo["H"])
			elif nome == "E":
				no.definir_ligacoes_labirinto(None, grafo["A"], None, grafo["I"])
			elif nome == "F":
				no.definir_ligacoes_labirinto(grafo["G"], grafo["B"], None, None)
			elif nome == "G":
				no.definir_ligacoes_labirinto(grafo["H"], None, grafo["F"], grafo["L"])
			elif nome == "H":
				no.definir_ligacoes_labirinto(None, grafo["D"], grafo["G"], None)
			elif nome == "I":
				no.definir_ligacoes_labirinto(grafo["J"], grafo["E"], None, grafo["N"])
			elif nome == "J":
				no.definir_ligacoes_labirinto(None, None, grafo["I"], grafo["O"])
			elif nome == "L":
				no.definir_ligacoes_labirinto(grafo["M"], grafo["G"], None, None)
			elif nome == "M":
				no.definir_ligacoes_labirinto(None, None, grafo["L"], grafo["Q"])
			elif nome == "N":
				no.definir_ligacoes_labirinto(None, grafo["I"], None, None)
			elif nome == "O":
				no.definir_ligacoes_labirinto(grafo["P"], grafo["J"], None, grafo["R"])
			elif nome == "P":
				no.definir_ligacoes_labirinto(grafo["Q"], None, grafo["O"], grafo["S"])
			elif nome == "Q":
				no.definir_ligacoes_labirinto(None, grafo["M"], grafo["P"], None)
			elif nome == "R":
				no.definir_ligacoes_labirinto(None, grafo["O"], None, None)
			elif nome == "S":
				no.definir_ligacoes_labirinto(None, grafo["P"], None, None)

def inicializar_grafo_sem_custo(grafo, tipo_de_grafo):
	if tipo_de_grafo == TipoDeGrafo.MODELO_SEM_CUSTO_1:
		alfabeto = ord("A")
		for i in range(19):
			nome = chr(alfabeto)
			if not(nome == "K"):
				grafo[nome] = NoGrafoLabirinto(nome)
			alfabeto += 1
		definir_caminho_do_grafo(grafo, TipoDeGrafo.MODELO_SEM_CUSTO_1)

def inicializar_pilha_abertos(grafo, pilha_de_abertos):
	no_raiz = arvore_busca_ic_1.ArvoreBusca(grafo["A"].nome, [], 0)
	pilha_de_abertos.append(no_raiz)

def inicializar_fila_abertos(grafo, fila_de_abertos):
	no_raiz = arvore_busca_ic_1.ArvoreBusca(grafo["A"].nome, [], 0)
	fila_de_abertos.insert(0, no_raiz)

class NoGrafo:
	def __init__(self, nome):
		self.nome = nome
		self.lista_de_ligacoes = []

	def definir_ligacao_com_custo(self, ligacao_a_adicionar, custo_do_caminho):
		self.lista_de_ligacoes.append([ligacao_a_adicionar, custo_do_caminho])

def definir_caminho_do_grafo_com_custo(grafo, tipo_de_grafo):
	if tipo_de_grafo == TipoDeGrafo.MODELO_COM_CUSTO_1:
		for nome, no in grafo.items():
			if nome == "A":
				no.definir_ligacao_com_custo(grafo["B"], 9)
				no.definir_ligacao_com_custo(grafo["C"], 5)
				no.definir_ligacao_com_custo(grafo["D"], 13)
			elif nome == "B":
				no.definir_ligacao_com_custo(grafo["A"], 9)
				no.definir_ligacao_com_custo(grafo["D"], 3)
				no.definir_ligacao_com_custo(grafo["E"], 10)
			elif nome == "C":
				no.definir_ligacao_com_custo(grafo["A"], 5)
				no.definir_ligacao_com_custo(grafo["F"], 12)
			elif nome == "D":
				no.definir_ligacao_com_custo(grafo["A"], 13)
				no.definir_ligacao_com_custo(grafo["B"], 3)
				no.definir_ligacao_com_custo(grafo["E"], 6)
				no.definir_ligacao_com_custo(grafo["G"], 14)
			elif nome == "E":
				no.definir_ligacao_com_custo(grafo["B"], 10)
				no.definir_ligacao_com_custo(grafo["D"], 6)
				no.definir_ligacao_com_custo(grafo["G"], 7)
			elif nome == "F":
				no.definir_ligacao_com_custo(grafo["C"], 12)
				no.definir_ligacao_com_custo(grafo["G"], 10)
			elif nome == "G":
				no.definir_ligacao_com_custo(grafo["D"], 14)
				no.definir_ligacao_com_custo(grafo["E"], 7)
				no.definir_ligacao_com_custo(grafo["F"], 10)
	elif tipo_de_grafo == TipoDeGrafo.MODELO_COM_CUSTO_2:
		for nome, no in grafo.items():
			if nome == "A":
				no.definir_ligacao_com_custo(grafo["B"], 8)
				no.definir_ligacao_com_custo(grafo["D"], 16)
				no.definir_ligacao_com_custo(grafo["C"], 3)
			elif nome == "B":
				no.definir_ligacao_com_custo(grafo["A"], 8)
				no.definir_ligacao_com_custo(grafo["D"], 7)
				no.definir_ligacao_com_custo(grafo["E"], 6)
			elif nome == "C":
				no.definir_ligacao_com_custo(grafo["A"], 3)
				no.definir_ligacao_com_custo(grafo["D"], 14)
				no.definir_ligacao_com_custo(grafo["F"], 6)
			elif nome == "D":
				no.definir_ligacao_com_custo(grafo["A"], 16)
				no.definir_ligacao_com_custo(grafo["B"], 7)
				no.definir_ligacao_com_custo(grafo["E"], 5)
				no.definir_ligacao_com_custo(grafo["G"], 10)
				no.definir_ligacao_com_custo(grafo["C"], 14)
				no.definir_ligacao_com_custo(grafo["F"], 6)
			elif nome == "E":
				no.definir_ligacao_com_custo(grafo["B"], 6)
				no.definir_ligacao_com_custo(grafo["D"], 5)
				no.definir_ligacao_com_custo(grafo["G"], 15)
			elif nome == "F":
				no.definir_ligacao_com_custo(grafo["C"], 6)
				no.definir_ligacao_com_custo(grafo["D"], 6)
				no.definir_ligacao_com_custo(grafo["G"], 17)
			elif nome == "G":
				no.definir_ligacao_com_custo(grafo["E"], 15)
				no.definir_ligacao_com_custo(grafo["D"], 10)
				no.definir_ligacao_com_custo(grafo["F"], 17)

def inicializar_grafo_com_custo(grafo, tipo_de_grafo):
	alfabeto = ord("A")
	for i in range(7):
		nome = chr(alfabeto)
		grafo[nome] = NoGrafo(nome)
		alfabeto += 1
	definir_caminho_do_grafo(grafo, tipo_de_grafo)
