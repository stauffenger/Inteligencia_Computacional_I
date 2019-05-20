import sys
# Adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import labirinto_ic_1
import arvore_busca_ic_1

def Busca_backtracking(lista_nos):
	pilha_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False

	labirinto_ic_1.Inicializar_pilha_abertos(lista_nos, pilha_de_abertos)
	arvore_busca_backtracking = pilha_de_abertos[0]

	while (not sucesso) and (pilha_de_abertos != []):
		ultimo_indice = (len(pilha_de_abertos)-1)
		no_candidato = pilha_de_abertos[ultimo_indice]
		if no_candidato.Expandir_backtracking(lista_nos, lista_de_fechados, pilha_de_abertos):
			if no_candidato.Filho_eh_solucao():
				sucesso = True
				resposta = no_candidato.No_solucao()
			else:
				no_candidato.Adiciona_filhos_na_pilha(pilha_de_abertos, lista_de_fechados)
		else:
			lista_de_fechados.append(pilha_de_abertos.pop())	 

	arvore_busca_backtracking.Imprime_arvore()
	return sucesso, resposta

labirinto = []
labirinto_ic_1.Inicializar_labirinto(labirinto)
sucesso, resposta = Busca_backtracking(labirinto)
print(sucesso, resposta.nome)