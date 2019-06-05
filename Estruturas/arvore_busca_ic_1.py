espaco = "| "
from itertools import zip_longest

class ArvoreBusca:
	def __init__(self, nome, filhos, custo_parcial):
		self.nome = nome
		self.filhos = filhos
		self.custo_parcial = custo_parcial

	def verifica_se_esta_nas_listas(self, nome, fila_de_abertos, lista_de_fechados):
		for item_aberto, item_fechado in zip_longest(fila_de_abertos, lista_de_fechados):
			if item_aberto and nome == item_aberto.nome:
				return True
			if item_fechado and nome == item_fechado.nome:
				return True
		return False

	def encontra_caminho_no_labirinto(self, labirinto):
		indice_caminho = None
		for caminho in labirinto:
			if caminho.nome == self.nome:
				indice_caminho = labirinto.index(caminho)
		
		caminho = labirinto[indice_caminho]
		return caminho

	def expandir_no(self, caminho, pilha_de_abertos, lista_de_fechados):
		if caminho != []:
			nome = caminho[0].nome
			ja_existe = self.verifica_se_esta_nas_listas(nome, pilha_de_abertos, lista_de_fechados)
			if ja_existe == False:
				self.filhos.append(ArvoreBusca(nome, [], None))
				return True
		return False

	def expandir_backtracking(self, labirinto, lista_de_fechados, pilha_de_abertos):
		caminho = self.encontra_caminho_no_labirinto(labirinto)

		if self.expandir_no(caminho.baixo, pilha_de_abertos, lista_de_fechados):
			return True
		if self.expandir_no(caminho.esquerda, pilha_de_abertos, lista_de_fechados):
			return True
		if self.expandir_no(caminho.cima, pilha_de_abertos, lista_de_fechados):
			return True
		if self.expandir_no(caminho.direita, pilha_de_abertos, lista_de_fechados):
			return True
		return False

	def expandir_profundidade(self, labirinto, pilha_de_abertos, lista_de_fechados):
		caminho = self.encontra_caminho_no_labirinto(labirinto)

		if self.filhos == []:
			self.expandir_no(caminho.direita, pilha_de_abertos, lista_de_fechados)
			self.expandir_no(caminho.cima, pilha_de_abertos, lista_de_fechados)
			self.expandir_no(caminho.esquerda, pilha_de_abertos, lista_de_fechados)
			self.expandir_no(caminho.baixo, pilha_de_abertos, lista_de_fechados)

	def expandir_largura(self, labirinto, fila_de_abertos, lista_de_fechados):
		self.expandir_profundidade(labirinto, fila_de_abertos, lista_de_fechados)	

	def filho_eh_solucao(self):
		for filho in self.filhos:
			if filho.nome == "S":
				return True
		return False

	def no_solucao(self):
		for filho in self.filhos:
			if filho.nome == "S":
				return filho

	def adiciona_filhos_na_fila(self, fila_de_abertos, lista_de_fechados):
		ultimo_indice = (len(self.filhos) - 1)
		if ultimo_indice >= 0:
			for indice in range(ultimo_indice, -1, -1):
				filho = self.filhos[indice] 
				nome = filho.nome
				ja_existe = self.verifica_se_esta_nas_listas(nome, fila_de_abertos, lista_de_fechados)
				if ja_existe == False:
					fila_de_abertos.append(filho)

	def adiciona_filhos_na_pilha(self, pilha_de_abertos, lista_de_fechados):
		for filho in self.filhos:
			nome = filho.nome
			ja_existe = self.verifica_se_esta_nas_listas(nome, pilha_de_abertos, lista_de_fechados)
			if ja_existe == False:
				pilha_de_abertos.append(filho)

	def imprime_arvore(self):
		altura_atual = 0
		self.imprime_no(altura_atual)

	def imprime_no(self, altura_atual):
		for i in range(0, altura_atual):
			print(espaco, end = '')
		if self.nome == "S":
			print("|-+" + self.nome + " <-- Solução")
		else:
			print("|-+" + self.nome)
		altura_atual += 1
		for filho in self.filhos:
			filho.imprime_no(altura_atual)
		altura_atual -= 1