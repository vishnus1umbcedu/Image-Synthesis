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

if __name__ == "__main__":
    #implementing Edmond Karp to find the max flow
    #Created graph and removed linked list to know th neighnors

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

    #Creating a neighbours matrix
    g_ngbr = Graph()
    ngbr_mtrx = g_ngbr.CreateEmptyGraph(7)

    #inserting values into adjacency matrix, residual matrix and linked list
    adj_mtx = g_am.AddToGraph(1,2,3)
    rsd_mtx = g_rm.AddToGraph(2,1,0)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(1,ng,2)
    ng += 1

    adj_mtx = g_am.AddToGraph(1,4,3)
    rsd_mtx = g_rm.AddToGraph(4,1,0)
    ngbr_mtrx = g_ngbr.AddToGraph(1,ng,4)

    adj_mtx = g_am.AddToGraph(2,3,4)
    rsd_mtx = g_rm.AddToGraph(3,2,0)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(2,ng,3)
    ng += 1

    adj_mtx = g_am.AddToGraph(3,1,3)
    rsd_mtx = g_rm.AddToGraph(1,3,0)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(3,ng,1)
    ng += 1

    adj_mtx = g_am.AddToGraph(3,4,1)
    rsd_mtx = g_rm.AddToGraph(4,3,0)
    ngbr_mtrx = g_ngbr.AddToGraph(3,ng,4)
    ng += 1

    adj_mtx = g_am.AddToGraph(3,5,2)
    rsd_mtx = g_rm.AddToGraph(5,3,0)
    ngbr_mtrx = g_ngbr.AddToGraph(3,ng,5)
    ng += 1

    adj_mtx = g_am.AddToGraph(4,5,2)
    rsd_mtx = g_rm.AddToGraph(5,4,0)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(4,ng,5)
    ng += 1

    adj_mtx = g_am.AddToGraph(4,6,6)
    rsd_mtx = g_rm.AddToGraph(6,4,0)
    ngbr_mtrx = g_ngbr.AddToGraph(4,ng,6)
    ng += 1

    adj_mtx = g_am.AddToGraph(5,7,1)
    rsd_mtx = g_rm.AddToGraph(7,5,0)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(5,ng,7)
    ng += 1

    adj_mtx = g_am.AddToGraph(6,7,9)
    rsd_mtx = g_rm.AddToGraph(7,6,0)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(6,ng,7)
    ng += 1

    #print(adj_mtx)
    #print(rsd_mtx)
    #print(ngbr_mtrx)