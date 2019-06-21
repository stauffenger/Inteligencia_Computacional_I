import sys
# adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import labirinto_ic_1
import arvore_busca_ic_1

def busca_profundidade(lista_nos):
	pilha_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False

	labirinto_ic_1.inicializar_pilha_abertos_sem_custo(lista_nos, pilha_de_abertos)
	arvore_busca_profundidade = pilha_de_abertos[0]

	while (not sucesso) and (pilha_de_abertos != []):
		no_candidato = pilha_de_abertos.pop()
		lista_de_fechados.append(no_candidato)
		no_candidato.expandir_profundidade(lista_nos, pilha_de_abertos, lista_de_fechados)
		if no_candidato.filho_eh_solucao():
			sucesso = True
			resposta = no_candidato.no_solucao()
		else:
			no_candidato.adiciona_filhos_na_pilha(pilha_de_abertos, lista_de_fechados)

	arvore_busca_profundidade.imprime_arvore()
	return sucesso, resposta

labirinto = {}
labirinto_ic_1.inicializar_labirinto_sem_custo(labirinto)
sucesso, resposta = busca_profundidade(labirinto)
print(sucesso, resposta.nome)