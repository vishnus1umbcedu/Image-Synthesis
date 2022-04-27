from math import sqrt
import math
import sys
import cv2
import copy
import numpy as np
imghut = "C:/Users/vishn/Desktop/Python/hut.jpg"
imgmount = "C:/Users/vishn/Desktop/Python/mountain.jpg"

#Implementing residual graph
#Adding neighbour matrix
#Implementing Edmond Karp
#Implementing min cut
#Implementing seam
#Inplemented converting nodes to pixels
#Refining neighbour matrix

class Graph:
    def _init_(self):
        self.d = None

     #creating an adjacency matrix
    def CreateEmptyGraph(self,number_of_vertices):
        self.d = np.zeros((number_of_vertices,number_of_vertices),float)
        return self.d

    #assigning values to adjacency matirx
    def AddToGraph(self,start_vertex,end_vertex,weight):
        self.d[start_vertex-1][end_vertex-1] = weight
        return self.d

class IntGraph:
    def _init_(self):
        self.d = None

     #creating an adjacency matrix
    def CreateEmptyGraph(self,number_of_vertices):
        self.d = np.zeros((number_of_vertices,number_of_vertices),int)
        return self.d

    #assigning values to adjacency matirx
    def AddToGraph(self,start_vertex,end_vertex,weight):
        self.d[start_vertex-1][end_vertex-1] = weight
        return self.d

g = Graph()
r = Graph()
n = IntGraph()
adj_mtx = g.CreateEmptyGraph(5442)
rsd_mtx = r.CreateEmptyGraph(5442)
ngbr_mtx = n.CreateEmptyGraph(5442)

img1 = cv2.imread(imghut)
#(h1,w1) = img1.shape[:2]
#print(h1,w1)
img2 = cv2.imread(imgmount)
#(h2,w2) = img2.shape[:2]
#print(h2,w2)

croppedimg1 = img1[102:216,0:272]
cv2.imwrite("C:/Users/vishn/Desktop/Python/result.jpg", croppedimg1)
color = (img1[200, 200])
#print (color[0]-color[1])
croppedimg2 = img2[0:236,0:272]
croppedresult = cv2.vconcat([croppedimg2,croppedimg1])
cv2.imwrite("C:/Users/vishn/Desktop/Python/result2.jpg", croppedimg2)
cv2.imwrite("C:/Users/vishn/Desktop/Python/resultf.jpg", croppedresult)

overlap1 = img1[90:110,0:272]
overlap2 = img2[230:250,0:272]
cv2.imwrite("C:/Users/vishn/Desktop/Python/overlap1.jpg", overlap1)
cv2.imwrite("C:/Users/vishn/Desktop/Python/overlap2.jpg", overlap2)
(h1,w1) = overlap1.shape[:2]
(h2,w2) = overlap2.shape[:2]
#print(h1,w1)


count = 0
numf = 1
numt = numf + w1
for i in range (0,h1):
    for j in range (0,w1):
        
        if j<w1-1:
            color1 = overlap1[i,j]
            color2 = overlap2[i,j]
            normval1 = (color1[0]-color2[0])^2+(color1[1]-color2[1])^2+(color1[2]-color2[2])^2
            color1 = overlap1[i,j+1]
            color2 = overlap2[i,j+1]
            normval2 = (color1[0]-color2[0])^2+(color1[1]-color2[1])^2+(color1[2]-color2[2])^2
            normval = normval1+normval2
            #print(normval)
            count = count+1
            #call adjmatrix fncn for [i,j],[i,j+1],normval
            #call adjmatrix for numf, numf+1, normal
            ng = 1
            while ngbr_mtx[numf+1][ng-1] != 0:
                ng += 1
            #adding data to adjacency matrix
            adj_mtx = g.AddToGraph(numf+1,numf+2, normval)
            #adding data to residual matrix which is a replica of adjacency matrix
            rsd_mtx = r.AddToGraph(numf+1,numf+2, normval)
            ngbr_mtx = n.AddToGraph(numf+1,ng,numf+2)
            ng = 1
            while ngbr_mtx[numf+2][ng-1] != 0:
                ng += 1
            ngbr_mtx = n.AddToGraph(numf+2,ng,numf+1)
            #print(ngbr_mtx)


        if i<h1-1:
            color1 = overlap1[i+1,j]
            color2 = overlap2[i+1,j]
            normval2 = (color1[0]-color2[0])^2+(color1[1]-color2[1])^2+(color1[2]-color2[2])^2
            normval = normval1+normval2
            #print(normval)
            count = count + 1
            #call adjmatrix fncn for [i,j],[i+1,j],normval
            #call adjmatrix for numf,numt, normval
            ng = 1
            while ngbr_mtx[numf+1][ng-1] != 0:
                ng += 1
            #adding data to adjacency matrix
            adj_mtx = g.AddToGraph(numf+1,numt+1, normval)
            #adding data to residual matrix
            rsd_mtx = r.AddToGraph(numf+1,numt+1,normval)
            ngbr_mtx = n.AddToGraph(numf+1,ng,numt+1)
            ng = 1
            while ngbr_mtx[numt+1][ng-1] != 0:
                ng += 1
            ngbr_mtx = n.AddToGraph(numt+1,ng,numf+1)
        numf = numf+1
        numt = numt+1
    
