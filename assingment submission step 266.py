import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='darkgray')

        self.textFName = StringVar()

        self.lblFName = Label(self.master, text='First Name', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master, text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, heigh=2, command=self.defaultEntry)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE)
        
        self.btnCancel = Button(self.master, text="Cancel", width=10, heigh=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        
    def cancel(self):
        self.master.destroy()



    def defaultEntry(self):
        fn = self.txtFName.get()
        sameText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("user_customized.html", "w")
        htmlFormat = "<html>\n<body>\n<p>" + fn + "<p>\n</body>\n</html>"
        htmlFile.write(htmlFormat)
        htmlFile.close()
        webbrowser.open_new_tab("user_customized.html")


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
