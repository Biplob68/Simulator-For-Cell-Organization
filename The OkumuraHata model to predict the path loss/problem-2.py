from tkinter import *
from tkinter.ttk import Radiobutton
import math






class MyWindow:
    def __init__(self, win):
        self.lbl0=Label(win, text='Okumara/Hata Model to Predict Path Loss', bd=5, fg='red', font=("Georgia", 17))
        self.lbl1=Label(win, text='Carrier frequency(150-1500 in MHz): ',bg='#A3CEDC', fg='black', font=("Georgia", 14))
        self.lbl2=Label(win, text='Height of transmitter antenna (30-300 in meter): ',bg='#A3CEDC', fg='Black', font=("Georgia", 14))
        self.lbl3=Label(win, text='Height of receiver antenna (1 - 10 in meter): ', bg ='#A3CEDC', bd=5, fg='Black', font=("Georgia", 14))
        self.lbl4=Label(win, text='Propagation distance (1-20 in km):', fg='Black',bg ='#A3CEDC', bd=5, font=("Georgia", 14))
        self.lbl5=Label(win, text='Value of the type of city (1 - Small/Medium, 2-Large):',bg ='#A3CEDC', bd=5, fg='Black', font=("Georgia", 14))
        self.lbl6=Label(win, text='Value of the type of area(1-Urban,2-Sub urban,3-Open area):',bg ='#A3CEDC', bd=5, fg='Black', font=("Georgia", 13))
        self.lbl7=Label(win, text='RESULT', bg ='#A3CEDC',  fg='Blue', font=("Georgia", 14))

 
        #Entry field

        self.t1=Entry(bd=3, fg='black', font=("Georgia",10))
        self.t2=Entry(bd=3, fg='black', font=("Georgia",10))
        self.t3=Entry(bd=3, fg='black', font=("Georgia",10))
        self.t4=Entry(bd=3, fg='black', font=("Georgia",10))
        self.t5=Entry(bd=3, fg='black', font=("Georgia",10))
        self.t6=Entry(bd=3, fg='black', font=("Georgia",10))
        self.t7=Entry(bd=3, fg='black', font=("arial",10))
        

        #Entry field and label position 
        self.lbl0.place(x=200, y=5)

        self.lbl1.place(x=170, y=50)
        self.t1.place(x=510, y=55)

        self.lbl2.place(x=63, y=100)
        self.t2.place(x=510, y=105)

        self.lbl3.place(x=110, y=150)
        self.t3.place(x=510, y=155)

        self.lbl4.place(x=182, y=200)
        self.t4.place(x=510, y=205)

        self.lbl5.place(x=25, y=250)
        self.t5.place(x=510, y=255)

        self.lbl6.place(x=20, y=300)
        self.t6.place(x=510, y=305)


        
     
        #create button
        self.b1=Button(win, text='PATH LOSS', command=self.Predicated_Path_Loss, bg ='#6E6EFF', fg='black', font=("Georgia", 15))
        self.b1.place(x=350, y=350)
        
        self.lbl7.place(x=260, y=400)
        self.t7.place(x=365, y=404)

        
        #Main function to predict path loss

    def Predicated_Path_Loss(self):
        self.t7.delete(0, 'end')
        carrier_frq=float(self.t1.get())
        height_transmitter=float(self.t2.get())
        height_receiver=float(self.t3.get())
        link_distance=float(self.t4.get())
        city=float(self.t5.get())
        area=float(self.t6.get())

        corr_factor = 0.0
   
        path_loss = 0.0
       
        if city == 1:
            corr_factor = (0.8 + ((1.1 * math.log10(carrier_frq) - 0.7)*height_receiver) - (1.56 * math.log10(carrier_frq)))

        else:
            if (carrier_frq >= 150) and (carrier_frq <= 200):
                corr_factor = (8.29 * (math.pow(math.log10(1.54 * height_receiver), 2))) - 1.1
            else:
                corr_factor = (3.2 * (math.pow(math.log10(11.75 * height_receiver), 2))) - 4.97

        path_loss = 69.55 + (26.16 * math.log10(carrier_frq)) - (13.82 * math.log10(height_transmitter)) - corr_factor + ((44.9 - (6.55 * math.log10(height_transmitter))) * math.log10(link_distance))        
        

        diff_loss = 0.0
        if area == 2:
            diff_loss = 2 * math.pow(math.log10((carrier_frq/28)), 2) + 5.4
        elif area == 3:
            diff_loss = 4.78 * math.pow(math.log10(carrier_frq), 2) + 18.733 * math.log10(carrier_frq) + 40.94

        path_loss -= diff_loss

       
        self.t7.insert(END, str(path_loss))


#Define window 
window=Tk()
mywin=MyWindow(window)



window.title('Mobile and Wireless Communication project')
window.configure(background='#A3CEDC')
window.geometry("800x600+10+10")



window.mainloop()