# -*- coding: utf-8 -*-

class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param M: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k > l:
                        M[k].append('-')
                    else:
                        M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not (self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-')  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def print(self):
        print('+', end=' ')
        for i in self.N:
            print(i, end=' ')
        print()
        for x in range(len(self.M)):
            print(self.N[x], end=' ')
            for y in self.M[x]:
                print(y, end=' ')
            print()

    def vertices_nao_adjacentes(self):
        retorno = []
        for x in self.N:
            for y in self.N:
                vert = x + self.SEPARADOR_ARESTA + y
                if not self.existeAresta(vert):
                    retorno.append(vert)
        return retorno

    def ha_laco(self):
        retorno = []
        for x in self.N:
            for y in self.N:
                if x == y:
                    vert = x + self.SEPARADOR_ARESTA + y
                    if self.existeAresta(vert):
                        return True
        return False

    def ha_paralelas(self):
        for x in self.M:
            for y in x:
                if y != self.SEPARADOR_ARESTA and y > 1:
                    return True
        return False

    def grau(self, v):
        cont = 0
        vindx = self.N.index(v)

        for i in self.M[vindx]:
            if i != self.SEPARADOR_ARESTA:
                cont += i

        for i in self.M:
            if self.M.index(i) != vindx and i[vindx] != self.SEPARADOR_ARESTA:
                cont += i[vindx]

        return cont

    def arestas_sobre_vertice(self, v):
        lista = []

        vert = self.N
        vindx = vert.index(v)

        x = self.M[vindx]

        for i in range(len(self.M)):
            y = self.M[i]
            if y[vindx] != self.SEPARADOR_ARESTA and y[vindx] > 0:
                for j in range(y[vindx]):
                    lista.append(self.N[i] + self.SEPARADOR_ARESTA + v)

        for i in range(len(x)):
            if x[i] != self.SEPARADOR_ARESTA and x[i] > 0:
                for j in range(x[i]):
                    lista.append(v + self.SEPARADOR_ARESTA + vert[i])

        return lista

    def eh_completo(self):

        for x in range(len(self.M)):
            q = len(self.N) - (x + 1)
            cont = 0
            contlaco = 0

            linha = self.M[x]
            for y in range(len(linha)):
                if linha[y] != self.SEPARADOR_ARESTA and linha[y] > 0 and x != y:
                    cont += 1
                    if x == y and linha[y] > 0:
                        contlaco += 1

            if cont != (q + contlaco) and cont != q:
                return False

        return True
    

    def vertices_adj(self, v):
        ares = self.arestas_sobre_vertice(v)
        for i in range(len(ares)):
            a = ares[i].split(self.SEPARADOR_ARESTA)
            if a[0] == v:
                ares[i] = a[1]
            elif a[1] == v:
                ares[i] = a[0]
        return ares

    def arvore_dfs(self,raiz):
        retorno = [raiz]

        return self.arvore_dfs_recursiva(raiz,retorno)

        
    def arvore_dfs_recursiva(self, raiz, retorno):
        count=2
        adj = self.vertices_adj(raiz)
        ares = self.arestas_sobre_vertice(raiz)

        for i in range(0, len(adj)):
                if adj[i] not in retorno :
                    retorno.append(ares[i])
                    retorno.append(adj[i])
                    count-=1

                    retorno = self.arvore_dfs_recursiva(adj[i], retorno)

        return retorno

    def conexo(self):
        for i in self.N:
            for j in self.N:
                if not self.caminho_dois_vertices(i, j):
                    return False
        return True


    def caminho_dois_vertices(self, i, f):
        lista = self.arvore_dfs(i)
        if i in lista and f in lista:
            return True
        else:
            return False

    def ha_euleriano(self):
        list_impar = self.grau_impar_par("impar")

        q_impar = len[list_impar]
        if (q_impar != 2 and q_impar != 0):
            return False
        return True
    
    def ha_pontes(self):
        import copy
        pontes = []
        matriz = copy.deepcopy(self.M)
        for x in range(len(self.M)):
            for y in range(len(self.M[x])):
                aresta = self.M[x][y]
                aresta_str = self.N[x] + self.SEPARADOR_ARESTA + self.N[y]
                if aresta==1 and aresta!=self.SEPARADOR_ARESTA:
                    self.remove_aresta(aresta_str)
                    if not self.conexo():
                        pontes.append(aresta_str)
                    self.M = copy.deepcopy(matriz)

        return pontes
                    

    def grau_impar_par(self, tipo):
        list_impar = []
        list_par = []

        for i in self.N:
            if self.grau(i) % 2 == 0:
                list_par.append(i)
            else:
                list_impar.append(i)
        if tipo == "impar":
            return list_impar
        elif tipo == "par":
            return list_par

    def todos_os_caminhos(self,inicio,fim):
        import copy
        path = []
        matriz = copy.deepcopy(self.M)
        while(True):
            current = inicio
            adj = self.vertices_adj(inicio)
            for v in adj:
                path.append([])




    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str
