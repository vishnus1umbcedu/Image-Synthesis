import numpy as np

class Graph:

    def __init__(self):
        self.d = None

    def CreateEmptyGraph(self,number_of_vertices):
        self.d = np.zeros((number_of_vertices-1,number_of_vertices-1),int)
        return self.d

    def AddToGraph(self,start_vertex,end_vertex,weight):
        self.d[start_vertex-1][end_vertex-1] = weight
        return self.d


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

    #g = Graph()
    #e = g.CreateEmptyGraph(9)
    #e = g.AddToGraph(3,3,1)
    #print(e)