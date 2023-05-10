import tkinter as tk
from tkinter import  ttk
from tkinter import*
from PIL import Image,ImageTk
from node import *
from StartPage import StartPage
from graphviz import Digraph
from conversion import NFA
class graphResut(tk.Frame):
    def __init__(self,parent,controller,theCanvas,nodelist,start_node,searchType,alphabet_list,transitions_list):
        tk.Frame.__init__(self, parent)
        self.searchType=searchType
        self.controller=controller
        self.mycanvas=theCanvas
        self.mycanvas.place(x=600,y=100,height=650,width=700)
        self.nodelist=nodelist
        self.start_node=start_node # list that contain the start node
        self.alphabet_list=alphabet_list
        self.transitions_list=transitions_list
        #result=self.aySearch(nodelist)
        self.a=algos()
        self.visited=[]
        self.solutionPath=[]
        self.table=[]
        self.newflag=1
        self.last_in_table=False
        img= (Image.open("play.png"))
        #Resize the Image using resize method
        resized_image= img.resize((30,30), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)

        img_1= (Image.open("yellow.png"))
        #Resize the Image using resize method
        resized_image_1= img_1.resize((30,30), Image.ANTIALIAS)
        new_image_1= ImageTk.PhotoImage(resized_image_1)

        

        img_2= (Image.open("light blue.png"))
        #Resize the Image using resize method
        resized_image_2= img_2.resize((30,30), Image.ANTIALIAS)
        new_image_2= ImageTk.PhotoImage(resized_image_2)
        #photo = PhotoImage(file = r"play.png")

        

        self.finish_visit=0
        self.goals_list=[]
        button1 = ttk.Button(self, text ="add Nodes",
                            command = lambda : controller.show_frame(StartPage))
        self.label_yellow=ttk.Label(self, text ="visited node",image=new_image_1,compound='left')
        self.label_lightBlue=ttk.Label(self, text ="solution path node",image=new_image_2,compound='left')
        self.label_yellow.image=new_image_1
        self.label_lightBlue.image=new_image_2
        self.label_yellow.place(x=10,y=600)
        self.label_lightBlue.place(x=10,y=630)

        button1.place(x=400,y=500)
        btn_start_searching = ttk.Button(self, text ="generate DFA",command=self.generateDFA)
        btn_start_searching.place(x=10,y=50)
        btn_play = ttk.Button(self,image=new_image,command=self.coloring)
        btn_play.image=new_image
        btn_play.place(x=400,y=300)
        self.label=ttk.Label(self, text ="")
        self.label.place(x=300,y=100)
        #for v in visited:
        #    self.mycanvas.itemconfig(v.circle, fill="yellow") 













        
    def generateDFA(self):
        nfaNodes=[]
        nfaGoals=[]
        nfaStarts=[]
        for node in self.nodelist:
            
            print ("nodeName:",node.nodeName)
            nfaNodes.append(node.nodeName)
            if node.goalflag==1:
                nfaGoals.append(node.nodeName)
            if node.startflag==1:
                nfaStarts.append(node.nodeName)
        print("nfaGoals",nfaGoals)
        print("nfaStarts",nfaStarts)
        print("nfa nodes",nfaNodes)
        nfa = NFA(
            len(nfaNodes), # number of states
            nfaNodes, # array of states
           len( (self.alphabet_list)), # number of alphabets
            self.alphabet_list, # array of alphabets
            nfaStarts[0], # start state
            len(nfaGoals), # number of final states
            nfaGoals, # array of final states
            len(self.transitions_list), # number of transitions
            self.transitions_list
            
            # array of transitions with its element of type :
            # [from state, alphabet, to state]
        )
        print("self.transitions_list",self.transitions_list)

        # nfa = NFA.fromUser() # To get input from user
        # print(repr(nfa)) # To print the quintuple in console

        # Making an object of Digraph to visualize NFA diagram
        nfa.graph = Digraph()

        # Adding states/nodes in NFA diagram
        for x in nfa.states:
            # If state is not a final state, then border shape is single circle
            # Else it is double circle
            if (x not in nfa.finals):
                nfa.graph.attr('node', shape='circle')
                nfa.graph.node(x)
            else:
                nfa.graph.attr('node', shape='doublecircle')
                nfa.graph.node(x)

        # Adding start state arrow in NFA diagram
        nfa.graph.attr('node', shape='none')
        nfa.graph.node('')
        nfa.graph.edge('', nfa.start)

        # Adding edge between states in NFA from the transitions array
        for x in nfa.transitions:
            nfa.graph.edge(x[0], x[2], label=('ε', x[1])[x[1] != 'e'])

        # Makes a pdf with name nfa.graph.pdf and views the pdf
        ###nfa.graph.render('nfa', view=True)

        # Making an object of Digraph to visualize DFA diagram
        dfa = Digraph(format="png")

        # Finding epsilon closure beforehand so to not recalculate each time
        epsilon_closure = dict()
        for x in nfa.states:
            epsilon_closure[x] = list(nfa.getEpsilonClosure(x))


        # First state of DFA will be epsilon closure of start state of NFA
        # This list will act as stack to maintain till when to evaluate the states
        dfa_stack = list()
        dfa_stack.append(epsilon_closure[nfa.start])

        # Check if start state is the final state in DFA
        if (nfa.isFinalDFA(dfa_stack[0])):
            dfa.attr('node', shape='doublecircle')
        else:
            dfa.attr('node', shape='circle')
        dfa.node(nfa.getStateName(dfa_stack[0]))

        # Adding start state arrow to start state in DFA
        dfa.attr('node', shape='none')
        dfa.node('')
        dfa.edge('', nfa.getStateName(dfa_stack[0]))

        # List to store the states of DFA
        dfa_states = list()
        dfa_states.append(epsilon_closure[nfa.start])

        # Loop will run till this stack is not empty
        while (len(dfa_stack) > 0):
            # Getting top of the stack for current evaluation
            cur_state = dfa_stack.pop(0)

            # Traversing through all the alphabets for evaluating transitions in DFA
            for al in range((nfa.no_alphabet) - 1):
                # Set to see if the epsilon closure of the set is empty or not
                from_closure = set()
                for x in cur_state:
                    # Performing Union update and adding all the new states in set
                    from_closure.update(
                        set(nfa.transition_table[str(x)+str(al)]))

                # Check if epsilon closure of the new set is not empty
                if (len(from_closure) > 0):
                    # Set for the To state set in DFA
                    to_state = set()
                    for x in list(from_closure):
                        to_state.update(set(epsilon_closure[nfa.states[x]]))

                    # Check if the to state already exists in DFA and if not then add it
                    if list(to_state) not in dfa_states:
                        dfa_stack.append(list(to_state))
                        dfa_states.append(list(to_state))

                        # Check if this set contains final state of NFA
                        # to get if this set will be final state in DFA
                        if (nfa.isFinalDFA(list(to_state))):
                            dfa.attr('node', shape='doublecircle')
                        else:
                            dfa.attr('node', shape='circle')
                        dfa.node(nfa.getStateName(list(to_state)))

                    # Adding edge between from state and to state
                    dfa.edge(nfa.getStateName(cur_state),
                            nfa.getStateName(list(to_state)),
                            label=nfa.alphabets[al])
                    
                # Else case for empty epsilon closure
                # This is a dead state(ϕ) in DFA
                else:
                
                    # Check if any dead state was present before this
                    # if not then make a new dead state ϕ
                    if (-1) not in dfa_states:
                        dfa.attr('node', shape='circle')
                        dfa.node('ϕ')

                        # For new dead state, add all transitions to itself,
                        # so that machine cannot leave the dead state
                        for alpha in range(nfa.no_alphabet - 1):
                            dfa.edge('ϕ', 'ϕ', nfa.alphabets[alpha])

                        # Adding -1 to list to mark that dead state is present
                        dfa_states.append(-1)

                    # Adding transition to dead state
                    dfa.edge(nfa.getStateName(cur_state,),
                            'ϕ', label = nfa.alphabets[al])

        # Makes a pdf with name dfa.pdf and views the pdf
        dfa.render('dfa')
        img_3= (Image.open("dfa.png"))
        #Resize the Image using resize method
        resized_image_3= img_3#.resize((650,700), Image.ANTIALIAS)
        new_image_3= ImageTk.PhotoImage(resized_image_3)    
        self.dfaImage=ttk.Label(self, image=new_image_3,compound='left')
        self.dfaImage.image=new_image_3
        self.dfaImage.place(x=1350,y=100)
        dfa.clear()
        nfa.graph.clear()
        
        



















    def aySearch(self):
        for n in self.nodelist:
            if n.goalflag==True:
                self.goals_list.append(n)
        search_type=self.searchType[0]
        start_node=self.start_node[0]
        print("name of startnode "+self.start_node[0].nodeName)
        print("TYPE OF startnode"+str(type(start_node)))
        print("self.searchType="+self.searchType[0])
        if search_type=="Breadth First search":
            print("breadth first*******")
            result=self.a.BFS(start_node)
            self.visited=result[1]
            self.solutionPath=result[0]
        elif search_type=="uniform cost search":
            result=self.a.uniform_cost_search(self.goals_list,start_node)
            self.visited=result[0]
            self.solutionPath=result[1]
        elif search_type=="A* search":
            print("A* search*******")
            result=self.a.a_star_algorithm(start_node)
            self.visited=result[1]
            self.solutionPath=result[0]
        elif search_type=="Greedy search":
            print("Greedy search*******")
            result=self.a.Greedy(start_node)
            self.visited=result[1]
            self.solutionPath=result[0]
        elif search_type=="Depth first search":
            print("DFS*******")
            result=self.a.DFS(start_node)
            self.visited=result[1]
            self.solutionPath=result[0]
        elif search_type=="iterative deepening search":
            print("Iterative *************")
            self.label.config(text="")
            self.iterator(start_node,self.nodelist)

        """
        visited_names=['a','b','c','d']
        solutionPath_names=['a','b','d']
        visited=[]
        solutionPath=[]
        for name in visited_names:
            for node in self.nodelist:
                if node.nodeName ==name:
                    visited.append(node)
        for name in solutionPath_names:
            for node in self.nodelist:
                if node.nodeName ==name:
                    solutionPath.append(node)      
        #return (visited,solutionPath)
        self.visited=visited
        self.solutionPath=solutionPath
        """
    def coloring(self):
        if self.searchType[0]=="iterative deepening search":
            print("line 117")
            self.coloring_2()
        else:
            if len(self.visited)!=0:
                node=self.visited.pop(0)
                self.mycanvas.itemconfig(node.circle, fill="yellow")
            else :
                node=self.solutionPath.pop(0)
                self.mycanvas.itemconfig(node.circle, fill="light blue")
    def iterator(self,source,nodelist):
        #label=ttk.Label(self, text ="")
        #label.place(x=300,y=100)
        arriveflag=0
        visited=[]
        table=[]
        L=0
        result=None
        while (len(visited)<len(nodelist)):
            result=self.a.iterative_deepening(source,L)
            visited=result[1]
            arriveflag=result[0]
            my_text=""
            visitNames=[]
            if arriveflag==False:
               
                for v in result[1]:
                    
                    visitNames.append(v.nodeName)
                my_text=my_text+"\nvisited of iteration "+str(L)+" is : "+str(visitNames)
                self.table.append([result[1],my_text])
                #label.config(text =my_text)
                print("visited of iteration"+str(L)+"is :"+str(visitNames))
                L=L+1
                for node in nodelist:
                    node.visitflag=False
                    node.parent=None
                    node.mark=False
                
            else:
                
                for v in result[1]:
                    visitNames.append(v.nodeName)
                my_text=my_text+"\nvisited of iteration "+str(L)+" is : "+str(visitNames)
                self.table.append([result[1],my_text,result[2]])
                #label.config(text =my_text)
                print("visited of iteration "+str(L)+" is : "+str(visitNames))
                break
        #return (result[1],result[2])
    def coloring_2(self):
        print(len(self.table))
        row=None
        if self.newflag==1:
            print("line 169")
            row=self.table.pop(0)
            self.visited=row[0]
            self.label.config(text=row[1])
            print("********************* row[1]: "+row[1])
            self.newflag=0
            if len(self.table)==0:
                self.last_in_table=True
                self.solutionPath=row[2]
                self.newflag=0
            
            
            
        if len(self.visited)!=0:
            node=self.visited.pop(0)
            self.mycanvas.itemconfig(node.circle, fill="yellow")
            if len(self.visited)==0:
                if self.last_in_table==False:
                    self.newflag=1
        else:
            if(self.last_in_table==True):
                node=self.solutionPath.pop(0)
                self.mycanvas.itemconfig(node.circle, fill="light blue")
                if len(self.solutionPath)==0:
                    self.last_in_table=False
                    self.newflag=1
               


        