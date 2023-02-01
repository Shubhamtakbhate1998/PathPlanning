
import numpy as np

#define a start node accordingly
#start=np.array([[1,4,7],[5,0,8],[2,3,6]])
start=np.array([[4,7,0],[1,2,8],[3,5,6]])
end=np.array([[1,4,7],[2,5,8],[3,6,0]])


#these functions helps to check if children nodes generated are visited or not
def is_visited(array1,list_arrays):
  for i in list_arrays:
    if ((array1==i).all()):
      return False
  
  return True
def is_visited_queue(array1,queue):
  for i in queue:
    if ((array1==i).all()):
      return False
  
  return True      
####################################################################################


#this function expands the tiles in the puzzle and give possible children nodes
def expand(node):
  children=[]    
  row, col = np.where(node == 0)
  if(row>0):
      C=np.copy(node)
      C[row,col]=C[row-1,col]
      C[row-1,col]=0
      children.append(C)
  if (row<2):
      C=np.copy(node)
      C[row,col]=C[row+1,col]
      C[row+1,col]=0
      children.append(C)   
  if (col>0):
      C=np.copy(node)
      C[row,col]=C[row,col-1]
      C[row,col-1]=0 
      children.append(C)        
  if(col<2): 
        C=np.copy(node)
        C[row,col]=C[row,col+1]
        C[row,col+1]=0 
        children.append(C) 
  return children


#function for BFS
 
def bfs(start,goal):
  parent_id=0
  queue = []
  visited =[] 
  
  queue.append(start)
  q_backtracking=[(start,parent_id)]
  
  visited_backtracking=[(start,parent_id)]
  
  
  while queue and not ((start==goal).all()):
    
    start = queue.pop(0)
    visited.append(start)
    
    a, b = q_backtracking.pop(0)
    visited_backtracking.append((a, b))
    parent_id=parent_id+1
    for neighbour in expand(start):
      if is_visited(neighbour, visited) and is_visited_queue(neighbour, queue):
        queue.append(neighbour)
        q_backtracking.append((neighbour, parent_id))
  
  return q_backtracking,visited_backtracking      
     
Queue,Visited=bfs(start,end) 


Visited_Nodes_List=[]
Node_index=[]
parent_index=[]
data=[]
#printing visited nodes
for i, j in enumerate(Visited[1::]):
  start , parent_id = j

 
  Visited_Nodes_List.append(start)
  print("Printing all visited node with parent id as matrix for visulisation")
  print(f'{i}: {start} {parent_id-1}')
  
  if i==0 and parent_id==0:
     Node_index.append("Node_index")
     parent_index.append("parent_index")
  else:
    Node_index.append(i)
    parent_index.append(parent_id-1) 
  
  print("************************************")
Node_index=np.array(Node_index)
Node_index = Node_index.reshape(-1, 1)
parent_index=np.array(parent_index)
parent_index=parent_index.reshape(-1,1)
data=np.array([])
data=np.append(Node_index,parent_index,axis=1)

#uncomment following four lines for genarating NodesInfo(Please provide correct address)


# file = open("/home/shubham/NodesInfo.txt", "w+")
# content = str(data)
# file.write(content)
# file.close()  


Visited_Nodes_List.pop(0)  #In code 0th node is appended twice hence poping the zeroth node
print("Visited nodes")
One_D=[]
for i in Visited_Nodes_List:
    i=np.array(i)
    i=i.flatten()
    One_D.append(i)
    print(i)
 
One_D=np.array(One_D)
#uncomment following four lines for genarating Nodes(Please provide correct address)

# file = open("/home/shubham/Nodes.txt", "w+")
# content = str(One_D)
# file.write(content)
# file.close() 


  
global var  
var=len(Visited)-1

back_track_list=[]
while var !=0:
  node,var=Visited[var]
  back_track_list.append(node)
  
back_track_list.reverse()
j=1
print("printing the solution to solve puzzle")
Solution=[]
for i in back_track_list:
    i=np.array(i)
    i=i.flatten()
    Solution.append(i)
    print(i,j)
    j+=1
Solution=np.array((Solution)) 
#uncomment following four lines for genarating NodesPath(Please provide correct address) 

# file = open("/home/shubham/NodesPath.txt", "w+")
# content = str(Solution)
# file.write(content)
# file.close() 







              



  
  



      


   
    




      









         
