import sys
# adicionando o caminho no sistema de busca por módulos
sys.path.insert(0, "../Estruturas/")
import grafo_ic_1
import arvore_busca_ic_1
import busca_informada_ic_1

grafo_com_custo_exemplo_1 = {}
tipo_de_grafo = grafo_ic_1.TipoDeGrafo.MODELO_COM_CUSTO_1
tipo_de_busca = arvore_busca_ic_1.TipoDeBusca.GULOSA
grafo_ic_1.inicializar_grafo_com_custo(grafo_com_custo_exemplo_1, tipo_de_grafo)
sucesso, resposta = busca_informada_ic_1.busca_informada(grafo_com_custo_exemplo_1, tipo_de_grafo, tipo_de_busca)
print(sucesso, resposta.nome, resposta.custo_parcial)