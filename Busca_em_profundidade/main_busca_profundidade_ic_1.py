import sys
# adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import grafo_ic_1
import arvore_busca_ic_1

def busca_profundidade(lista_nos, tipo_de_grafo):
	pilha_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False

	grafo_ic_1.inicializar_pilha_abertos(lista_nos, pilha_de_abertos)
	arvore_busca_profundidade = pilha_de_abertos[0]

	while (not sucesso) and (pilha_de_abertos != []):
		no_candidato = pilha_de_abertos.pop()
		lista_de_fechados.append(no_candidato)
		no_candidato.expandir_profundidade(lista_nos, pilha_de_abertos, lista_de_fechados)
		if no_candidato.filho_eh_solucao(tipo_de_grafo):
			sucesso = True
			resposta = no_candidato.no_solucao(tipo_de_grafo)
		else:
			no_candidato.adiciona_filhos_na_pilha_de_abertos(pilha_de_abertos, lista_de_fechados)

	arvore_busca_profundidade.imprime_arvore(tipo_de_grafo, resposta)
	return sucesso, resposta

labirinto = {}
tipo_de_grafo = grafo_ic_1.TipoDeGrafo.MODELO_SEM_CUSTO_1
grafo_ic_1.inicializar_grafo_sem_custo(labirinto, tipo_de_grafo)
sucesso, resposta = busca_profundidade(labirinto, tipo_de_grafo)
print(sucesso, resposta.nome)