from Tkinter import *
import random

root = Tk()
root.title("First Website")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
 
# Create a Tkinter variable

argg = ''
argg = ''
argg2=''
argg3=''
argg4= ''
myvar = IntVar()
myvar1 = IntVar()
myvar2 = IntVar()
myvar3 = IntVar()
myvar4  = IntVar()

'''def mywarWritten(*args):
    print "mywarWritten",myvar.get()

myvar.trace("w", mywarWritten)'''

def path():
    argg = myvar.get()
    argg4 = myvar4.get()
    argg1 = myvar1.get()
    argg2 = myvar2.get()
    argg3 = myvar3.get()
    f = open("entries.txt", "w+")
    a = range(int(argg),int(argg1))
    b = range(int(argg2),int(argg3))
    
    for each in range(0,int(argg4)):
        h= random.choice(a)
        w= random.choice(b)
        f.write(str(h)+ ",")
        f.write(str(w)+ "\n")
    
    
    f.close()
Label(mainframe,text='Height range from').grid(row=0,column=0)
Entry(mainframe,width=23,textvariable = myvar).grid(row=0,column=1)
Label(mainframe,text='to').grid(row=0,column=2)
Entry(mainframe,width=23,textvariable = myvar1).grid(row=0,column=2)
Label(mainframe,text='Weight range from').grid(row=1,column=0)
Entry(mainframe,width=23,textvariable = myvar2).grid(row=1,column=1)
Label(mainframe,text='to').grid(row=1,column=2)
Entry(mainframe,width=23,textvariable = myvar3).grid(row=1,column=2)
Label(mainframe,text='Number of values needed').grid(row=2,column=0)
Entry(mainframe,width=23,textvariable = myvar4).grid(row=2,column=1)


m=Button(mainframe,text='submit',command=path).grid(row=3,column=2)



root.mainloop()
