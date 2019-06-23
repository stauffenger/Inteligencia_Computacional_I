espaco = "| "
import grafo_ic_1

class ArvoreBusca:
	def __init__(self, nome, filhos, custo_parcial):
		self.nome = nome
		self.filhos = filhos
		self.custo_parcial = custo_parcial

	def verifica_se_esta_na_lista(self, nome, lista):
		for item in lista:
			if item and item.nome == nome:
				return True
		return False

	def verifica_se_esta_nas_listas(self, nome, fila_de_abertos, lista_de_fechados):
		return self.verifica_se_esta_na_lista(nome, fila_de_abertos) or self.verifica_se_esta_na_lista(nome, lista_de_fechados)

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
				if self.verifica_se_esta_na_lista(no.nome, lista_de_abertos):
					self.expandir_no_ordenado(no, custo, lista_de_abertos, lista_de_fechados)
				else:
					self.expandir_no(no, custo, [], lista_de_fechados)

	def expandir_no_ordenado(self, no_grafo, custo, lista_de_abertos, lista_de_fechados):
		for no_aberto in lista_de_abertos:
			if no_grafo.nome == no_aberto.nome:
				custo_parcial_novo_no = self.custo_parcial + custo
				novo_no = ArvoreBusca(no_grafo.nome, [], custo_parcial_novo_no)
				item_a_ser_fechado = (
						self.mantem_item_de_menor_custo_e_retorna_o_de_maior_custo(
							novo_no, no_aberto, lista_de_abertos)
					)
				lista_de_fechados.append(item_a_ser_fechado)

	def mantem_item_de_menor_custo_e_retorna_o_de_maior_custo(self, novo_no, no_antigo, lista):
		if novo_no.custo_parcial < no_antigo.custo_parcial:
			no_com_maior_custo = lista.remove(no_antigo)
			lista.append(novo_no)
			self.filhos.append(novo_no)
		else:
			no_com_maior_custo = novo_no
			ja_existe = self.verifica_se_esta_na_lista(novo_no.nome, self.filhos)
			if ja_existe == False:
				self.filhos.append(novo_no)
		return no_com_maior_custo

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

	def imprime_arvore(self, tipo_de_grafo, resposta):
		altura_atual = 0
		solucao = self.definir_solucao(tipo_de_grafo)
		if tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_SEM_CUSTO_1:
			self.imprime_no(altura_atual, solucao)
		elif tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_1 or (
				tipo_de_grafo == grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_2):
			self.imprime_no_com_custo(altura_atual, solucao, resposta)

	def imprime_no_com_custo(self, altura_atual, solucao, resposta):
		for i in range(0, altura_atual):
			print(espaco, end = '')
		if self.nome == solucao and self.custo_parcial == resposta.custo_parcial:
			print("|-+" + self.nome + "_[" + str(self.custo_parcial) + "] <-- Resposta")
		else:
			print("|-+" + self.nome + "_[" + str(self.custo_parcial) + "]")
		altura_atual += 1
		for filho in self.filhos:
			filho.imprime_no_com_custo(altura_atual, solucao, resposta)
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