#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     03/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Tkinter import *
class App:
    def __init___(self,master):
        frame = Frame(master)
        frame.pack()

        self.hello = Button(frame,text='hello',command=self.hello)
        self.hello.pack(side=LEFT)
        self.quit = Button(frame,text='Quit',fg='red',command=frame.quit)
        self.quit.pack(side=RIGHT)

    def hello(self):
        print ('Hello Python!')

root = Tk()
root.wm_title('Hello')
root.wm_minsize(200,200)
##app = App(root)
root.mainloop()

