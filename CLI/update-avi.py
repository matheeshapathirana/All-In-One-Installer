import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=597
        height=363
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg='#1d1c1c')

        GLabel_999=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=35)
        GLabel_999["font"] = ft
        GLabel_999["fg"] = "#FFFFFF"
        GLabel_999["bg"] = "#1d1c1c"
        GLabel_999["justify"] = "center"
        GLabel_999["text"] = "New Updates Available"
        GLabel_999.place(x=50,y=20,width=505,height=122)

        GButton_628=tk.Button(root)
        GButton_628["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_628["font"] = ft
        GButton_628["fg"] = "#000000"
        GButton_628["justify"] = "center"
        GButton_628["text"] = "Update"
        GButton_628.place(x=80,y=240,width=180,height=60)
        GButton_628["command"] = self.GButton_628_command

        GButton_523=tk.Button(root)
        GButton_523["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_523["font"] = ft
        GButton_523["fg"] = "#000000"
        GButton_523["justify"] = "center"
        GButton_523["text"] = "Close"
        GButton_523.place(x=320,y=240,width=180,height=60)
        GButton_523["command"] = self.GButton_523_command

    @staticmethod
    def GButton_628_command():
        print("updateing")


    @staticmethod
    def GButton_523_command():
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
