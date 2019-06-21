import arvore_busca_ic_1
from enum import Enum

class TipoDeLabirinto(Enum):
	MODELO_SEM_CUSTO_1 = 0
	MODELO_COM_CUSTO_1 = 1
	MODELO_COM_CUSTO_2 = 2

class Caminho:
	def __init__(self, nome):
		self.nome = nome
		self.baixo = None	
		self.esquerda = None
		self.cima = None
		self.direita = None

	def definir_ligacoes_sem_custo(self, baixo, esquerda, cima, direita):
		self.baixo = baixo	
		self.esquerda = esquerda
		self.cima = cima
		self.direita = direita

def definir_caminho_do_labirinto(labirinto, tipo_de_labirinto):
	if tipo_de_labirinto == TipoDeLabirinto.MODELO_SEM_CUSTO_1:
		definir_caminho_do_labirinto_sem_custo(labirinto, tipo_de_labirinto)
	elif tipo_de_labirinto == TipoDeLabirinto.MODELO_COM_CUSTO_1 or tipo_de_labirinto == TipoDeLabirinto.MODELO_COM_CUSTO_2:
		definir_caminho_do_labirinto_com_custo(labirinto, tipo_de_labirinto)

def definir_caminho_do_labirinto_sem_custo(labirinto, tipo_de_labirinto):
	if tipo_de_labirinto == TipoDeLabirinto.MODELO_SEM_CUSTO_1:
		for nome, no in labirinto.items():
			if nome == "A":
				no.definir_ligacoes_sem_custo(labirinto["B"], None, None, labirinto["E"])
			elif nome == "B":
				no.definir_ligacoes_sem_custo(labirinto["C"], None, labirinto["A"], labirinto["F"])
			elif nome == "C":
				no.definir_ligacoes_sem_custo(None, None, labirinto["B"], None)
			elif nome == "D":
				no.definir_ligacoes_sem_custo(None, None, None, labirinto["H"])
			elif nome == "E":
				no.definir_ligacoes_sem_custo(None, labirinto["A"], None, labirinto["I"])
			elif nome == "F":
				no.definir_ligacoes_sem_custo(labirinto["G"], labirinto["B"], None, None)
			elif nome == "G":
				no.definir_ligacoes_sem_custo(labirinto["H"], None, labirinto["F"], labirinto["L"])
			elif nome == "H":
				no.definir_ligacoes_sem_custo(None, labirinto["D"], labirinto["G"], None)
			elif nome == "I":
				no.definir_ligacoes_sem_custo(labirinto["J"], labirinto["E"], None, labirinto["N"])
			elif nome == "J":
				no.definir_ligacoes_sem_custo(None, None, labirinto["I"], labirinto["O"])
			elif nome == "L":
				no.definir_ligacoes_sem_custo(labirinto["M"], labirinto["G"], None, None)
			elif nome == "M":
				no.definir_ligacoes_sem_custo(None, None, labirinto["L"], labirinto["Q"])
			elif nome == "N":
				no.definir_ligacoes_sem_custo(None, labirinto["I"], None, None)
			elif nome == "O":
				no.definir_ligacoes_sem_custo(labirinto["P"], labirinto["J"], None, labirinto["R"])
			elif nome == "P":
				no.definir_ligacoes_sem_custo(labirinto["Q"], None, labirinto["O"], labirinto["S"])
			elif nome == "Q":
				no.definir_ligacoes_sem_custo(None, labirinto["M"], labirinto["P"], None)
			elif nome == "R":
				no.definir_ligacoes_sem_custo(None, labirinto["O"], None, None)
			elif nome == "S":
				no.definir_ligacoes_sem_custo(None, labirinto["P"], None, None)

def inicializar_labirinto_sem_custo(labirinto):
	alfabeto = ord("A")
	for i in range(19):
		nome = chr(alfabeto)
		if not(nome == "K"):
			labirinto[nome] = Caminho(nome)
		alfabeto += 1
	definir_caminho_do_labirinto(labirinto, TipoDeLabirinto.MODELO_SEM_CUSTO_1)

def inicializar_pilha_abertos_sem_custo(labirinto, pilha_de_abertos):
	no_raiz = arvore_busca_ic_1.ArvoreBusca(labirinto["A"].nome, [], None)
	pilha_de_abertos.append(no_raiz)

def inicializar_fila_abertos_sem_custo(labirinto, fila_de_abertos):
	no_raiz = arvore_busca_ic_1.ArvoreBusca(labirinto["A"].nome, [], None)
	fila_de_abertos.insert(0, no_raiz)

