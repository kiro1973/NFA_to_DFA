#developed by kirollos george
from turtle import bgcolor
from StartPage import StartPage
from Page1 import Page1
from graphResult import graphResut
from page11 import Page11
import tkinter as tk
from tkinter import*
from tkinter import ttk
from node import node 
#start page for drawin nodes
#page 1 for drawing undirected edges
# page 11 for drawing directed edges
LARGEFONT =("Verdana", 35)  
class tkinterApp(tk.Tk):     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(400,200)
        self.state('zoom')
        # creating a container        
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
        self.nodelist=[]
        self.list=[]
        self.edgeList=[]
        self.goalslist=[]
        self.mycanvas=Canvas(self,bg='light grey')
        self.start_node=[]
        self.searchType= []
        self.alphabet_list=[]
        self.transitions_list=[]
        # iterating through a tuple consisting
        # of the different page layouts
        #edge flag =2 at first before choosing edges type either directed or undirected
        # edge flag = 0 if we are workin wirth undirected graph
        #edgeflag = 1 if we are working wirth directed graph
        self.edgeflag=2
        for F in (StartPage,Page11):
  
            frame = F(container, self,self.list,self.mycanvas,self.edgeList,self.nodelist,self.goalslist,self.edgeflag,self.start_node,self.searchType,self.alphabet_list,self.transitions_list)
        
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame  
            frame.grid(row = 0, column = 0, sticky ="nsew")
        frame=graphResut(container,self,self.mycanvas,self.nodelist,self.start_node,self.searchType,self.alphabet_list,self.transitions_list)
        self.frames[graphResut]=frame
        frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(StartPage)
  
   
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
app = tkinterApp()
app.mainloop()