from fileinput import filename
from math import sqrt
import math
import sys
import cv2
import copy
import numpy as np

#Used for adjacency matrix with float values
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

#Used for matrix having neighbours of a vertex with integer values
class IntGraph:
    def _init_(self):
        self.d = None

     #creating an adjacency matrix
    def CreateEmptyGraph(self,number_of_vertices):
        self.d = np.empty((number_of_vertices,number_of_vertices),int)
        return self.d

    #assigning values to adjacency matirx
    def AddToGraph(self,start_vertex,end_vertex,weight):
        self.d[start_vertex-1][end_vertex-1] = weight
        return self.d

if __name__ == "__main__":
    #Gettig and constructing the file path
    filepath = input("Please name the images as hut.jpg and mountain.jpg. Enter file path of the images: ")
    filepath = filepath.replace("\\","/")

    imghut = filepath+"/hut.jpg"
    imgmount = filepath+"/mountain.jpg"

    #Reading image of hut
    img1 = cv2.imread(imghut)

    #Reading image of mountain
    img2 = cv2.imread(imgmount)

    #Selecting the overlap region of the two images to be merged
    overlap1 = img1[90:110,0:272]
    overlap2 = img2[230:250,0:272]

    #Getting the dimensions from the overlapped region
    (h1,w1) = overlap1.shape[:2]
    (h2,w2) = overlap2.shape[:2]

    #Initializing the mattrices from class graph
    g = Graph()
    r = Graph()
    n = IntGraph()

    #Creating adjacency, residual and neighbours matrix
    #Adjacency matrix is used from updating the weights after every BFS
    #Residual matrix maintains the initial weights of the graph
    #Neighbours matrix maintains the neighbours of ebery vertex
    adj_mtx = g.CreateEmptyGraph((h1*w1)+2)
    rsd_mtx = r.CreateEmptyGraph((h1*w1)+2)
    ngbr_mtx = n.CreateEmptyGraph((h1*w1)+2)

    count = 0
    numf = 1
    numt = numf + w1

    #Calculating the appropriate norm between neighbouring pixels in the overlap region
    for i in range (0,h1):
        for j in range (0,w1):
            ng = 0
            if j<w1-1:
                color1 = overlap1[i,j]
                color2 = overlap2[i,j]
                normval1 = (color1[0]-color2[0])^2+(color1[1]-color2[1])^2+(color1[2]-color2[2])^2

                color1 = overlap1[i,j+1]
                color2 = overlap2[i,j+1]
                normval2 = (color1[0]-color2[0])^2+(color1[1]-color2[1])^2+(color1[2]-color2[2])^2

                normval = normval1+normval2
                count = count+1
                
                #adding data to adjacency matrix
                adj_mtx = g.AddToGraph(numf+1,numf+2, normval)

                #adding data to residual matrix
                rsd_mtx = r.AddToGraph(numf+1,numf+2, normval)

                #Updating the neighbours matrix
                ngbr_mtx = n.AddToGraph(numf+1,ng,numf+2)
                ng += 1


            if i<h1-1:
                color1 = overlap1[i+1,j]
                color2 = overlap2[i+1,j]
                normval2 = (color1[0]-color2[0])^2+(color1[1]-color2[1])^2+(color1[2]-color2[2])^2

                normval = normval1+normval2
                
                count = count + 1
                
                #adding data to adjacency matrix
                adj_mtx = g.AddToGraph(numf+1,numt+1, normval)

                #adding data to residual matrix
                rsd_mtx = r.AddToGraph(numf+1,numt+1,normval)

                #Updating the neighbours matrix
                ngbr_mtx = n.AddToGraph(numf+1,ng,numt+1)
            numf = numf+1
            numt = numt+1
                    
    ng = 0

    for x in range(2, 274):
        #adding data to adjacency, residual matrix and neighbour matrix
        adj_mtx = g.AddToGraph(1,x, math.inf)
        rsd_mtx = r.AddToGraph(1,x, math.inf)
        ngbr_mtx = n.AddToGraph(1,ng,x)
    
        adj_mtx = g.AddToGraph((w1*(h1-1))+x,(h1*w1)+2, math.inf)
        rsd_mtx = r.AddToGraph((w1*(h1-1))+x,(h1*w1)+2, math.inf)    
        ngbr_mtx = n.AddToGraph((w1*(h1-1))+x,1,(h1*w1)+2)
        ng+=1

    #Implementing Edmond Karp
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

        #Implementing rounds of BFS
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
        key = (h1*w1)+2
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
        key=(h1*w1)+2
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

        nghbr_vtx.clear()
        path_dict.clear()
        visited_vertices.clear()
        flow = 0

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

    #Mapping node values to the pixel to contruct the mearged image
    finlist = []
    finlist = [20000 for i in range (272)]
    reminder = 3
    for reminder in range (3,272):
        for i in range (0,len(cut1)):
            if cut1[i]%272 == reminder:
                finlist[reminder-2] = cut1[i]

    reminder = 0
    for reminder in range (0,2):
        for i in range(0,len(cut1)):
            if cut1[i]%272 == reminder:
                if reminder == 0:
                    finlist[len(finlist)-2] =  cut1[i]
                if reminder == 1:
                    finlist[len(finlist)-1] =  cut1[i]

    for i in range (0, len(finlist)):
        if finlist[i] != 20000:
            finlist[i] = finlist[i]//272

    imgnew = np.zeros((h1,272,3), np.uint8)

    for wid in range (0,272):
        for len in range (0,h1):
            if len < finlist[wid]+1:
                imgnew[len,wid] = overlap2[len,wid]
            else:
                imgnew[len,wid] = overlap1[len,wid]

    #Writing the merged image to output path
    croppedimg1= img1[110:216,0:272]
    croppedimg2= img2[0:230,0:272]
    croppedresult = cv2.vconcat([croppedimg2,imgnew])
    croppedresult = cv2.vconcat([croppedresult,croppedimg1])
    cv2.imwrite((filepath+"/mergedimage.jpg"),croppedresult)
    filepath = filepath.replace("/","\\")
    print("Find the output image here: "+filepath+"\mergedimage.jpg")