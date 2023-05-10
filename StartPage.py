#import main_file
import math
from turtle import color
from line import DrawLineApp
from Page1 import Page1
from page11 import Page11
import tkinter as tk
from tkinter import  ttk
from tkinter import*
from tkinter import messagebox
from node import node
from PIL import Image,ImageTk
LARGEFONT =("Verdana", 35)
class StartPage(tk.Frame):
    def __init__(self, parent, controller,list,theCanvas,edgeList,nodelist,goalslist ,edgeflag,start_node,searchType,alphabet_list,transitions_list):
    
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.edgeflag=edgeflag       # weight flag 
        self.start=0  # 0 if no start node seected
        self.goal=0   # 0 if no goal node seected
        self.searchType=searchType
        self.searchType.append("Breadth First search")
        self.start_node=start_node
        self.goalslist=goalslist
        self.edgeList=edgeList
        self.hflag=0   # flag if the chosen algorithm must contain heuristic value
        self.alphabet_list=alphabet_list
        self.transitions_list=transitions_list
        # label of frame Layout 2
        options = [
        "Breadth First search",
        "uniform cost search",
        "Depth first search",
        "iterative deepening search",
        "Greedy search",
        "A* search"
                        ]
        clicked = StringVar()
        clicked.set( "Monday" )
#        self.combo=ttk.Combobox( self , value =options )
#        self.combo.current(0)
#        self.combo.bind("<<ComboboxSelected>>",self.comboclick)
#        self.combo.place(x=300,y=100)
        label = ttk.Label(self, text ="Design your Nodes in the gray area", font = LARGEFONT)
        label_alphabet=ttk.Label(self, text ="enter alphabet in the range of small english letters, use e as epsilon")
        self.label_alphabetList=ttk.Label(self, text =self.alphabet_list)
        label3=ttk.Label(self,text="to add a node you must :\n(1)enter the node name in the space below\n(2)click the draw node(or Goal) button\n(3)make a click in the gray area")
        self.Hlabel=ttk.Label(self, text ="heuristic of node")
        startlabel=ttk.Label(self, text ="click the button then click on the node you want to set as start")
        # making the text
        #draw_line=DrawLineApp(self,row=1,column=2)
        #self.mycanvas=Canvas(self,bg='light grey')
        self.mycanvas=theCanvas
        self.mycanvas.place(x=600,y=100,height=650,width=700)
        points = self.P(60,0), self.P(90,50), self.P(50,100), self.P(10,50), self.P(40,0)
        
