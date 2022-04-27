import numpy as np

class Graph:
    def __init__(self):
        self.d = None

     #creating an adjacency matrix
    def CreateEmptyGraph(self,number_of_vertices):
        self.d = np.zeros((number_of_vertices,number_of_vertices),int)
        return self.d

    #assigning values to adjacency matirx
    def AddToGraph(self,start_vertex,end_vertex,weight):
        self.d[start_vertex-1][end_vertex-1] = weight
        return self.d

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #inserting adjacent vertices of a vertex
    def insert_values(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    #getting adjacent vertices of a vertex
    def traverse(self):

        ngbr = []

        if self.head is None:
            return ngbr

        itr = self.head
        
        while itr:
            ngbr.append(itr.data)
            itr = itr.next
        return ngbr


if __name__ == "__main__":
    #implementing Edmond Karp to find the max flow

    #defining the variable
    #current
    #flow
    #max_flow

    #creating an empty list to insert and pop the neighbour vertices to a vertex
    nghbr_vtx = [] 

    #creating an empty list to add the visited vertices
    visited_vertices = []

    #creating empty dictionary to trace back the path
    path_dict = {}

    #Creating a graph for test purposes
    #Creating an adjacency matrix
    g_am = Graph()
    adj_mtx = g_am.CreateEmptyGraph(7)

    #Creating a residual matrix
    g_rm = Graph()    
    rsd_mtx = g_rm.CreateEmptyGraph(7)

    #inserting values into adjacency matrix, residual matrix and linked list
    adj_mtx = g_am.AddToGraph(1,2,3)
    rsd_mtx = g_rm.AddToGraph(2,1,0)
    gl1 = LinkedList()
    gl1.insert_values(1)
    gl1.insert_values(2)
    #gl1_p = gl1.traverse()
    #print(adj_mtx)
    #print(rsd_mtx)
    #print(gl1_p)

    adj_mtx = g_am.AddToGraph(1,4,3)
    rsd_mtx = g_rm.AddToGraph(4,1,0)
    gl1.insert_values(4)

    adj_mtx = g_am.AddToGraph(2,3,4)
    rsd_mtx = g_rm.AddToGraph(3,2,0)
    gl2 = LinkedList()
    gl2.insert_values(2)
    gl2.insert_values(3)

    adj_mtx = g_am.AddToGraph(3,1,3)
    rsd_mtx = g_rm.AddToGraph(1,3,0)
    gl3 = LinkedList()
    gl3.insert_values(3)
    gl3.insert_values(1)

    adj_mtx = g_am.AddToGraph(3,4,1)
    rsd_mtx = g_rm.AddToGraph(4,3,0)
    gl3.insert_values(4)

    adj_mtx = g_am.AddToGraph(3,5,2)
    rsd_mtx = g_rm.AddToGraph(5,3,0)
    gl3.insert_values(5)

    adj_mtx = g_am.AddToGraph(4,5,2)
    rsd_mtx = g_rm.AddToGraph(5,4,0)
    gl4 = LinkedList()
    gl4.insert_values(4)
    gl4.insert_values(5)

    adj_mtx = g_am.AddToGraph(4,6,6)
    rsd_mtx = g_rm.AddToGraph(6,4,0)
    gl4.insert_values(6)

    adj_mtx = g_am.AddToGraph(5,7,1)
    rsd_mtx = g_rm.AddToGraph(7,5,0)
    gl5 = LinkedList()
    gl5.insert_values(5)
    gl5.insert_values(7)

    adj_mtx = g_am.AddToGraph(6,7,9)
    rsd_mtx = g_rm.AddToGraph(7,6,0)
    gl6 = LinkedList()
    gl6.insert_values(6)
    gl6.insert_values(7)

    #gl1_p = gl1.traverse()
    #print(adj_mtx)
    #print(rsd_mtx)
    #print(gl1_p)