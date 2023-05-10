from tkinter import *
class DrawLineApp () :
    def __init__(self,the_frame,row,column):
        self.mycanvas=Canvas(the_frame,bg='light grey')
        self.mycanvas.grid(row=row,column=column,padx=20,rowspan=4,columnspan=1, sticky='ns')
      
        self.mycanvas.bind('<Button-1>',self.draw_line)
        self.click_number=0
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0
    def draw_line(self,event):
        if self.click_number==0:
            self.x1=event.x
            self.y1=event.y
            self.click_number=1
        else:
            self.x2=event.x
            self.y2=event.y
            self.mycanvas.create_line(self.x1,self.y1,self.x2,self.y2,fill='black',width=1)
            self.click_number=0
""""
my_window=Tk()
my_window.rowconfigure(0,weight=1)
my_window.columnconfigure(0,weight=1)
the_frame=Frame(my_window)
the_frame.grid(row=0,column=0,sticky='nsew')
the_frame_title=Label(the_frame,text='the_frame',bg='gray')
#the_frame_title.pack(side = "top", fill = "both", expand = True)
my_draw_line=DrawLineApp(the_frame,row=0,column=0)
my_window.mainloop()
"""