from importlib.resources import path
from locale import currency
import sys
import numpy as np
from pip import main

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
    #Implementing min cut

    #defining the variable
    current = 0
    flow = 0
    max_flow = 0

    cut1 = []
    cut2 = []

    #creating key list for min cut
    min_key = []

    #creating value list for min cut
    min_value = []

    #creating an empty list to insert and pop the neighbour vertices to a vertex
    nghbr_vtx = [] 

    #creating an empty list to add the visited vertices
    visited_vertices = []

    #creating empty dictionary to trace back the path
    path_dict = {}

    #Creating a graph for test purposes
    #Creating an adjacency matrix
    g_am = Graph()
    adj_mtx = g_am.CreateEmptyGraph(6)

    #Creating a residual matrix
    g_rm = Graph()    
    rsd_mtx = g_rm.CreateEmptyGraph(6)

    #Creating a neighbours matrix
    g_ngbr = Graph()
    ngbr_mtrx = g_ngbr.CreateEmptyGraph(6)

    #inserting values into adjacency matrix, residual matrix and linked list
    adj_mtx = g_am.AddToGraph(1,2,16)
    rsd_mtx = g_rm.AddToGraph(1,2,16)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(1,ng,2)
    ng += 1

    adj_mtx = g_am.AddToGraph(1,3,13)
    rsd_mtx = g_rm.AddToGraph(1,3,13)
    ngbr_mtrx = g_ngbr.AddToGraph(1,ng,3)
    ng += 1

    adj_mtx = g_am.AddToGraph(2,3,10)
    rsd_mtx = g_rm.AddToGraph(2,3,10)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(2,ng,3)
    ng += 1
    adj_mtx = g_am.AddToGraph(2,4,12)
    rsd_mtx = g_rm.AddToGraph(2,4,12)
    ngbr_mtrx = g_ngbr.AddToGraph(2,ng,4)
    ng += 1

    ngbr_mtrx = g_ngbr.AddToGraph(2,ng,1)
    ng += 1

    adj_mtx = g_am.AddToGraph(3,2,4)
    rsd_mtx = g_rm.AddToGraph(3,2,4)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(3,ng,2)
    ng += 1

    adj_mtx = g_am.AddToGraph(3,5,14)
    rsd_mtx = g_rm.AddToGraph(3,5,14)
    ngbr_mtrx = g_ngbr.AddToGraph(3,ng,5)
    ng += 1

    ngbr_mtrx = g_ngbr.AddToGraph(3,ng,1)
    ng += 1

    ngbr_mtrx = g_ngbr.AddToGraph(3,ng,4)
    ng += 1

    adj_mtx = g_am.AddToGraph(4,3,9)
    rsd_mtx = g_rm.AddToGraph(4,3,9)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(4,ng,3)
    ng += 1
    adj_mtx = g_am.AddToGraph(4,6,20)
    rsd_mtx = g_rm.AddToGraph(4,6,20)
    ngbr_mtrx = g_ngbr.AddToGraph(4,ng,6)
    ng += 1

    ngbr_mtrx = g_ngbr.AddToGraph(4,ng,2)
    ng += 1

    ngbr_mtrx = g_ngbr.AddToGraph(4,ng,5)
    ng += 1

    adj_mtx = g_am.AddToGraph(5,6,4)
    rsd_mtx = g_rm.AddToGraph(5,6,4)
    ng = 1
    ngbr_mtrx = g_ngbr.AddToGraph(5,ng,6)
    ng += 1
    adj_mtx = g_am.AddToGraph(5,4,7)
    rsd_mtx = g_rm.AddToGraph(5,4,7)
    ngbr_mtrx = g_ngbr.AddToGraph(5,ng,4)
    ng += 1
    ngbr_mtrx = g_ngbr.AddToGraph(5,ng,3)

    print(adj_mtx)
    #rsd_mtx = adj_mtx
    print(rsd_mtx)
    #print(ngbr_mtrx)

    go = 1
    while go == 1:
        min_value.clear()
        min_key.clear()

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
                        min_key.append(ngbr_mtrx[current-1][j])
                        min_value.append(current)
                        j += 1
                else:
                    j += 1
            
        
        #Getting the flow of the path
        key = 6
        if key in path_dict:
                flow = adj_mtx[path_dict[key] -1][key-1]
                key = path_dict[key]
        else:
            key = 1
            go = 0
        
        while (key != 1):
            if adj_mtx[path_dict[key] -1][key-1] < flow:
                flow = adj_mtx[path_dict[key] -1][key-1]
                key = path_dict[key]
            else:
                key = path_dict[key]

        #Adjusting the flow from the residual graph
        key = 6
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
        #round += 1

    #print(nghbr_vtx)
    #print(path_dict)
    print(min_key)
    print(min_value)
    print(max_flow)
    print(adj_mtx)

    #finding min cut
    for i in range(len(min_key)):
        j = 0
        while ngbr_mtrx[min_key[i]-1][j] != 0:
            if ngbr_mtrx[min_key[i]-1][j] in min_value:
                j += 1
            else:
                if rsd_mtx[min_key[i]-1][ngbr_mtrx[min_key[i]-1][j]-1] == adj_mtx[ngbr_mtrx[min_key[i]-1][j]-1][min_key[i]-1]:
                    cut1.append(min_key[i])
                    cut2.append(ngbr_mtrx[min_key[i]-1][j])
                j += 1

    print(rsd_mtx)
    print(cut1)
    print(cut2)
