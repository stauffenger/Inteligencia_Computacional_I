tabulacao = "."
class Arvore_busca:
	def __init__(self, nome, filhos):
		self.nome = nome
		self.filhos = filhos

	def Expandir_backtracking(self, labirinto, lista_de_fechados, pilha_de_abertos):
		indice_caminho = None
		for caminho in labirinto:
			if caminho.nome == self.nome:
				indice_caminho = labirinto.index(caminho)
		
		caminho = labirinto[indice_caminho]

		if caminho.baixo is not None:
			ja_existe = False
			for item in pilha_de_abertos:
				if caminho.baixo.nome == item.nome:
					ja_existe = True
			for item in lista_de_fechados:
				if caminho.baixo.nome == item.nome:
					ja_existe = True
			if ja_existe == False:
				self.filhos.append(Arvore_busca(caminho.baixo.nome, []))
				return True
		if caminho.esquerda is not None:
			ja_existe = False
			for item in pilha_de_abertos:
				if caminho.esquerda.nome == item.nome:
					ja_existe = True
			for item in lista_de_fechados:
				if caminho.esquerda.nome == item.nome:
					ja_existe = True
			if ja_existe == False:
				self.filhos.append(Arvore_busca(caminho.esquerda.nome, []))
				return True
		if caminho.cima is not None:
			ja_existe = False
			for item in pilha_de_abertos:
				if caminho.cima.nome == item.nome:
					ja_existe = True
			for item in lista_de_fechados:
				if caminho.cima.nome == item.nome:
					ja_existe = True
			if ja_existe == False:
				self.filhos.append(Arvore_busca(caminho.cima.nome, []))
				return True
		if caminho.direita is not None:
			ja_existe = False
			for item in pilha_de_abertos:
				if caminho.direita.nome == item.nome:
					ja_existe = True
			for item in lista_de_fechados:
				if caminho.direita.nome == item.nome:
					ja_existe = True
			if ja_existe == False:
				self.filhos.append(Arvore_busca(caminho.direita.nome, []))
				return True
		return False

	def Expandir_profundidade(self, labirinto, pilha_de_abertos, lista_de_fechados):
		indice_caminho = None
		for caminho in labirinto:
			if caminho.nome == self.nome:
				indice_caminho = labirinto.index(caminho)
		
		caminho = labirinto[indice_caminho]
		nome = None
		if self.filhos == []:
			if caminho.direita is not None:
				nome = caminho.direita.nome
				ja_existe = False
				for item in pilha_de_abertos:
					if nome == item.nome:
						ja_existe = True
				for item in lista_de_fechados:
					if nome == item.nome:
						ja_existe = True
				if ja_existe == False:
					self.filhos.append(Arvore_busca(nome, []))
			if caminho.cima is not None:
				nome = caminho.cima.nome
				ja_existe = False
				for item in pilha_de_abertos:
					if nome == item.nome:
						ja_existe = True
				for item in lista_de_fechados:
					if nome == item.nome:
						ja_existe = True
				if ja_existe == False:
					self.filhos.append(Arvore_busca(nome, []))
			if caminho.esquerda is not None:
				nome = caminho.esquerda.nome
				ja_existe = False
				for item in pilha_de_abertos:
					if nome == item.nome:
						ja_existe = True
				for item in lista_de_fechados:
					if nome == item.nome:
						ja_existe = True
				if ja_existe == False:
					self.filhos.append(Arvore_busca(nome, []))
			if caminho.baixo is not None:
				nome = caminho.baixo.nome
				ja_existe = False
				for item in pilha_de_abertos:
					if nome == item.nome:
						ja_existe = True
				for item in lista_de_fechados:
					if nome == item.nome:
						ja_existe = True
				if ja_existe == False:
					self.filhos.append(Arvore_busca(nome, []))

	def Filho_eh_solucao(self):
		for filho in self.filhos:
			if filho.nome == "S":
				return True
		return False

	def No_solucao(self):
		for filho in self.filhos:
			if filho.nome == "S":
				return filho

	def Adiciona_filhos_na_pilha(self, pilha_de_abertos, lista_de_fechados):
		for filho in self.filhos:
			ja_existe = False
			for item in pilha_de_abertos:
				if filho.nome == item.nome:
					ja_existe = True
			for item in lista_de_fechados:
				if filho.nome == item.nome:
					ja_existe = True
			if ja_existe == False:
				pilha_de_abertos.append(filho)

	def Imprime_arvore(self):
		altura_atual = 1
		altura_maxima = altura_atual
		numero_filhos = 0
		numero_maximo_filhos = 0
		altura_atual, altura_maxima, numero_maximo_filhos = self.Calcula_altura(altura_atual, altura_maxima, numero_maximo_filhos)
		altura_atual = 1
		quantidade_folhas = 1
		pilha_arvore = {}
		for altura in range(1, altura_maxima+2):
			pilha_arvore[altura] = ""
		self.Imprime_no(pilha_arvore, altura_atual, altura_maxima, numero_filhos, numero_maximo_filhos, quantidade_folhas)
		for altura, conteudo in pilha_arvore.items():
			print(conteudo)

	def Imprime_no(self, pilha_arvore, altura_atual, altura_maxima, numero_filhos, numero_maximo_filhos, quantidade_folhas):
		numero_filhos = len(self.filhos)
		for i in range(1, (altura_maxima-altura_atual+1)*numero_maximo_filhos*(quantidade_folhas*(numero_maximo_filhos*numero_maximo_filhos))):
			pilha_arvore[altura_atual] += tabulacao
		if numero_filhos == 0:
			quantidade_folhas += 1
		pilha_arvore[altura_atual] += self.nome + str(quantidade_folhas)
		altura_atual += 1
		for filho in self.filhos:
			quantidade_folhas = filho.Imprime_no(pilha_arvore, altura_atual, altura_maxima, numero_filhos, numero_maximo_filhos, quantidade_folhas)
		"""if numero_filhos < numero_maximo_filhos:
			for i in range(1, numero_maximo_filhos-numero_filhos):
				for j in range(1, (altura_maxima-altura_atual+1)*numero_maximo_filhos*(quantidade_folhas*(numero_maximo_filhos*numero_maximo_filhos))):
					pilha_arvore[altura_atual] += tabulacao"""
		altura_atual -= 1
		return quantidade_folhas

	def Calcula_altura(self, altura_atual, altura_maxima, numero_maximo_filhos):
		numero_filhos = len(self.filhos)
		if numero_filhos > numero_maximo_filhos:
			numero_maximo_filhos = numero_filhos

		if altura_atual > altura_maxima:
			altura_maxima = altura_atual
		altura_atual += 1

		for filho in self.filhos:
			altura_atual, altura_maxima, numero_maximo_filhos = filho.Calcula_altura(altura_atual, altura_maxima, numero_maximo_filhos)
		altura_atual -= 1
		return altura_atual, altura_maxima, numero_maximo_filhos