#        fracture = self.mycanvas.create_line(points, arrow='last', fill='yellow')
###       Creating a semi circle arrow
        #smooth = self.mycanvas.create_line(points, arrow='last', smooth=1)
        self.name = StringVar()
        self.hName= StringVar()
        self.alphabetNameAdd= StringVar()
        self.alphabetNameDelete= StringVar()
        self.nodeEntry=Entry(self,textvariable=self.name)
        self.hEntry=Entry(self,textvariable=self.hName)
        self.alphabetEntryForAdd=Entry(self,textvariable=self.alphabetNameAdd)
        self.alphabetEntryForDelete=Entry(self,textvariable=self.alphabetNameDelete)
        self.nodelist=nodelist
        self.list=list # list that stores the names of nodes
        label2 = ttk.Label(self, text ="enter node name")
        self.click_number=0
        #button_draw_line = ttk.Button(self, text ="draw_line",command=self.linking)
        btn_draw_circle = ttk.Button(self, text ="draw_node",command=self.linking_2)
        self.btn_draw_goal = ttk.Button(self, text ="Draw Goal State",command=self.linking_3)
        self.btn_choose_goal = ttk.Button(self, text ="Choose Goal State",command=self.Goal_linking)
        self.btn_clear = ttk.Button(self, text ="Clear",command=self.clear)

        #img= (Image.open("fig.png"))

        #Resize the Image using resize method
        #resized_image= img.resize((300,205), Image.ANTIALIAS)
        #new_image= ImageTk.PhotoImage(resized_image)
        btn_add_alphabet=ttk.Button(self, text ="add alphabet",command=self.add_alphabet)
        btn_delete_alphabet=ttk.Button(self, text ="delete alphabet",command=self.delete_alphabet)
        btn_choose_start=ttk.Button(self, text ="choose start node",command=self.Start_linking)
        btn_undo_start=ttk.Button(self, text ="deselect the sart node",command=self.call_undo_start)
        btn_undo_goal=ttk.Button(self, text ="deselect the goal node",command=self.call_undo_goal)
        #if (edgeflag==2 or edgeflag==0):
        self.button1 = ttk.Button(self, text ="add undirected edges",
        command = self.btn1_func)
        self.button2 = ttk.Button(self, text ="add directed edges",
        command = self.btn2_func)
        
        #button_draw_line.grid(row = 2, column = 0 ,padx = 10, pady = 10,sticky='W')
        btn_draw_circle.place(x=10, y=300)
        #self.btn_draw_goal.place(x=10, y=250)
        self.btn_clear.place(x=800,y=760)
        self.btn_choose_goal.place(x=10, y=520)
        #btn_undo_goal.place(x=10, y=500)
        btn_choose_start.place(x=10,y=550)
        startlabel.place(x=150,y=550)
        btn_undo_start.place(x=10,y=600)
        label2.place(x=10,y=350)
        label_alphabet.place(x=10,y=400)
        self.alphabetEntryForAdd.place(x=10,y=420)
        btn_add_alphabet.place(x=150,y=420)
        self.label_alphabetList.place(x=250,y=420)
        self.alphabetEntryForDelete.place(x=10,y=450)
        btn_delete_alphabet.place(x=150,y=450)
        label.grid(row = 0, column = 0, padx = 10, pady = 10,columnspan=3)
        label3.place(x=120,y=280)

        self.nodeEntry.place(x=123,y=350)
        #self.hEntry.place(x=123,y=400)
        #self.Hlabel.place(x=10,y=400)
       
       # self.button1.place(x=10,y=670) # here we are making nfa , no need for undirected edges        
        self.button2.place(x=150,y=670)
    def is_single_alpha(input_str):
        if len(input_str) != 1:  # Check if input is a single character
            return False
        elif not input_str.isalpha():  # Check if input is an alphabetic character
            return False
        elif input_str not in 'abcdefghijklmnopqrstuvwxyz':  # Check if input is between a to z
            return False
        else:
            return True
    def add_alphabet(self):
        input_add=self.alphabetEntryForAdd.get()
        if len(input_add) != 1:  # Check if input is a single character
            messagebox.showwarning("wrong choice","one letter at a time")
        elif not input_add.isalpha():  # Check if input is an alphabetic character
            messagebox.showwarning("wrong choice","enter only alphabets")
        elif input_add not in 'abcdefghijklmnopqrstuvwxyz':  # Check if input is between a to z
            messagebox.showwarning("wrong choice","small letters from a to z only")
        else:
           self.alphabet_list.append(input_add)
           self.label_alphabetList.config(text=self.alphabet_list)
           
        
    def delete_alphabet(self):
        input_add=self.alphabetEntryForDelete.get()
        if len(input_add) != 1:  # Check if input is a single character
            messagebox.showwarning("wrong choice","one letter at a time")
        elif not input_add.isalpha():  # Check if input is an alphabetic character
            messagebox.showwarning("wrong choice","enter only alphabets")
        elif input_add not in 'abcdefghijklmnopqrstuvwxyz':  # Check if input is between a to z
            messagebox.showwarning("wrong choice","small letters from a to z only")
        else:
           self.alphabet_list.remove(input_add)
           self.label_alphabetList.config(text=self.alphabet_list)
    def P(self,x,y):
        """
        For convenience only.
        Transform point in cartesian (x,y) to Canvas (X,Y)
        As both system has difference y direction:
        Cartesian y-axis from bottom-left - up 
        Canvas Y-axis from top-left - down 
        """
        X = 4 + (x/100) * (310-2*4)
        Y = 4 + (1-(y/100)) * (210-2*4)
        return (X,Y)
    def clear(self):
        self.mycanvas.delete("all")
        self.nodelist.clear()
        self.list.clear()
        self.edgeList.clear()
        self.start_node.clear()
        #self.searchType.clear()
        #self.searchType.append("Breadth First search")
        self.start=0
        self.goal=0
    """
    def comboclick(self,event):
        k=self.searchType.pop()
        self.searchType.append(self.combo.get())
        print("search types is :"+self.combo.get())
        if self.combo.get()=="A* search" or self.combo.get()=="Greedy search":
            self.hEntry.place(x=123,y=400)
            self.Hlabel.place(x=10,y=400)
            self.btn_draw_goal.place(x=10, y=250)
            self.btn_choose_goal.place_forget()
            self.hflag=1
           
        else :
            self.Hlabel.place_forget()
            self.hEntry.place_forget()
            self.btn_draw_goal.place_forget()
            self.btn_choose_goal.place(x=10, y=450)
            self.hflag=0
            #Page1.weigh
        if self.combo.get() in ["Breadth First search","Depth first search","iterative deepening search "]:
            self.edgeflag=0
        else:
            self.edgeflag=1
    """
    def btn1_func(self):
        if self.start==1 and self.goal!=0:
            self.controller.show_frame(Page1)
            self.button2.destroy()
        else :messagebox.showwarning("wrong choice","You must select the start and goal node")
    def btn2_func(self):
        if self.start==1 and self.goal!=0:
            self.controller.show_frame(Page11)
            self.button1.destroy()
           
        else :messagebox.showwarning("wrong choice","You must select the start node and goal node")
    def linking_2 (self):
        self.edgeflag=1
        print("type of Hentry is :")
        print(type(self.hEntry.get()))
        if len(self.nodeEntry.get())>2:
            messagebox.showwarning("wrong choice","more than 2 characters")
        elif(self.list.count(self.nodeEntry.get())>0):
            messagebox.showwarning("wrong choice","no 2 nodes could have the same name") 
        elif  self.hflag==1 and((self.hEntry.get()).isnumeric() )==FALSE :
             messagebox.showwarning("wrong choice","a heuristic must be integer")  
        elif self.hflag==1 and (int(self.hEntry.get()))==0  :
             messagebox.showwarning("wrong choice","only the goal state which can have  the heuristic equal to 0")        
        else:
            global nodeName
            nodeName=self.nodeEntry.get()

            self.mycanvas.bind('<Button-1>',self.draw_circle)
            
            self.list.append(nodeName)
            print(self.list)
        """
            if self.list.count()==1:
                print("first list element")
                with open('gfg.txt', 'w+') as f:
      
            # write elements of list
           
                    f.write('%s\n' %nodeName)
                f.close()
            else:
                with open('gfg.txt', 'a+') as f:
                    f.write('%s\n' %nodeName)
                f.close()  """
    def Start_linking(self):
        if self.start==0:
            self.mycanvas.bind('<Button-1>',self.select_start)
        else :
             messagebox.showwarning("wrong choice","the start node is alreay set")
    def Goal_linking(self):
        #if self.goal==0:
            self.mycanvas.bind('<Button-1>',self.select_goal)
        #else :
          #   messagebox.showwarning("wrong choice","the start node is alreay set")
    def call_undo_start(self):
        if self.start==1:
            self.mycanvas.bind('<Button-1>',self.undo_start)
        else :
             messagebox.showwarning("wrong choice","there is no start node to deselect")
    def call_undo_goal(self):
        if self.goal!=0:
            self.mycanvas.bind('<Button-1>',self.undo_goal)
        else :
             messagebox.showwarning("wrong choice","there is no goal node to deselect")
    def linking_3 (self):
        #print(int(self.hEntry.get()))
        if len(self.nodeEntry.get())>2:
            messagebox.showwarning("wrong choice","more than 2 characters")
        elif(self.list.count(self.nodeEntry.get())>0):
            messagebox.showwarning("wrong choice","no 2 nodes could have the same name") 
        elif self.hflag==1 and ((int(self.hEntry.get()))!=0) and (self.hEntry.get()!=''):
            print("self.hEntry.get()="+str(int(self.hEntry.get())))
            print("line110")
            messagebox.showwarning("wrong choice","a heuristic to a goal must be Zero")                    
        else:
            global nodeName
            self.goal+=1
            nodeName=self.nodeEntry.get()
            self.mycanvas.bind('<Button-1>',self.draw_goal)            
            self.list.append(nodeName)
            print(self.list)
        
    def draw_circle(self,event):
        x3=event.x
        y3=event.y
        my_circle=self.mycanvas.create_oval(x3-20,y3-20,x3+20,y3+20,width=1,tags="oval")
        self.mycanvas.tag_bind(my_circle,'<Button-1>',lambda x:print("m"))
        print(type(my_circle))
        self.mycanvas.create_text((x3, y3), text=nodeName)
        if self.hflag==0:
            nodeheuristic=500
        else:
            nodeheuristic=int(self.hEntry.get())
        my_node=node(nodeName,x3,y3,my_circle,FALSE,nodeheuristic)
        print("is the node:"+nodeName+"  a goal?")
        print(my_node.goalflag)
        self.nodelist.append(my_node)
       # print(self.dict)
        #x = self.dict.get("aa")
        #print("line76"+str(x.Xposition))
        print(self.nodelist)
        self.mycanvas.unbind('<Button-1>',self.draw_circle)
        
    def draw_goal(self,event):
        x3=event.x
        y3=event.y
        my_circle=self.mycanvas.create_oval(x3-20,y3-20,x3+20,y3+20,width=1,tags="oval",fill='red')
        self.mycanvas.create_text((x3, y3), text=nodeName)
        my_node=node(nodeName,x3,y3,my_circle,True,0)
        print("is the node:"+nodeName+"  a goal?")
        print(my_node.goalflag)
        self.nodelist.append(my_node)
        self.goalslist.append(node)
       # print(self.dict)
        #x = self.dict.get("aa")
        #print("line76"+str(x.Xposition))
        print(self.nodelist)
        self.mycanvas.unbind('<Button-1>',self.draw_circle)
