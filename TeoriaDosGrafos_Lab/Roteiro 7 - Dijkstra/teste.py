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

g_d = Grafo(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A1','B1','C1','D1','E1','F1','CJ'])

g_d.adicionaAresta('A-B')
g_d.adicionaAresta('A-C')
g_d.adicionaAresta('A-D')
g_d.adicionaAresta('B-E')
g_d.adicionaAresta('B-I')
g_d.adicionaAresta('C-G')
g_d.adicionaAresta('D-C')
g_d.adicionaAresta('D-H')
g_d.adicionaAresta('E-F')
g_d.adicionaAresta('F-J')
g_d.adicionaAresta('F-B')
g_d.adicionaAresta('G-F')
g_d.adicionaAresta('G-J')
g_d.adicionaAresta('G-K')
g_d.adicionaAresta('H-G')
g_d.adicionaAresta('H-L')
g_d.adicionaAresta('I-M')
g_d.adicionaAresta('J-I')
g_d.adicionaAresta('J-N')
g_d.adicionaAresta('K-O')
g_d.adicionaAresta('L-P')
g_d.adicionaAresta('M-Q')
g_d.adicionaAresta('M-S')
g_d.adicionaAresta('N-R')
g_d.adicionaAresta('N-S')
g_d.adicionaAresta('N-T')
g_d.adicionaAresta('O-S')
g_d.adicionaAresta('P-T')
g_d.adicionaAresta('Q-U')
g_d.adicionaAresta('R-V')
g_d.adicionaAresta('S-R')
g_d.adicionaAresta('U-Y')
g_d.adicionaAresta('U-Z')
g_d.adicionaAresta('V-Z')
g_d.adicionaAresta('V-A1')
g_d.adicionaAresta('V-W')
g_d.adicionaAresta('W-S')
g_d.adicionaAresta('X-B1')
g_d.adicionaAresta('X-C1')
g_d.adicionaAresta('Y-D1')
g_d.adicionaAresta('B1-E1')
g_d.adicionaAresta('D1-E1')
g_d.adicionaAresta('E1-F1')
g_d.adicionaAresta('E1-CJ')


g = Grafo(['A','B','C','D','E','F','G','H','I','J','K'])
g.adicionaAresta('A-B')
g.adicionaAresta('A-J')
g.adicionaAresta('B-G')
g.adicionaAresta('B-C')
g.adicionaAresta('B-D')
g.adicionaAresta('B-E')
g.adicionaAresta('B-F')
g.adicionaAresta('C-D')
g.adicionaAresta('D-E')
g.adicionaAresta('F-H')
g.adicionaAresta('G-H')
g.adicionaAresta('I-G')
g.adicionaAresta('I-J')
g.adicionaAresta('J-G')
g.adicionaAresta('J-K')
g.adicionaAresta('K-H')



#g_d.adicionaAresta('T-S')

points = ['L', 'S', 'U', 'D1']
print(g_d.drone('A', 'CJ', 3, 5, points))

'''list = g_d.dijkstra('A', 'CJ')

for i in list:
    print(i, end=' ')
print()'''



