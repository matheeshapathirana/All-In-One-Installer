import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("No Updates")
        #setting window size
        width=597
        height=363
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg='#1d1c1c')

        GLabel_464=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=38)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#FFFFFF"
        GLabel_464["bg"] = "#1d1c1c"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "No Updates"
        GLabel_464.place(x=50,y=20,width=505,height=122)

        GButton_628=tk.Button(root)
        GButton_628["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_628["font"] = ft
        GButton_628["fg"] = "#000000"
        GButton_628["justify"] = "center"
        GButton_628["text"] = "Close"
        GButton_628.place(x=170,y=200,width=251,height=90)
        GButton_628["command"] = self.GButton_628_command

    @staticmethod
    def GButton_628_command():
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
