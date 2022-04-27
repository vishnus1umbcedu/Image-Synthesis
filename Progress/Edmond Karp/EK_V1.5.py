from importlib.resources import path
from locale import currency
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
    #Created graph and removed linked list to know th neighbours
    #Implementing 1st round of BFS
    #Implementing 4 rounds BFS as we know the solution

    #defining the variable
    current = 0
    flow = 0
    max_flow = 0

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
    ngbr_mtrx = g_ngbr.AddToGraph(5,ng,4) 

    adj_mtx = g_am.AddToGraph(6,7,9)
    rsd_mtx = g_rm.AddToGraph(7,6,0)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(6,ng,7)
    ng += 1

    print(adj_mtx)
    #print(rsd_mtx)
    #print(ngbr_mtrx)

    round = 1
    while round < 5:
        #Implementing 1st round of BFS
        nghbr_vtx.append(1)
        visited_vertices.append(1)
        
        #Checking if we reached the sink
        while (len(nghbr_vtx) > 0):
            current = nghbr_vtx.pop(0)
            j = 0
            #Checking for neighnour whose weight is greater than 0
            while(ngbr_mtrx[current-1][j] != 0):
                if adj_mtx[current-1][ngbr_mtrx[current-1][j]-1] > 0:
                    #Checking if neighbour is visited
                    if ngbr_mtrx[current-1][j] in visited_vertices:
                        j += 1
                    else:
                        nghbr_vtx.append(ngbr_mtrx[current-1][j])
                        visited_vertices.append(ngbr_mtrx[current-1][j])
                        path_dict[ngbr_mtrx[current-1][j]] = current
                        j += 1
                else:
                    j += 1
            
        
        #Getting the flow of the path
        key = 7
        path = str(key)
        if key in path_dict:
                flow = adj_mtx[path_dict[key] -1][key-1]
                key = path_dict[key]
        else:
            key = 1
        
        while (key != 1):
            if adj_mtx[path_dict[key] -1][key-1] < flow:
                flow = adj_mtx[path_dict[key] -1][key-1]
                key = path_dict[key]
            else:
                key = path_dict[key]

        #Adjusting the flow from the residual graph
        key = 7
        if key in path_dict:
                adj_mtx[path_dict[key] -1][key-1] = adj_mtx[path_dict[key] -1][key-1] - flow
                adj_mtx[key-1][path_dict[key]-1] = adj_mtx[key-1][path_dict[key]-1] + flow
                key = path_dict[key]
        else:
            key = 1
        
        while (key != 1):
                adj_mtx[path_dict[key] -1][key-1] = adj_mtx[path_dict[key] -1][key-1] - flow
                adj_mtx[key-1][path_dict[key]-1] = adj_mtx[key-1][path_dict[key]-1] + flow
                key = path_dict[key]
        
        max_flow += flow
        print(path_dict)

        nghbr_vtx.clear()
        path_dict.clear()
        visited_vertices.clear()
        flow = 0
        #print(path)
        round += 1

    #print(nghbr_vtx)
    #print(path_dict)
    print(max_flow)
    print(adj_mtx)