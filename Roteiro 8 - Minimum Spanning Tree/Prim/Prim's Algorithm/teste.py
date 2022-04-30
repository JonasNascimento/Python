from grafo_adj_nao_dir import Grafo

g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
#{'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'}
g_p.adicionaAresta('J-C')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-M')
g_p.adicionaAresta('C-T')
g_p.adicionaAresta('M-T')
g_p.adicionaAresta('T-Z')

g_c = Grafo(['J', 'C', 'E', 'P'])
g_c.adicionaAresta('J-C')
g_c.adicionaAresta('J-E')
g_c.adicionaAresta('J-P')
g_c.adicionaAresta('C-E')
g_c.adicionaAresta('C-P')
g_c.adicionaAresta('E-P')


g_l5 = Grafo(['C', 'D'])
g_l5.adicionaAresta('D-C')
g_l5.adicionaAresta('C-C')

#print(g_p.vertices_nao_adjacentes())

#g_p.remove_paralelas()
g_l5.print()
print(g_l5.eh_completo())

#print(g_p.arestas_sobre_vertice('J'))

#print(g_p.eh_completo())


