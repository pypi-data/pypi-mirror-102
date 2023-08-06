# relation.py
"""
@author hawksoft

This package provides Realtion class as an complement to sympy package. 

## install: 
    pip install hawksoft.relation

## usage:

remember: Relation is defined on a set A, which is called discourse. so the first thing is define a set A.
1 set discourse A at first
  Relation.setA(1,2,3)
2 create  a relation object:
  r1 = Relation((1,2),(2,3))
3 use the object
  r1.showSet()  # will show the relation as a set
  r1.showGraph() # will show the relation as a graph
  r1.showMatrix() # will show the relation as a matrix  
4 the relation object can be used as sympy object 
  r2 = r1 ** -1  # get converse relation
"""
import sympy

from sympy.abc import x,y

#import graphviz as gz
import networkx

#import matplotlib
#print(matplotlib.get_backend())
#matplotlib.use('AAgg') 

import matplotlib.pyplot as plt

class Relation(sympy.FiniteSet):
    """
    Define Relation class inherited from FinitSet.
    @author hawksoft
    """
    A = sympy.FiniteSet()
    id2items = {}
    @classmethod
    def setA(cls,*items):
        """
        This is a class method. Set discourse

        Parameters:
            items: lists of elements of set
        Returns:
            no return
        """
        cls.A = sympy.FiniteSet(*items)
        cls.id2items= {}
        num  = 0
        for i in cls.A:
            cls.id2items[num] = i
            num = num + 1
    @classmethod
    def getUniversal(cls):
        """
        This is a class method. Get the Universal Relation on the discourse.

        Parameters:
            none.
        Returns:
            Return the universal relation on discourse.
        """
        temp = cls.A * cls.A
        l = []
        for i in temp:
            l.append(i)
        return Relation(*l,name = 'Universal Relation')
    @classmethod
    def getIdentity(cls):
        """
        This is a class method. Get the Identity Relation on the discourse.

        Parameters:
            none.
        Returns:
            Return the identity relation on discourse.
        """
        l = []
        for i in range(0,len(cls.id2items)):
             item = (cls.id2items[i],cls.id2items[i])
             l.append(item)
        return Relation(*l)
    def __init__(self,*items,name='noName'):
        '''
        Init a relation object.

        parameters:
          items: 2-tuple list define the relation
          name:this is an optional argument,you can give name to the relation
        returns
           a relation object  
        example:
           Relation.setA(1,2,3)
           r1  = Relation((1,2),(2,3),name = "simple relation')

        '''
        #if sympy.Eq(self.A,sympy.EmptySet):
        #    print('empty A')
        #    self.setA(1,2,3,4)
        if len(items) == 0:
            sympy.FiniteSet(('xxx','xxx'))
        else:
            sympy.FiniteSet(self,*items)
        self.name = name
        
    
    def drawGraphbyGraphviz(self):
        '''
        Draw relation graph by using graphviz package. Do not use it.
        '''
        g = gz.Graph(format='png')
        for i in self.C:
            g.node(str(i))
        l = []
        for i in self:
            l.append(str(i[0])+str(i[1]))
        g.edges(l)
        #print(g.source)
        g.render('./test',view=True) 
    def drawDigraphbyGraphviz(self):
        '''
        Draw relation graph by using graphviz package. Do not use it.
        '''
        g = gz.Digraph(format='png')
        for i in self.A:
            g.node(str(i))
        l = []
        for i in self:
            l.append(str(i[0])+str(i[1]))
        g.edges(l)
        #print(g.source)
        g.render('./test',view=True) 

    def showSet(self):
        '''
        This method show relation as a set

        Parameters:
          None.
        Returns:
          None.
        '''
        sympy.pprint(self)
    def showGraph(self):
        '''
        This method show relation as a graph.

        Parameters:
          None.
        Returns:
          None.
        '''
        g = networkx.DiGraph()
        listNode = [self.id2items[i] for i in self.id2items]
        g.add_nodes_from(listNode)
        listEdge =[]
        for i in range(len(self.id2items)):
            for j in range(len(self.id2items)):
                item = (self.id2items[i],self.id2items[j])
                if self.contains(item) == True:
                    listEdge.append(item)
        g.add_edges_from(listEdge)
        plt.subplot(111)
        networkx.draw(g, with_labels=True, font_weight='bold')
        plt.show()
    def showMatrix(self):
        '''
        This method show relation as a matrix.

        Parameters:
          None.
        Returns:
          None.
        '''
        self.toMatrix()
        sympy.pprint(self.matrix)
    def toMatrix(self):
        if self.is_empty:
            matrix = sympy.zeros(len(len(self.id2itmes),len(self.id2itmes)))
        else:
            mat = []
            for i in range(0,len(self.id2items)):
                line = []
                for j  in range(0,len(self.id2items)):
                    item = (self.id2items[i],self.id2items[j])
                    if self.contains(item)==True:
                        line.append(1)
                    else:
                        line.append(0)
                mat.append(line)
        self.matrix = sympy.Matrix(mat)
        return self.matrix
    def fromMatrix(self,matrix):
        l = []
        for i in range(0,len(self.id2items)):
            rows = matrix.row(i)
            for j in range(0, len(self.id2items)):
                if rows[j] == 1:
                    item = (self.id2items[i],self.id2items[j])
                    l.append(item)
        if len(l) == 0:
            l.append(('xxx','xxx'))
        return Relation(*l)
    def __add__(self,adds):
        '''
        Return a new relation which is self union with adds.
        ''' 
        temp = self.union(adds)
        l = []
        for i in temp:
            l.append(i)
        if len(l) == 0:
            l.append(('xxx','xxx'))
        result = Relation(*l) 
        return result
    def __sub__(self,subs):
        '''
        Return a new relation which is self sub subs.
        ''' 
        temp = sympy.Complement(self,subs)
        l = []
        for i in temp:
            l.append(i)
        if len(l) == 0:
            l.append(('xxx','xxx'))
        result = Relation(*l) 
        return result
        
    def __pow__(self,num):
        '''
        Return a new relation which is self's power.
        
        Parameters
          num: the exponents
        ''' 
        mat = self.toMatrix()
        if num == -1:
            mat = mat.T
        else:
            mat = mat**num
        return self.fromMatrix(mat)

    def intersect(self,other):
        temp = self.intersect(other)
        print(temp)
        l = []
        for i in temp:
            l.append(i)
        if len(l) == 0:
            l.append(('xxx','xxx'))
        result = Relation(*l) 
        return result
    def reflectiveClosure(self):
        '''
        Return the reflectiveClosure
        '''
        return self + self.getIdentity()
    def symmetricClosure(self):
        '''
        Return the symmetricClosure
        '''
        return self + self ** -1
    def transitiveClosure(self):
        '''
        Return the transitiveClosure
        '''
        temp = self 
        for i in range(2,len(self.id2items)):
            temp1 = temp ** i
            temp = temp + temp1
        return temp