########## color and set the start node
    def select_start(self,event):
        x3=event.x
        y3=event.y
        distanceflag=0
        for node in self.nodelist:
            distance = math.sqrt( (node.Xposition-(event.x))**2+((node.Yposition-(event.y))**2)) 
            if distance<=(40*math.sqrt(2)):              
                distanceflag=1
                break
        if self.start==1:
            return
        if distanceflag==1:             
            node.startflag=1
            self.start=1 
            self.start_node.append(node)
            self.mycanvas.itemconfig(node.circle, fill='green') 
         
        else :
            messagebox.showwarning("wrong choice","you must click inside a circle")     
        print(self.nodelist)
        self.mycanvas.unbind('<Button-1>',self.select_start)
    def select_goal(self,event):
        x3=event.x
        y3=event.y
        distanceflag=0
        ## bug fixed##
        
          ##end of bug
        for node in self.nodelist:
            distance = math.sqrt( (node.Xposition-(event.x))**2+((node.Yposition-(event.y))**2)) 
            if distance<=(40*math.sqrt(2)):              
                distanceflag=1
                if node.goalflag==1:
                    messagebox.showwarning("wrong choice","the node is alreaddy a goal")
                    return
                break
        if distanceflag==1:             
            node.goalflag=1
            self.goal=self.goal+1 
            self.goalslist.append(node)
            print ("goals:")
            for goal in self.goalslist:
                print(goal.nodeName)
            self.mycanvas.create_oval(node.Xposition-15,node.Yposition-15,node.Xposition+15,node.Yposition+15,width=1,tags="oval")  
        else :
            messagebox.showwarning("wrong choice","you must click inside a circle")     
        print(self.nodelist)
        self.mycanvas.unbind('<Button-1>',self.select_goal)
    def undo_start(self,event):
        distanceflag=0
        for node in self.nodelist:
            distance = math.sqrt( (node.Xposition-(event.x))**2+((node.Yposition-(event.y))**2)) 
            if distance<=(40*math.sqrt(2)):              
                distanceflag=1
                break
        if distanceflag==1:             
            node.startflag=0
            self.start=0 
            f=self.start_node.pop()
            self.mycanvas.itemconfig(node.circle, fill='')  
        else :
            messagebox.showwarning("wrong choice","you must click inside a circle")
    def undo_goal(self,event):
        distanceflag=0
        for node in self.nodelist:
            distance = math.sqrt( (node.Xposition-(event.x))**2+((node.Yposition-(event.y))**2)) 
            if distance<=(40*math.sqrt(2)):              
                distanceflag=1
                break
        if distanceflag==1:             
            node.goalflag=0
            self.goal=self.goal-1 
            f=self.goalslist.pop()
            self.mycanvas.itemconfig(node.circle, fill='')  
        else :
            messagebox.showwarning("wrong choice","you must click inside a circle")
    def linking (self):
        self.mycanvas.bind('<Button-1>',self.draw_line)
        print('line 45')
        
        print('line 47')
        #mycanvas.bind('<Button-1>',draw_line)
    def draw_line(self,event):
        #global click_number
        global x1,y1
        # thecanvas.bind('<Button-1>',self.draw_line)
        if (self.click_number==0):
            x1=event.x
            y1=event.y
            self.click_number=1
            
        else :
            x2=event.x
            y2=event.y
            self.mycanvas.create_line(x1,y1,x2,y2,fill='black',width=1)
            #self.mycanvas.create_oval(x1-50,y1-50,x1,y1,width=1,tags="oval")
            self.click_number=0
            #self.mycanvas.unbind('<Button-1>',self.draw_line)
        

  
  