class CaminhoComCusto:
	def __init__(self, nome):
		self.nome = nome
		self.lista_de_ligacoes = []

	def definir_ligacao_com_custo(self, ligacao_a_adicionar, custo_do_caminho):
		self.lista_de_ligacoes.extend([ligacao_a_adicionar, custo_do_caminho])

def definir_caminho_do_labirinto_com_custo(labirinto, tipo_de_labirinto):
	if tipo_de_labirinto == TipoDeLabirinto.MODELO_COM_CUSTO_1:
		for nome, no in labirinto.items():
			if nome == "A":
				no.definir_ligacao_com_custo(labirinto["B"], 9)
				no.definir_ligacao_com_custo(labirinto["D"], 13)
				no.definir_ligacao_com_custo(labirinto["C"], 5)
			elif nome == "B":
				no.definir_ligacao_com_custo(labirinto["A"], 9)
				no.definir_ligacao_com_custo(labirinto["D"], 3)
				no.definir_ligacao_com_custo(labirinto["E"], 10)
			elif nome == "C":
				no.definir_ligacao_com_custo(labirinto["A"], 5)
				no.definir_ligacao_com_custo(labirinto["F"], 12)
			elif nome == "D":
				no.definir_ligacao_com_custo(labirinto["A"], 13)
				no.definir_ligacao_com_custo(labirinto["B"], 3)
				no.definir_ligacao_com_custo(labirinto["E"], 6)
				no.definir_ligacao_com_custo(labirinto["G"], 14)
			elif nome == "E":
				no.definir_ligacao_com_custo(labirinto["B"], 10)
				no.definir_ligacao_com_custo(labirinto["D"], 6)
				no.definir_ligacao_com_custo(labirinto["G"], 7)
			elif nome == "F":
				no.definir_ligacao_com_custo(labirinto["C"], 12)
				no.definir_ligacao_com_custo(labirinto["G"], 10)
			elif nome == "G":
				no.definir_ligacao_com_custo(labirinto["E"], 7)
				no.definir_ligacao_com_custo(labirinto["D"], 14)
				no.definir_ligacao_com_custo(labirinto["F"], 10)
	elif tipo_de_labirinto == TipoDeLabirinto.MODELO_COM_CUSTO_2:
		for nome, no in labirinto.items():
			if nome == "A":
				no.definir_ligacao_com_custo(labirinto["B"], 8)
				no.definir_ligacao_com_custo(labirinto["D"], 16)
				no.definir_ligacao_com_custo(labirinto["C"], 3)
			elif nome == "B":
				no.definir_ligacao_com_custo(labirinto["A"], 8)
				no.definir_ligacao_com_custo(labirinto["D"], 7)
				no.definir_ligacao_com_custo(labirinto["E"], 6)
			elif nome == "C":
				no.definir_ligacao_com_custo(labirinto["A"], 3)
				no.definir_ligacao_com_custo(labirinto["D"], 14)
				no.definir_ligacao_com_custo(labirinto["F"], 6)
			elif nome == "D":
				no.definir_ligacao_com_custo(labirinto["A"], 16)
				no.definir_ligacao_com_custo(labirinto["B"], 7)
				no.definir_ligacao_com_custo(labirinto["E"], 5)
				no.definir_ligacao_com_custo(labirinto["G"], 10)
				no.definir_ligacao_com_custo(labirinto["C"], 14)
				no.definir_ligacao_com_custo(labirinto["F"], 6)
			elif nome == "E":
				no.definir_ligacao_com_custo(labirinto["B"], 6)
				no.definir_ligacao_com_custo(labirinto["D"], 5)
				no.definir_ligacao_com_custo(labirinto["G"], 15)
			elif nome == "F":
				no.definir_ligacao_com_custo(labirinto["C"], 6)
				no.definir_ligacao_com_custo(labirinto["D"], 6)
				no.definir_ligacao_com_custo(labirinto["G"], 17)
			elif nome == "G":
				no.definir_ligacao_com_custo(labirinto["E"], 15)
				no.definir_ligacao_com_custo(labirinto["D"], 10)
				no.definir_ligacao_com_custo(labirinto["F"], 17)

def inicializar_labirinto_com_custo(labirinto):
	alfabeto = ord("A")
	for i in range(7):
		nome = chr(alfabeto)
		labirinto[nome] = CaminhoComCusto(nome)
		alfabeto += 1
	definir_caminho_do_labirinto(labirinto, TipoDeLabirinto.MODELO_COM_CUSTO_1)
