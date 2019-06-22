import sys
# adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import grafo_ic_1
import arvore_busca_ic_1

def busca_largura(lista_nos, tipo_de_grafo):
	fila_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False

	grafo_ic_1.inicializar_fila_abertos(lista_nos, fila_de_abertos)
	arvore_busca_largura = fila_de_abertos[0]

	while (sucesso == False) and (fila_de_abertos != []):
		no_candidato = fila_de_abertos.pop(0)
		lista_de_fechados.append(no_candidato)
		no_candidato.expandir_largura(lista_nos, fila_de_abertos, lista_de_fechados)
		if no_candidato.filho_eh_solucao(tipo_de_grafo):
			sucesso = True
			resposta = no_candidato.no_solucao(tipo_de_grafo)
		else:
			no_candidato.adiciona_filhos_na_fila_de_abertos(fila_de_abertos, lista_de_fechados)

	arvore_busca_largura.imprime_arvore(tipo_de_grafo)
	return sucesso, resposta

labirinto = {}
tipo_de_grafo = grafo_ic_1.TipoDeGrafo.MODELO_SEM_CUSTO_1
grafo_ic_1.inicializar_grafo_sem_custo(labirinto, tipo_de_grafo)
sucesso, resposta = busca_largura(labirinto, tipo_de_grafo)
print(sucesso, resposta.nome)