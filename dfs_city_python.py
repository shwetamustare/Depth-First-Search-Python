dfsTree=[]
def dfs(vertex):
    visited[vertex]=1
    flag =0
    Neighbour = adjMat[vertex]
    for i in range(len(Neighbour)):
        if Neighbour[i] == 1:
            if visited[i] == 0:
                flag = flag+1
                dfs(i)
        if (i == (len(Neighbour)-1)):
             dfsTree.append(name[vertex])


num = input("Enter number of cities: ")
print num
name=[]
for i in range(num):
	city=i+1
	print "Enter name of city ",city,": "
	name.append(raw_input())
print "Type y if connection between cities exist and type n otherwise."
for i in range(num):
	adjMat=[[0]*num for _ in range(num)]

for i in range(num):
	for j in range(i):
		print "Are ",name[i]," and ",name[j]," connected? "
		cost = raw_input()
		if cost=='y' or cost == 'Y':
			adjMat[i][j]=1
			adjMat[j][i]=1
print "Matrix is: "
Mat=[]
for i in range(num):
	for j in range(num):
		Mat.append(adjMat[i][j])
	print Mat
	del Mat[:]

visited=[]
for i in range(num):
	visited.append(0)
print "DFS traversal is: "
dfs(0)
print dfsTree


'''
    locahost$ python city.py
    Enter number of cities: 6
    6
    Enter name of city  1 :
    a
    Enter name of city  2 :
    b
    Enter name of city  3 :
    c
    Enter name of city  4 :
    d
    Enter name of city  5 :
    e
    Enter name of city  6 :
    f
    Type y if connection between cities exist and type n otherwise.
    Are  b  and  a  connected?
    y
    Are  c  and  a  connected?
    n
    Are  c  and  b  connected?
    y
    Are  d  and  a  connected?
    y
    Are  d  and  b  connected?
    y
    Are  d  and  c  connected?
    n
    Are  e  and  a  connected?
    n
    Are  e  and  b  connected?
    n
    Are  e  and  c  connected?
    y
    Are  e  and  d  connected?
    y
    Are  f  and  a  connected?
    n
    Are  f  and  b  connected?
    y
    Are  f  and  c  connected?
    y
    Are  f  and  d  connected?
    n
    Are  f  and  e  connected?
    y
    Matrix is: 
    [0, 1, 0, 1, 0, 0]
    [1, 0, 1, 1, 0, 1]
    [0, 1, 0, 0, 1, 1]
    [1, 1, 0, 0, 1, 0]
    [0, 0, 1, 1, 0, 1]
    [0, 1, 1, 0, 1, 0]
    DFS traversal is: 
    ['d', 'f', 'e', 'c', 'b', 'a']
'''