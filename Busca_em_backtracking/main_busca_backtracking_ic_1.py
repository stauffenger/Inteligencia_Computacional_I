import sys
# adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import grafo_ic_1
import arvore_busca_ic_1

def busca_backtracking(lista_nos, tipo_de_grafo):
	pilha_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False

	grafo_ic_1.inicializar_pilha_abertos(lista_nos, pilha_de_abertos)
	arvore_busca_backtracking = pilha_de_abertos[0]

	while (not sucesso) and (pilha_de_abertos != []):
		ultimo_indice = (len(pilha_de_abertos)-1)
		no_candidato = pilha_de_abertos[ultimo_indice]
		if no_candidato.expandir_backtracking(lista_nos, lista_de_fechados, pilha_de_abertos):
			if no_candidato.filho_eh_solucao(tipo_de_grafo):
				sucesso = True
				resposta = no_candidato.no_solucao(tipo_de_grafo)
			else:
				no_candidato.adiciona_filhos_na_pilha_de_abertos(pilha_de_abertos, lista_de_fechados)
		else:
			lista_de_fechados.append(pilha_de_abertos.pop())	 

	arvore_busca_backtracking.imprime_arvore(tipo_de_grafo)
	return sucesso, resposta

labirinto = {}
tipo_de_grafo = grafo_ic_1.TipoDeGrafo.MODELO_SEM_CUSTO_1
grafo_ic_1.inicializar_grafo_sem_custo(labirinto, tipo_de_grafo)
sucesso, resposta = busca_backtracking(labirinto, tipo_de_grafo)
print(sucesso, resposta.nome)