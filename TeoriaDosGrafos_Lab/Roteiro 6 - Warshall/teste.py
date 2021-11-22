from grafo_adj_dir import Grafo

'''g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
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
g_c.adicionaAresta('E-P')'''

g_a = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
g_a.adicionaAresta('A-B')
g_a.adicionaAresta('A-H')
g_a.adicionaAresta('B-C')
g_a.adicionaAresta('C-A')
g_a.adicionaAresta('C-D')
g_a.adicionaAresta('D-E')
g_a.adicionaAresta('E-F')
g_a.adicionaAresta('E-G')

g_a.print()

matriz =g_a.warshall()
print('---------------------------------------------------------------------------------------')

print('+',end= ' ')
for i in g_a.N:
    print(i, end = ' ')
print()
for x in range(len(matriz)):
    print(g_a.N[x], end=' ')
    for y in matriz[x]:
        print(y, end=' ')
    print()


