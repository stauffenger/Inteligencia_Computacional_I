espaco = "| "
import grafo_ic_1
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

	def expandir_no(self, no_grafo, custo, pilha_de_abertos, lista_de_fechados):
		if no_grafo is not None:
			nome = no_grafo.nome
			ja_existe = self.verifica_se_esta_nas_listas(nome, pilha_de_abertos, lista_de_fechados)
			if ja_existe == False:
				custo_parcial = self.custo_parcial + custo
				self.filhos.append(ArvoreBusca(nome, [], custo_parcial))
				return True
		return False

	def expandir_backtracking(self, labirinto, lista_de_fechados, pilha_de_abertos):
		no_grafo_labirinto = labirinto[self.nome]
		custo = 0

		if self.expandir_no(no_grafo_labirinto.baixo, custo, pilha_de_abertos, lista_de_fechados):
			return True
		if self.expandir_no(no_grafo_labirinto.esquerda, custo, pilha_de_abertos, lista_de_fechados):
			return True
		if self.expandir_no(no_grafo_labirinto.cima, custo, pilha_de_abertos, lista_de_fechados):
			return True
		if self.expandir_no(no_grafo_labirinto.direita, custo, pilha_de_abertos, lista_de_fechados):
			return True
		return False

	def expandir_profundidade(self, labirinto, pilha_de_abertos, lista_de_fechados):
		no_grafo_labirinto = labirinto[self.nome]
		custo = 0

		if self.filhos == []:
			self.expandir_no(no_grafo_labirinto.direita, custo, pilha_de_abertos, lista_de_fechados)
			self.expandir_no(no_grafo_labirinto.cima, custo, pilha_de_abertos, lista_de_fechados)
			self.expandir_no(no_grafo_labirinto.esquerda, custo, pilha_de_abertos, lista_de_fechados)
			self.expandir_no(no_grafo_labirinto.baixo, custo, pilha_de_abertos, lista_de_fechados)

	def expandir_largura(self, labirinto, fila_de_abertos, lista_de_fechados):
		self.expandir_profundidade(labirinto, fila_de_abertos, lista_de_fechados)	

	def expandir_ordenada(self, grafo, lista_de_abertos, lista_de_fechados):
		no_grafo = grafo[self.nome]

		if self.filhos == []:
			for no, custo in no_grafo.lista_de_ligacoes:
				self.expandir_no(no, custo, [], lista_de_fechados)

	def definir_solucao(self, tipo_de_grafo):
		solucao = ""
		if tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_SEM_CUSTO_1:
			solucao = "S"
		elif tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_1 or (
				tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_2):
			solucao = "G"
		return solucao

	def eh_solucao(self, tipo_de_grafo):
		solucao = self.definir_solucao(tipo_de_grafo)

		if self.nome == solucao:
			return True
		return False

	def filho_eh_solucao(self, tipo_de_grafo):
		solucao = self.definir_solucao(tipo_de_grafo)

		for filho in self.filhos:
			if filho.nome == solucao:
				return True
		return False

	def no_solucao(self, tipo_de_grafo):
		solucao = self.definir_solucao(tipo_de_grafo)

		for filho in self.filhos:
			if filho.nome == solucao:
				return filho

	def adiciona_filhos_na_fila_de_abertos(self, fila_de_abertos, lista_de_fechados):
		ultimo_indice = (len(self.filhos) - 1)
		if ultimo_indice >= 0:
			for indice in range(ultimo_indice, -1, -1):
				filho = self.filhos[indice] 
				nome = filho.nome
				ja_existe = self.verifica_se_esta_nas_listas(nome, fila_de_abertos, lista_de_fechados)
				if ja_existe == False:
					fila_de_abertos.append(filho)

	def adiciona_filhos_na_pilha_de_abertos(self, pilha_de_abertos, lista_de_fechados):
		for filho in self.filhos:
			nome = filho.nome
			ja_existe = self.verifica_se_esta_nas_listas(nome, pilha_de_abertos, lista_de_fechados)
			if ja_existe == False:
				pilha_de_abertos.append(filho)

	def imprime_arvore(self, tipo_de_grafo):
		altura_atual = 0
		solucao = self.definir_solucao(tipo_de_grafo)
		if tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_SEM_CUSTO_1:
			self.imprime_no(altura_atual, solucao)
		elif tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_1 or (
				tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_2):
			self.imprime_no_com_custo(altura_atual, solucao)

	def imprime_no_com_custo(self, altura_atual, solucao):
		for i in range(0, altura_atual):
			print(espaco, end = '')
		if self.nome == solucao:
			print("|-+" + self.nome + "-", self.custo_parcial, " <-- Solução")
		else:
			print("|-+" + self.nome + "-", self.custo_parcial)
		altura_atual += 1
		for filho in self.filhos:
			filho.imprime_no_com_custo(altura_atual, solucao)
		altura_atual -= 1

	def imprime_no(self, altura_atual, solucao):
		for i in range(0, altura_atual):
			print(espaco, end = '')
		if self.nome == solucao:
			print("|-+" + self.nome + " <-- Solução")
		else:
			print("|-+" + self.nome)
		altura_atual += 1
		for filho in self.filhos:
			filho.imprime_no(altura_atual, solucao)
		altura_atual -= 1

def remove_elemento_de_menor_custo_da_lista(lista):
		if lista != []:
			elemento_de_menor_custo = lista[0]
			for elemento in lista:
				if elemento.custo_parcial <= elemento_de_menor_custo.custo_parcial:
					elemento_de_menor_custo = elemento
			lista.remove(elemento_de_menor_custo)
			return elemento_de_menor_custo