class node:
    def __init__(self,name,Xposition,Yposition,circle,goalflag,heuristic,parent=None,distance=None):
        self.children=[]#each argument in the list is a tuple consisting of node and weight(int) 
        # EX:   ([(node1,4),(node2,4),(node3,1)])
        self.nodeName=name       
        self.goalflag=goalflag #takes boolean values
        self.heuristic=heuristic #heuristic is an integer
        self.startflag=0
        self.visitflag=False
        self.mark=False
        self.Xposition=Xposition
        self.Yposition=Yposition
        self.circle=circle
        self.parent=parent
        self.distance=distance
        self.level=0 
        def __repr__(self):
            return   str((self.nodeName))
        def __str__(self):
            return str( (self.nodeName))


class nodecouples:
    def __init__(self,node1,weight,node2):
        self.node1=node1
        self.node2=node2
        self.weight=weight
class algos:
    def BFS(self,s):
            arriveflag=0
            goal=None
            visited=[]
            solutionpath=[]
            queue = []
            queue.append(s)
            s.visitflag= True
            visited.append(s)
            while queue:
                s = queue.pop(0)
                if s.goalflag==True:
                    print("line 41")
                    break
                for c in s.children:
                    if c[0].visitflag == False:
                        queue.append(c[0])
                        print("c[0].nodeName : "+c[0].nodeName)
                        c[0].visitflag = True
                        visited.append(c[0])
                        c[0].parent=s
                        if c[0].goalflag==True:
                            print("goal found which is : "+c[0].nodeName)
                            arriveflag=1
                            goal=c[0]
                            print(solutionpath)
                            break
                if arriveflag==1:
                    n=goal
                    while(True):
                        if n==None:
                            break
                        else:
                            solutionpath.append(n)
                            n=n.parent
                            print("line 75")
                            print(solutionpath)
                    solutionpath.reverse()
                    return(solutionpath,visited)
     
    def k_sorted(self,n):
        return int(n[0])
    # returns [ LIST OF VISITED NODES, SOLUTION PATH, MINIMUM COST TO GOAL]
    
    def uniform_cost_search(self,goal, start):
        # minimum cost upto
        # goal state from starting
        global graph, cost
        answer = []
        lstofvisited=[]
        parents={}
        # create a priority queue
        queue = []

        # set the answer vector to max value
        for i in range(len(goal)):              #"done"

            answer.append(10 ** 8)

        # insert the starting index     queue->frenge list of lists [[]]

        queue.append([0, start])                #-----------------"""under resolviling"""

        # map to store visited node
        visited = {}

        # count
        count = 0

        # while the queue is not empty
        while (len(queue) > 0):

            # get the top element of the
            queue = sorted(queue,key=self.k_sorted)                   #"done"
            tmp= queue[-1]                          #tmp[0]->ok-------tmp[1],[-1] not yet
            if tmp[1].nodeName not in visited:

                p = queue[-1]
            print(queue,'.....', p)

            # pop the element

            del queue[-1]

            # get the original value
            p[0] *= -1


            # check if the element is part of
            # the goal list
            if (p[1] in goal):
                parent = p[-1]
                path = [p[1]]
                while parent != start:
                    path.append(parent)
                    parent=parents[parent]
                    #parent=q
                path.append(start)

                # get the position
                index = goal.index(p[1])

                # if a new goal is reached
                if (answer[index] == 10 ** 8):
                    count += 1

                # if the cost is less
                if (answer[index] > p[0]):

                    answer[index] = p[0]

                # pop the element
                del queue[-1]

                queue = sorted(queue,key=self.k_sorted)
                if (count == 1):                #terminate when reach the first goal
                    lstofvisited.append(p[1])
                    parents.update({p[1]:p[-1]})

                    print('list of visited nodes \t',lstofvisited)
                    path.reverse()
                    print('solution path\t', path)
                    print("Minimum cost from ", start, "to", p[1], "is = ", answer[index])
                    return [lstofvisited,path,answer[index]]

            # check for the non visited nodes
            # which are adjacent to present node

            #modified from here
            if (p[1] not in visited):
                children=p[1].children.copy()

                for i in children:
                    # value is multiplied by -1 so that
                    # least priority is at the top
                    #               [num,                   node,           node]
                    if i[0] not in visited:
                         queue.insert(0, [ (p[0]+i[-1]) *-1,i[0]  ,p[1]] )           #done
                        #queue.append( [ (p[0]+i[-1]) *-1,i[0]  ,p[1]] )           #done
                    #queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i],p[1]])
                lstofvisited.append(p[1])
            # mark as visited
            visited[p[1]] = 1
            #print(visited[p[-1]])

            parents.update({p[1]:p[-1]})
        #for i in lstofvisited:
        #   print(i[0])
        print('list of visited nodes /t',lstofvisited)
        print(path)
        return answer
    def a_star_algorithm(self, start_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        visited = []
      #  visited.append(start_node)
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity


        start_node.distance = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None
            #     print(open_list)
            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or v.distance + v.heuristic < n.distance + n.heuristic:
                    n = v;
            visited.append(n)
            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n.heuristic == 0:
                solution_path = []

                while parents[n] != n:
                    solution_path.append(n)
                    n = parents[n]

                solution_path.append(start_node)

                solution_path.reverse()

               ##print('Path found: {}'.format(solution_path))
               ##print('Visited found: {}'.format(visited))
                return (solution_path, visited)

            # for all neighbors of the current node do
            for (m, weight) in n.children:
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:

                    open_list.add(m)
                    parents[m] = n
                    m.distance = n.distance + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if m.distance > n.distance + weight:
                        m.distance = n.distance + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    def Greedy(self, start_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        visited = []
       # visited.append(start_node)
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        start_node.distance = 0
        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None
            #     print(open_list)
            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or  v.heuristic <  n.heuristic:
                    n = v;
            visited.append(n)

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n.goalflag == True:
                solution_path = []

                while parents[n] != n:
                    solution_path.append(n)
                    n = parents[n]

                solution_path.append(start_node)

                solution_path.reverse()

               ##print('Path found: {}'.format(solution_path))
               ##print('Visited found: {}'.format(visited))
                return (solution_path, visited)

            # for all neighbors of the current node do
            for (m, weight) in n.children:
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list


            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    def DFS(self,n):            # prints all vertices in DFS manner from a given source.
                                # Initially mark all vertices as not visited
        visited = []
        s=(n,None)
        # Create a stack for DFS
        stack = []
        solutionpath=[]
        # Push the current source node.
        stack.append(s)
 
        while (len(stack)):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()
 
            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if (s[0].visitflag==False):
                print(s[0].nodeName,end=' ')
                s[0].visitflag = True
                visited.append(s[0])
                s[0].parent=s[1]
            if s[0].goalflag==True:
                n=s[0]
                while(True):
                        if n==None:
                            break
                        else:
                            solutionpath.append(n)
                            n=n.parent
                            print("line 75")
                            print(solutionpath)
                solutionpath.reverse()
                return(solutionpath,visited) 
            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in s[0].children:
                if (node[0].visitflag==False):
                    stack.append((node[0],s[0]))       
    
    def iterative_deepening(self,source,depth):
        visited=[]
        stack=[] #create a stack S
        source.level = 0
        solutionpath=[]
        stack.append((source,None,0))#push source onto S
       # source.visitflag=True#mark source
        source.mark=True
        while (len(stack)): #while S is not empty:
            v=stack[-1]
            stack.pop()
            #pop an item from S into v
            print (type(v[2]))
            if v[2] > depth:
                print("error line 379 etsala7")
                continue
            if (v[0].visitflag==False):
                print(v[0].nodeName)
                v[0].visitflag = True
                visited.append(v[0])
                print ("line387 v[0]"+str(v[0].nodeName))
                v[0].parent=v[1]
            if v[0].goalflag==True:
                n=v[0]
                while(True):
                        if n==None:
                            break
                        else:
                            solutionpath.append(n)
                            n=n.parent
                            print("line 75")
                            print(solutionpath)
                solutionpath.reverse()
                return(True,visited,solutionpath)

                
              
            for node in v[0].children: #for each edge e incident on v in Graph:
                if (node[0].visitflag==False):
                   
                    
                    stack.append((node[0],v[0],v[2]+1))    
        return (False,visited)
               
    def iterator(self,source,nodelist):
        arriveflag=0
        visited=[]
        L=0
        result=None
        while (len(visited)<len(nodelist)):
            result=self.iterative_deepening(source,L)
            visited=result[1]
            arriveflag=result[0]
            visitNames=[]
            if arriveflag==False:
                
                for v in result[1]:
                    visitNames.append(v.nodeName)
                print("visited of iteration "+str(L)+" is : "+str(visitNames))
                L=L+1
                for node in nodelist:
                    node.visitflag=False
                    node.parent=None
                    node.mark=False
                
            else:
                for v in result[2]:
                    visitNames.append(v.nodeName)
                print("visited of iteration "+str(L)+" is : "+str(visitNames))
                break
        #return (result[1],result[2])
        

if __name__=="__main__":
    my_node=node('a',0,0,0,False,0)           
    node1=node('b',0,0,0,False,0)
    node2=node('c',0,0,0,False,0)
    node3=node('d',0,0,0,True,0)
    my_node.children=[(node1,4),(node2,3)]
    node1.children=[(node3,1),(node2,3)]
    a=algos()
    nodelist=[my_node,node1,node2,node3]
    
    result=a.iterator(my_node,nodelist)
    print("solutionPath :")
    for k in result[0]:
        print(k.nodeName)
    print("visited")
    for k in result[1]:
        print(k.nodeName)


