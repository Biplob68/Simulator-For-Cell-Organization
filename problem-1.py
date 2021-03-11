from tkinter import *
from tkinter.ttk import Radiobutton
import math



class MyWindow:
    def __init__(self, win):
        self.lbl0=Label(win, text='A Simulator for Cell Organization',fg='#FF0A0A', font="Georgia 20")
        self.lbl1=Label(win, text='Area size to Cover :', fg='black', background='#A3CEDC', font="Georgia 15")
        self.lbl2=Label(win, text='Required cell type :', fg='Black', background='#A3CEDC', font=("Georgia", 15))
        self.lbl3=Label(win, text='Radius of each cell :', fg='Black', background='#A3CEDC', font=("Georgia", 15))
        self.lbl4=Label(win, text='Total number of frequencies :', fg='Black', background='#A3CEDC', font=("Georgia", 15))
        self.lbl5=Label(win, text='Frequency reuse factor :', fg='Black', background='#A3CEDC', font=("Georgia", 15))



        #Define total Entry
        self.t1=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.t4=Entry(bd=3)
        self.t5=Entry(bd=3)
        self.t6=Entry(bd=3)
        self.t7=Entry(bd=3)
        self.t8=Entry(bd=3)
        self.t9=Entry(bd=3)


        #Define Entry and Label Position in window
        self.lbl0.place(x=150, y=3)

        self.lbl1.place(x=142, y=50)
        self.t1.place(x=325, y=55)

        self.lbl2.place(x=140, y=100)

        self.lbl3.place(x=133, y=150)
        self.t3.place(x=325, y=155)

        self.lbl4.place(x=47, y=200)
        self.t4.place(x=325, y=205)

        self.lbl5.place(x=97, y=250)
        self.t5.place(x=325, y=255)


     
        #Button to find output

        self.b1=Button(win, text='Total Required cell ', command=self.total_cell, bg ='#6E6EFF', font=("Georgia", 11))
        self.b2=Button(win, text='Channel Per Cell', bg ='#6E6EFF', font=("Georgia", 11))
        self.b2.bind('<Button-1>', self.channel_per_cell, )

        self.b3=Button(win, text='Total Channel Capacity', bg ='#6E6EFF', font=("Georgia", 11))
        self.b3.bind('<Button-1>', self.cahnnel_capacity)

        self.b4=Button(win, text='Total Possible Call', bg ='#6E6EFF', font=("Georgia", 11))
        self.b4.bind('<Button-1>', self.possible_call)

        self.b1.place(x=50, y=300)
        self.b2.place(x=205, y=300)
        self.b3.place(x=340, y=300)
        self.b4.place(x=520, y=300)

        self.t6.place(x=50, y=350)
        self.t7.place(x=205, y=350)
        self.t8.place(x=350, y=350)
        self.t9.place(x=520, y=350)
       

        
    #Funcction for result

    def total_cell(self):
        self.t6.delete(0, 'end')
        A=float(self.t1.get())     #Total area to cover
        R=float(self.t3.get()) 
        A1=(2.6*R*R)               #Area for one cell
        Total_Cell=math.floor(A/A1)    
        self.t6.insert(END, int(Total_Cell))



    def channel_per_cell(self, event):
        self.t7.delete(0, 'end')
        Total_Channel=float(self.t4.get())
        Reuse_factor=float(self.t5.get())
        Channel_Per_Cell=(Total_Channel/Reuse_factor)
        self.t7.insert(END, int(Channel_Per_Cell))
    
    
    def cahnnel_capacity(self,event):
        self.t8.delete(0, 'end')
        Total_Cell=int(self.t6.get())
        Channel_Per_Cell=int(self.t7.get())
        Total_Channel_Capacity=(Total_Cell*Channel_Per_Cell)
        self.t8.insert(END, str(Total_Channel_Capacity))
    
    def possible_call(self,event):
        self.t9.delete(0, 'end')
        Total_Cell=int(self.t6.get())
        Channel_Per_Cell=int(self.t7.get())
        Total_Possible_Call=(Total_Cell*Channel_Per_Cell)
        self.t9.insert(END, str(Total_Possible_Call))
    

#Define window
 
window=Tk()
mywin=MyWindow(window)


v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="Microcell", variable=v0,value=1)
r2=Radiobutton(window, text="Macrocell", variable=v0,value=2)
r1.place(x=327,y=105)
r2.place(x=405, y=105)
                


window.title('Mobile and Wireless Communication project')
window.configure(background='#A3CEDC')
window.geometry("700x600+10+10")
window.mainloop()