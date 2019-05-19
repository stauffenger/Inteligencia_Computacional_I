import sys
sys.path.insert(0, "../Estruturas/")
import labirinto_ic_1
import arvore_busca_ic_1

def Busca_profundidade(lista_nos):
	pilha_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False
	arvore_busca_profundidade = []

	labirinto_ic_1.Inicializar_pilha_abertos(lista_nos, pilha_de_abertos, arvore_busca_profundidade)

	while (not sucesso) and (pilha_de_abertos != []):
		no_candidato = pilha_de_abertos.pop()
		lista_de_fechados.append(no_candidato)
		no_candidato.Expandir_profundidade(lista_nos, pilha_de_abertos, lista_de_fechados)
		if no_candidato.Filho_eh_solucao():
			sucesso = True
			resposta = no_candidato.No_solucao()
		else:
			no_candidato.Adiciona_filhos_na_pilha(pilha_de_abertos, lista_de_fechados)
		print(no_candidato.nome),
	print(resposta.nome)
	#arvore_busca_profundidade[0].Imprime_arvore()
	return sucesso, resposta

labirinto = []
labirinto_ic_1.Inicializar_labirinto(labirinto)
sucesso, resposta = Busca_profundidade(labirinto)
print(sucesso, resposta.nome)
