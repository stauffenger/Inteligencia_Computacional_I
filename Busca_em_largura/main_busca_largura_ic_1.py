import sys
# adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import labirinto_ic_1
import arvore_busca_ic_1

def busca_largura(lista_nos):
	fila_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False

	labirinto_ic_1.inicializar_fila_abertos_sem_custo(lista_nos, fila_de_abertos)
	arvore_busca_largura = fila_de_abertos[0]

	while (sucesso == False) and (fila_de_abertos != []):
		no_candidato = fila_de_abertos.pop(0)
		lista_de_fechados.append(no_candidato)
		no_candidato.expandir_largura(lista_nos, fila_de_abertos, lista_de_fechados)
		if no_candidato.filho_eh_solucao():
			sucesso = True
			resposta = no_candidato.no_solucao()
		else:
			no_candidato.adiciona_filhos_na_fila(fila_de_abertos, lista_de_fechados)

	arvore_busca_largura.imprime_arvore()
	return sucesso, resposta

labirinto = []
labirinto_ic_1.inicializar_labirinto_sem_custo(labirinto)
sucesso, resposta = busca_largura(labirinto)
print(sucesso, resposta.nome)