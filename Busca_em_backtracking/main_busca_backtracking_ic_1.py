import sys
sys.path.insert(0, "../Estruturas/")
import labirinto_ic_1
import arvore_busca_ic_1

def Adiciona_item_em_impressao(altura, impressao, no_candidato, lista_auxiliar_impressao):
	lista_auxiliar_impressao.append(no_candidato.nome)
	if altura not in impressao:
		impressao[altura] = lista_auxiliar_impressao
	elif no_candidato.nome not in impressao[altura]:
		impressao[altura].append(no_candidato.nome)

def Imprime_arvore(impressao):
	for linha in impressao:
		for nome in impressao[linha]:
			print(nome)

def Busca_backtracking(lista_nos):
	pilha_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False
	impressao = {}
	lista_auxiliar_impressao = []
	altura = 0
	arvore_busca_backtracking = None

	labirinto_ic_1.Inicializar_pilha_abertos(lista_nos, pilha_de_abertos, arvore_busca_backtracking)

	while (not sucesso) and (pilha_de_abertos != []):
		ultimo_indice = (len(pilha_de_abertos)-1)
		no_candidato = pilha_de_abertos[ultimo_indice]
		if no_candidato.Expandir_backtracking(lista_nos, lista_de_fechados, pilha_de_abertos):
			if no_candidato.Filho_eh_solucao():
				sucesso = True
				resposta = no_candidato.No_solucao()
			else:
				no_candidato.Adiciona_filhos_na_pilha(pilha_de_abertos, lista_de_fechados)
				altura += 1
				Adiciona_item_em_impressao(altura, impressao, no_candidato, lista_auxiliar_impressao)
				lista_auxiliar_impressao = []
		else:
			lista_de_fechados.append(pilha_de_abertos.pop())	
			altura -= 1 

	Imprime_arvore(impressao)
	print(resposta.nome)
	#arvore_busca_backtracking[0].Imprime_arvore()
	return sucesso, resposta

labirinto = []
labirinto_ic_1.Inicializar_labirinto(labirinto)
sucesso, resposta = Busca_backtracking(labirinto)
print(sucesso, resposta.nome)
