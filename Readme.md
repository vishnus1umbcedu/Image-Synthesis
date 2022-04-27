Submitted by

KT16974, Parinitha Reddy Gaddam

IK67010, Vishnu Vardhan Samba


Find the executable file in “Proj1” folder

Installation of dependencies:

Install numpy and Opencv modules. Use the following commands in command prompt/terminal to install them: 
1. pip install numpy
2. pip install opencv-python 

Instructions to run the program:

1. Save the images from git hub repository folder to your system. Name the Picture with Hut as "hut.jpg" and Mountain as "mountain.jpg"
2. Run the python file named ImgMerge_V4.2.py
3. The program prompts for file path. Give the complete file path till the folder in which the pictures are present.
   For example: "C:\Users\parin\OneDrive\Desktop\Python" in case where your images are stored in python folder.
4. The program executes and generates output images in the same folder with the names "mergedimage_seam.jpg" and "mergedimage.jpg"

Interpreting the output: 

1. The image "mergedimage_seam.jpg" contains the seam(pixels in red) in the overlap region between the two images. The pixels above this seam
   comes from the mounatin image while the pixels below this seam comes from the hut image.
2. The image "mergedimage.jpg" gives the merged image without the seam.

Description of Assignment:

This assignment is the implementation of a part of the Paper "Graphcut Textures: Image and Video Synthesis Using Graph Cuts" by Vivek Kwatra,Arno Sch¨odl,Irfan Essa,Greg Turk,Aaron Bobick.
According to the paper, when image processing like 2D texture synthesis, Image merging and Blending are done, the Dynamic programming algorithms are used. This paper used the technique
of graph cut instead. Brief interpretation of the assignmentfor Image Blending is as follows:
1. When two images are blended, an overlap region is chosen from the two images, where the output image will contain portion of the 2 images outside the overlap region, in addition to
the blended overlap region.

2. The overlap region is blended in the following way: a graph / netwrok flow is constructed for pixels in the overlapped region.
each pixel of overlap region is depicted as a node, each node is connected to its adjecent nodes and the appropriate norm between the pixels is added as the weight of edge netween the two neighbouring nodes
The appropriate norm is calculated in the following way according to the paper:
"Let s and t be two adjacent pixel positions in the overlap region. Also, let A(s) and B(s) be the pixel colors at the positions in the old and new patches, respectively.
We define the matching quality cost M between the two adjacent pixels s and t that copy from patches A and B respectively to be:
M(s, t,A,B) = ||A(s)−B(s)||+||A(t)−B(t)||
where || · || denotes an appropriate norm."

3. Once the graph is constructed in this way, Edmond-Karp algorithm is implemented on this graph to obtain the maximum flow and minimum cuts. The Minimum cut decides which pixel comes from which image in the overlapping region.

Additional files:
Find the adjacency list in AdjacencyList.txt
Find the text file containing vector of pixels numbers which forms cuts in CutPixels.txt
