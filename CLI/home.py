import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("All-In-One Installer")
        #setting window size
        width=988
        height=896
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg='#1d1c1c')

        GButton_871=tk.Button(root)
        GButton_871["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_871["font"] = ft
        GButton_871["fg"] = "#000000"
        GButton_871["justify"] = "center"
        GButton_871["text"] = "Exit"
        GButton_871.place(x=30,y=820,width=120,height=50)
        GButton_871["command"] = self.GButton_871_command

        GButton_264=tk.Button(root)
        GButton_264["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_264["font"] = ft
        GButton_264["fg"] = "#000000"
        GButton_264["justify"] = "center"
        GButton_264["text"] = "Update"
        GButton_264.place(x=170,y=820,width=120,height=50)
        GButton_264["command"] = self.GButton_264_command

        GButton_52=tk.Button(root)
        GButton_52["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_52["font"] = ft
        GButton_52["fg"] = "#000000"
        GButton_52["justify"] = "center"
        GButton_52["text"] = "Home"
        GButton_52.place(x=50,y=60,width=200,height=50)
        GButton_52["command"] = self.GButton_52_command

        GButton_405=tk.Button(root)
        GButton_405["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_405["font"] = ft
        GButton_405["fg"] = "#000000"
        GButton_405["justify"] = "center"
        GButton_405["text"] = "Utility Softwares"
        GButton_405.place(x=300,y=60,width=280,height=50)
        GButton_405["command"] = self.GButton_405_command

        GButton_362=tk.Button(root)
        GButton_362["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_362["font"] = ft
        GButton_362["fg"] = "#000000"
        GButton_362["justify"] = "center"
        GButton_362["text"] = "Entertainment"
        GButton_362.place(x=640,y=60,width=274,height=50)
        GButton_362["command"] = self.GButton_362_command

    @staticmethod
    def GButton_871_command():
        root.destroy()


    @staticmethod
    def GButton_264_command():
        print("command")


    @staticmethod
    def GButton_52_command():
        print("command")


    @staticmethod
    def GButton_405_command():
        print('US installer')


    @staticmethod
    def GButton_362_command():
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
