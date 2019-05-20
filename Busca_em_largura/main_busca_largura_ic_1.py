import sys
sys.path.insert(0, "../Estruturas/")
import labirinto_ic_1
import arvore_busca_ic_1

def Busca_largura(lista_nos):
	fila_de_abertos = []
	resposta = None
	lista_de_fechados = []
	sucesso = False
	arvore_busca_largura = None

	labirinto_ic_1.Inicializar_fila_abertos(lista_nos, fila_de_abertos)
	arvore_busca_largura = fila_de_abertos[0]

	while (sucesso == False) and (fila_de_abertos != []):
		no_candidato = fila_de_abertos.pop(0)
		lista_de_fechados.append(no_candidato)
		no_candidato.Expandir_largura(lista_nos, fila_de_abertos, lista_de_fechados)
		if no_candidato.Filho_eh_solucao():
			sucesso = True
			resposta = no_candidato.No_solucao()
		else:
			no_candidato.Adiciona_filhos_na_fila(fila_de_abertos, lista_de_fechados)

	arvore_busca_largura.Imprime_arvore()
	return sucesso, resposta

labirinto = []
labirinto_ic_1.Inicializar_labirinto(labirinto)
sucesso, resposta = Busca_largura(labirinto)
print(sucesso, resposta.nome)