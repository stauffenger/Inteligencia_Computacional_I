import sys
# adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import grafo_ic_1
import arvore_busca_ic_1

def busca_gulosa(lista_nos, tipo_de_grafo):
	lista_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False

	grafo_ic_1.inicializar_fila_abertos(lista_nos, lista_de_abertos)
	arvore_busca_gulosa = lista_de_abertos[0]

	while not(sucesso) and (lista_de_abertos != []):
		no_candidato = arvore_busca_ic_1.remove_elemento_de_melhor_avaliacao_da_lista(lista_de_abertos, tipo_de_grafo)
		lista_de_fechados.append(no_candidato)
		if no_candidato.eh_solucao(tipo_de_grafo):
			sucesso = True
			resposta = no_candidato
		else:
			no_candidato.expandir_gulosa_e_adiciona_filhos_na_lista_de_abertos(lista_nos, lista_de_abertos, lista_de_fechados, tipo_de_grafo)
		
	arvore_busca_gulosa.imprime_arvore(tipo_de_grafo, resposta)
	return sucesso, resposta

grafo_com_custo_exemplo_1 = {}
tipo_de_grafo = grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_1
grafo_ic_1.inicializar_grafo_com_custo(grafo_com_custo_exemplo_1, tipo_de_grafo)
sucesso, resposta = busca_gulosa(grafo_com_custo_exemplo_1, tipo_de_grafo)
print(sucesso, resposta.nome, resposta.custo_parcial)