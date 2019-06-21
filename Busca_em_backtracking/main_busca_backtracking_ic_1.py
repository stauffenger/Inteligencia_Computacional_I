import sys
# adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import labirinto_ic_1
import arvore_busca_ic_1

def busca_backtracking(lista_nos):
	pilha_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False

	labirinto_ic_1.inicializar_pilha_abertos_sem_custo(lista_nos, pilha_de_abertos)
	arvore_busca_backtracking = pilha_de_abertos[0]

	while (not sucesso) and (pilha_de_abertos != []):
		ultimo_indice = (len(pilha_de_abertos)-1)
		no_candidato = pilha_de_abertos[ultimo_indice]
		if no_candidato.expandir_backtracking(lista_nos, lista_de_fechados, pilha_de_abertos):
			if no_candidato.filho_eh_solucao():
				sucesso = True
				resposta = no_candidato.no_solucao()
			else:
				no_candidato.adiciona_filhos_na_pilha(pilha_de_abertos, lista_de_fechados)
		else:
			lista_de_fechados.append(pilha_de_abertos.pop())	 

	arvore_busca_backtracking.imprime_arvore()
	return sucesso, resposta

labirinto = {}
labirinto_ic_1.inicializar_labirinto_sem_custo(labirinto)
sucesso, resposta = busca_backtracking(labirinto)
print(sucesso, resposta.nome)