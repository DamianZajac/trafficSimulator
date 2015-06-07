from Tkinter import *
from PIL import Image, ImageTk


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Traffic simulator")
        self.pack(fill=BOTH, expand=1)

        startButton = Button(self, text="Start", command=self.start)
        startButton.place(x=100, y=0)

        stopButton = Button(self, text="Stop", command=self.stop)
        stopButton.place(x=150, y=0)

        self.v = IntVar()

        labelText2 = StringVar()
        labelText2.set("Choose turn:")
        label2 = Label(self, textvariable=labelText2)
        label2.pack(anchor=W)

        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.CheckVar3 = IntVar()
        self.CheckVar4 = IntVar()
        self.CheckVar5 = IntVar()
        C1Left = Checkbutton(self, text = "left", variable = self.CheckVar1, onvalue = 1, offvalue = 0, command=self.checked1)
        C2Right = Checkbutton(self, text = "right", variable = self.CheckVar2, onvalue = 1, offvalue = 0, command=self.checked2)
        C3Up = Checkbutton(self, text = "up", variable = self.CheckVar3, onvalue = 1, offvalue = 0, command=self.checked3)
        C4Down = Checkbutton(self, text = "down", variable = self.CheckVar4, onvalue = 1, offvalue = 0, command=self.checked4)
        C5End = Checkbutton(self, text = "end", variable = self.CheckVar5, onvalue = 1, offvalue = 0, command=self.checked5)
        C1Left.pack(anchor=W)
        C2Right.pack(anchor=W)
        C3Up.pack(anchor=W)
        C4Down.pack(anchor=W)
        C5End.pack(anchor=W)

        global X
        global Y
        X = 1280/2
        Y = 720/2
        plusButtonN = Button(self, text="+", command=self.up)
        plusButtonN.place(anchor=N, x=1280/2)

        plusButtonW = Button(self, text="+", command=self.left)
        plusButtonW.place(anchor=W, y=720/2)

        plusButtonE = Button(self, text="+", command=self.right)
        plusButtonE.place(anchor=E, x=1280, y=720/2)

        plusButtonS = Button(self, text="+", command=self.down)
        plusButtonS.place(anchor=S, x=1280/2, y=720)


        #image test
        Project_path = ''
        load = Image.open('up.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(anchor=N, x=X, y=Y)

    def selected(self):
        return self.v.get()

    def checked1(self):
        return self.CheckVar1.get()

    def checked2(self):
        return self.CheckVar2.get()

    def checked3(self):
        return self.CheckVar3.get()

    def checked4(self):
        return self.CheckVar4.get()

    def checked5(self):
        return self.CheckVar5.get()

    def roadPicker(self):
        return

    def start(self):
        return

    def stop(self):
        return

    def up(self):
        if(self.CheckVar5.get()==1):
            load = Image.open('down.png')
        elif(self.CheckVar1.get()==1):
            load = Image.open('down_left.png')
        elif(self.CheckVar2.get()==1):
            load = Image.open('right_down.png')
        elif(self.CheckVar3.get()==1):
            load = Image.open('up_down.png')
        if((self.CheckVar1.get()==1) and (self.CheckVar3.get()==1) and (self.CheckVar2.get()==1)):
            load = Image.open('up_right_down_left.png')
        elif(self.CheckVar2.get()==1 and self.CheckVar3.get()==1):
            load = Image.open('up_right_down.png')
        elif(self.CheckVar1.get()==1 and self.CheckVar3.get()==1):
            load = Image.open('up_down_left.png')
        elif(self.CheckVar1.get()==1 and self.CheckVar2.get()==1):
            load = Image.open('right_down_left.png')
        if (Y>100):
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(anchor=N, x=X, y=Y-100)
            global Y
            Y -= 100
        return

    def left(self):
        if(self.CheckVar5.get()==1):
            load = Image.open('right.png')
        elif(self.CheckVar1.get()==1):
            load = Image.open('right_left.png')
        elif(self.CheckVar4.get()==1):
            load = Image.open('right_down.png')
        elif(self.CheckVar3.get()==1):
            load = Image.open('up_right.png')
        if((self.CheckVar1.get()==1) and (self.CheckVar3.get()==1) and (self.CheckVar4.get()==1)):
            load = Image.open('up_right_down_left.png')
        elif(self.CheckVar4.get()==1 and self.CheckVar3.get()==1):
            load = Image.open('up_right_down.png')
        elif(self.CheckVar1.get()==1 and self.CheckVar3.get()==1):
            load = Image.open('up_right_left.png')
        elif(self.CheckVar1.get()==1 and self.CheckVar4.get()==1):
            load = Image.open('right_down_left.png')
        if X>200:
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(anchor=N, x=X-100, y=Y)
            global X
            X -= 100
        return

    def right(self):
        if(self.CheckVar5.get()==1):
            load = Image.open('left.png')
        elif(self.CheckVar4.get()==1):
            load = Image.open('down_left.png')
        elif(self.CheckVar2.get()==1):
            load = Image.open('right_left.png')
        elif(self.CheckVar3.get()==1):
            load = Image.open('up_left.png')
        if((self.CheckVar4.get()==1) and (self.CheckVar3.get()==1) and (self.CheckVar2.get()==1)):
            load = Image.open('up_right_down_left.png')
        elif(self.CheckVar2.get()==1 and self.CheckVar3.get()==1):
            load = Image.open('up_right_left.png')
        elif(self.CheckVar4.get()==1 and self.CheckVar3.get()==1):
            load = Image.open('up_down_left.png')
        elif(self.CheckVar4.get()==1 and self.CheckVar2.get()==1):
            load = Image.open('right_down_left.png')
        if X<1100:
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(anchor=N, x=X+100, y=Y)
            global X
            X += 100
        return

    def down(self):
        if(self.CheckVar5.get()==1):
            load = Image.open('up.png')
        elif(self.CheckVar1.get()==1):
            load = Image.open('up_left.png')
        elif(self.CheckVar2.get()==1):
            load = Image.open('up_right.png')
        elif(self.CheckVar4.get()==1):
            load = Image.open('up_down.png')
        if((self.CheckVar1.get()==1) and (self.CheckVar4.get()==1) and (self.CheckVar2.get()==1)):
            load = Image.open('up_right_down_left.png')
        elif(self.CheckVar2.get()==1 and self.CheckVar4.get()==1):
            load = Image.open('up_right_down.png')
        elif(self.CheckVar1.get()==1 and self.CheckVar4.get()==1):
            load = Image.open('up_down_left.png')
        elif(self.CheckVar1.get()==1 and self.CheckVar2.get()==1):
            load = Image.open('up_right_left.png')
        if Y<500:
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(anchor=N, x=X, y=Y+100)
            global Y
            Y += 100
        return


root = Tk()
root.geometry("1280x720")
app = Window(root)
root.mainloop()
