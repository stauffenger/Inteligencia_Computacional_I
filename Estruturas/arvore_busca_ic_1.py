espaco = "-"
from itertools import zip_longest
class Arvore_busca:
	def __init__(self, nome, filhos):
		self.nome = nome
		self.filhos = filhos

	def Verifica_se_esta_nas_listas(self, nome, fila_de_abertos, lista_de_fechados):
		for item_aberto, item_fechado in zip_longest(fila_de_abertos, lista_de_fechados):
			if item_aberto and nome == item_aberto.nome:
				return True
			elif item_fechado and nome == item_fechado.nome:
				return True
		return False

	def Encontra_caminho_no_labirinto(self, labirinto):
		indice_caminho = None
		for caminho in labirinto:
			if caminho.nome == self.nome:
				indice_caminho = labirinto.index(caminho)
		
		caminho = labirinto[indice_caminho]
		return caminho

	def Expandir_no(self, caminho, pilha_de_abertos, lista_de_fechados):
		if caminho is not None:
			nome = caminho.nome
			ja_existe = self.Verifica_se_esta_nas_listas(nome, pilha_de_abertos, lista_de_fechados)
			if ja_existe == False:
				self.filhos.append(Arvore_busca(nome, []))
				return True
		return False

	def Expandir_backtracking(self, labirinto, lista_de_fechados, pilha_de_abertos):
		caminho = self.Encontra_caminho_no_labirinto(labirinto)

		if self.Expandir_no(caminho.baixo, pilha_de_abertos, lista_de_fechados):
			return True
		if self.Expandir_no(caminho.esquerda, pilha_de_abertos, lista_de_fechados):
			return True
		if self.Expandir_no(caminho.cima, pilha_de_abertos, lista_de_fechados):
			return True
		if self.Expandir_no(caminho.direita, pilha_de_abertos, lista_de_fechados):
			return True
		return False

	def Expandir_profundidade(self, labirinto, pilha_de_abertos, lista_de_fechados):
		caminho = self.Encontra_caminho_no_labirinto(labirinto)

		if self.filhos == []:
			self.Expandir_no(caminho.direita, pilha_de_abertos, lista_de_fechados)
			self.Expandir_no(caminho.cima, pilha_de_abertos, lista_de_fechados)
			self.Expandir_no(caminho.esquerda, pilha_de_abertos, lista_de_fechados)
			self.Expandir_no(caminho.baixo, pilha_de_abertos, lista_de_fechados)

	def Expandir_largura(self, labirinto, fila_de_abertos, lista_de_fechados):
		self.Expandir_profundidade(labirinto, fila_de_abertos, lista_de_fechados)	

	def Filho_eh_solucao(self):
		for filho in self.filhos:
			if filho.nome == "S":
				return True
		return False

	def No_solucao(self):
		for filho in self.filhos:
			if filho.nome == "S":
				return filho

	def Adiciona_filhos_na_fila(self, fila_de_abertos, lista_de_fechados):
		ultimo_indice = (len(self.filhos) - 1)
		if ultimo_indice >= 0:
			for indice in range(ultimo_indice, -1, -1):
				filho = self.filhos[indice] 
				nome = filho.nome
				ja_existe = self.Verifica_se_esta_nas_listas(nome, fila_de_abertos, lista_de_fechados)
				if ja_existe == False:
					fila_de_abertos.append(filho)

	def Adiciona_filhos_na_pilha(self, pilha_de_abertos, lista_de_fechados):
		for filho in self.filhos:
			nome = filho.nome
			ja_existe = self.Verifica_se_esta_nas_listas(nome, pilha_de_abertos, lista_de_fechados)
			if ja_existe == False:
				pilha_de_abertos.append(filho)

	def Imprime_arvore(self):
		altura_atual = 0
		self.Imprime_no(altura_atual)

	def Imprime_no(self, pilha_arvore, altura_atual):
		for i in range(0, altura_atual):
			print(espaco, end = '')
		print(self.nome)
		altura_atual += 1
		for filho in self.filhos:
			filho.Imprime_no(altura_atual)
		altura_atual -= 1