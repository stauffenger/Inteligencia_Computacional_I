import sys
# adicionando caminhos no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
sys.path.insert(0, "../Busca_gulosa/")
import grafo_ic_1
import arvore_busca_ic_1
import busca_informada_ic_1

def busca_A_estrela(lista_nos, tipo_de_grafo, tipo_de_busca):
	sucesso, resposta = busca_informada_ic_1.busca_informada(lista_nos, tipo_de_grafo, tipo_de_busca)

	return sucesso, resposta

grafo_com_custo_exemplo_1 = {}
tipo_de_grafo = grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_1
tipo_de_busca = arvore_busca_ic_1.TipoDeBusca.A_ESTRELA
grafo_ic_1.inicializar_grafo_com_custo(grafo_com_custo_exemplo_1, tipo_de_grafo)
sucesso, resposta = busca_A_estrela(grafo_com_custo_exemplo_1, tipo_de_grafo, tipo_de_busca)
print(sucesso, resposta.nome, resposta.custo_parcial)