#print(numf)
#print(numt)    
#print(count)
            
ng = 1
for x in range(2, 273+1):
    #call adjmatrix for 0,x,inf
    #call adjmatrix for 5150+x,5151,inf
    #adding dat to adjacency and residual matrix
    adj_mtx = g.AddToGraph(0+1,x, math.inf)
    rsd_mtx = r.AddToGraph(0+1,x, math.inf)
    ngbr_mtx = n.AddToGraph(1,ng,x)
    adj_mtx = g.AddToGraph(5168+x,5441+1, math.inf)
    rsd_mtx = r.AddToGraph(5168+x,5441+1, math.inf)
    ngbr_mtx = n.AddToGraph(5168+x,1,5442)
    ng+=1

#print(adj_mtx)
#print(adj_mtx[0][272])

#Implementing Edmond Karp
#defining the variable
print(ngbr_mtx[274][0])
print(ngbr_mtx[274][3])
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
        while(ngbr_mtx[current-1][j] != 0):
            if adj_mtx[current-1][ngbr_mtx[current-1][j]-1] > 0:
                #Checking if neighbour is visited
                if ngbr_mtx[current-1][j] in visited_vertices:
                    j += 1
                else:
                    nghbr_vtx.append(ngbr_mtx[current-1][j])
                    visited_vertices.append(ngbr_mtx[current-1][j])
                    path_dict[ngbr_mtx[current-1][j]] = current
                    min_key.append(ngbr_mtx[current-1][j])
                    min_value.append(current)
                    j += 1
            else:
                j += 1
            
        
    #Getting the flow of the path
    key = 5442
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
    key = 5442
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
    #print(path_dict)

    nghbr_vtx.clear()
    path_dict.clear()
    visited_vertices.clear()
    flow = 0

    #print(path)
    #round += 1

#print(nghbr_vtx)
#print(path_dict)
#print(min_key)
#print(min_value)
#print(max_flow)
#print(adj_mtx)

#finding min cut
for i in range(len(min_key)):
    j = 0
    while ngbr_mtx[min_key[i]-1][j] != 0:
        if ngbr_mtx[min_key[i]-1][j] in min_value:
            j += 1
        else:
            if rsd_mtx[min_key[i]-1][ngbr_mtx[min_key[i]-1][j]-1] == adj_mtx[ngbr_mtx[min_key[i]-1][j]-1][min_key[i]-1]:
                cut1.append(min_key[i])
                cut2.append(ngbr_mtx[min_key[i]-1][j])
            j += 1

#print(rsd_mtx)
#print(cut1)
#print(cut2)
print(max_flow)
#print(len(cut1))
#print(len(cut2))

finlist = []
finlist = [6000 for i in range (272)]
reminder = 3
for reminder in range (3,271):
    for i in range (0,len(cut1)):
        if cut1[i]%272 == reminder:
            #print(i)
            #print(cut1[i])
            #print(cut2[i])
            finlist[reminder-2] = cut1[i]
print(finlist)
for i in range (0, len(finlist)):
    if finlist[i] != 6000:
        finlist[i] = finlist[i]//272

#print(finlist)


#seam= 10
#arr = []
#arr = [10 for i in range(272)]
#print(arr)
imgnew = np.zeros((20,272,3), np.uint8)
#cv2.imwrite("C:/Users/parin/OneDrive/Desktop/result/blankimg.jpg", imgnew)
for wid in range (0,272):
    for len in range (0,20):
        if len < finlist[wid]+1:
            imgnew[len,wid] = overlap2[len,wid]
        else:
            imgnew[len,wid] = overlap1[len,wid]

cv2.imwrite("C:/Users/vishn/Desktop/Python/finimg.jpg", imgnew)
croppedresult = cv2.vconcat([croppedimg2,imgnew])
croppedresult = cv2.vconcat([croppedresult,croppedimg1])
cv2.imwrite("C:/Users/vishn/Desktop/Python/mergedimg.jpg", croppedresult)

#print(adj_mtx[5440][5441])
#for i in range (0,5):
#    print(ngbr_mtx[3-1][i])
#print(ngbr_mtx)






 


