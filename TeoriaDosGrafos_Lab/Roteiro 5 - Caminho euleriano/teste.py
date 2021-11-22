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

g_eule = Grafo(['A', 'B', 'C', 'D','E'])
g_eule.adicionaAresta('A-B')
g_eule.adicionaAresta('A-D')
g_eule.adicionaAresta('B-C')
g_eule.adicionaAresta('B-E')
g_eule.adicionaAresta('C-E')
g_eule.adicionaAresta('E-D')

g_eule2 = Grafo(['A', 'B', 'C', 'D','E','F'])
g_eule2.adicionaAresta('A-B')
g_eule2.adicionaAresta('B-C')
g_eule2.adicionaAresta('C-D')
g_eule2.adicionaAresta('C-E')
g_eule2.adicionaAresta('D-E')
g_eule2.adicionaAresta('C-F')

print(g_eule2.conexo())
g_eule2.print()

print('---------------------------------------------------')
print("pontes:",g_eule2.ha_pontes())



