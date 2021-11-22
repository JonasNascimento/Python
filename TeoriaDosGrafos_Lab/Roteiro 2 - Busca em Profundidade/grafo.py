class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

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

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def vertices_nao_adjacentes(self):
        lista_de_valores=self.A.values()
        resultado = []
        for i in self.N:
            for j in self.N:
                a_going = '{}-{}'.format(i,j)
                a_backing = '{}-{}'.format(j,i)

                if a_going not in lista_de_valores and a_backing not in lista_de_valores:
                    resultado.append(a_going)

        return resultado

    def ha_laco(self):
        lista_de_valores=self.A.values()
        form = '{}-{}'
        resultado = False
        for i in self.N:
            for j in self.N:
                if(i==j) and ((form.format(i,j)) in lista_de_valores):
                    resultado = True
        return resultado

    def ha_paralelas(self):
        cont = 0
        lista = self.A.values()
        for i in self.N:
            for j in self.N:
                form = '{}-{}'.format(j,i)
                form2 = '{}-{}'.format(i,j)
                if form in lista:
                    for x in lista:
                        if x==form or x==form2:
                            cont+=1
                    if cont>=2:
                        return True
                    cont = 0

        return False

    def grau(self,v):
        lista_de_valores = self.A.values()
        cont = 0
        for i in lista_de_valores:
            i.split('-')
            if i[0]==v or i[2]==v:
                cont+=1

        return cont

    def eh_completo(self):
        lista = self.A.values()

        for i in self.N:
            for j in self.N:
                form = '{}-{}'.format(i,j)
                if i!=j and form not in lista:
                    form = '{}-{}'.format(j,i)
                    if form not in lista:
                        return False
        return True

    def arestas_sobre_vertice(self,v):
        lista = self.A.values()
        keys = []
        retorno = []
        cont = 0
        for j in self.A:
           keys.append(j)

        for i in keys:
            a = self.A.get(i)
            a.split('-')
            if a[0]==v or a[2]==v:
                retorno.append(i)

        return retorno

    def vertices_adjacentes(self, v):
        adj = []
        ares = self.arestas_sobre_vertice(v)
        for i in range(0, len(ares)):
            adj.append(self.A.get(ares[i]))
            p = adj[i].split('-')

            if p[0] == v:
                adj[i] = p[1]

            elif p[1] == v:
                adj[i] = p[0]

        return adj


    def arvore_dfs(self,raiz):
        retorno = [raiz]

        return self.arvore_dfs_recursiva(raiz,retorno)

        
    def arvore_dfs_recursiva(self, raiz, retorno):
        adj = self.vertices_adjacentes(raiz)
        ares = self.arestas_sobre_vertice(raiz)

        for i in range(0, len(adj)):
                if adj[i] not in retorno:
                    retorno.append(ares[i])
                    retorno.append(adj[i])
                    retorno = self.arvore_dfs_recursiva(adj[i], retorno)

        return retorno


    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str































