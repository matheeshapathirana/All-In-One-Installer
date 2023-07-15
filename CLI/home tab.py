import os
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("All-In-One Installer- Home")
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
        GButton_52["bg"] = "#000000"
        ft = tkFont.Font(family='sego ui',size=28)
        GButton_52["font"] = ft
        GButton_52["fg"] = "#FFFFFF"
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

        GButton_676=tk.Button(root)
        GButton_676["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_676["font"] = ft
        GButton_676["fg"] = "#000000"
        GButton_676["justify"] = "center"
        GButton_676["text"] = "Install Minecraft"
        GButton_676.place(x=70,y=220,width=180,height=65)
        GButton_676["command"] = self.GButton_676_command

        GLabel_176=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=28)
        GLabel_176["font"] = ft
        GLabel_176["fg"] = "#FFFFFF"
        GLabel_176["bg"] = "#1d1c1c"
        GLabel_176["justify"] = "center"
        GLabel_176["text"] = "Top Apps"
        GLabel_176.place(x=0,y=160,width=237,height=40)

        GButton_205=tk.Button(root)
        GButton_205["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_205["font"] = ft
        GButton_205["fg"] = "#000000"
        GButton_205["justify"] = "center"
        GButton_205["text"] = "Install Valorant"
        GButton_205.place(x=290,y=220,width=180,height=65)
        GButton_205["command"] = self.GButton_205_command

        GButton_59=tk.Button(root)
        GButton_59["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_59["font"] = ft
        GButton_59["fg"] = "#000000"
        GButton_59["justify"] = "center"
        GButton_59["text"] = "Install Zoom"
        GButton_59.place(x=510,y=220,width=180,height=65)
        GButton_59["command"] = self.GButton_59_command

        GButton_516=tk.Button(root)
        GButton_516["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_516["font"] = ft
        GButton_516["fg"] = "#000000"
        GButton_516["justify"] = "center"
        GButton_516["text"] = "Install Spotify"
        GButton_516.place(x=740,y=220,width=180,height=65)
        GButton_516["command"] = self.GButton_516_command

        GButton_183=tk.Button(root)
        GButton_183["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=15)
        GButton_183["font"] = ft
        GButton_183["fg"] = "#000000"
        GButton_183["justify"] = "center"
        GButton_183["text"] = "Install Lunar Client"
        GButton_183.place(x=70,y=330,width=180,height=65)
        GButton_183["command"] = self.GButton_183_command

        GButton_486=tk.Button(root)
        GButton_486["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_486["font"] = ft
        GButton_486["fg"] = "#000000"
        GButton_486["justify"] = "center"
        GButton_486["text"] = "Install Python"
        GButton_486.place(x=290,y=330,width=180,height=65)
        GButton_486["command"] = self.GButton_486_command

        GButton_261=tk.Button(root)
        GButton_261["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_261["font"] = ft
        GButton_261["fg"] = "#000000"
        GButton_261["justify"] = "center"
        GButton_261["text"] = "Install Steam"
        GButton_261.place(x=510,y=330,width=180,height=65)
        GButton_261["command"] = self.GButton_261_command

        GButton_699=tk.Button(root)
        GButton_699["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=13)
        GButton_699["font"] = ft
        GButton_699["fg"] = "#000000"
        GButton_699["justify"] = "center"
        GButton_699["text"] = "Install Google Chrome"
        GButton_699.place(x=740,y=330,width=180,height=65)
        GButton_699["command"] = self.GButton_699_command

    @staticmethod
    def GButton_871_command():
        root.destroy()


    @staticmethod
    def GButton_264_command():
        print("update")


    @staticmethod
    def GButton_52_command():
        print("home")


    @staticmethod
    def GButton_405_command():
        print("US")


    @staticmethod
    def GButton_362_command():
        print("ent")


    @staticmethod
    def GButton_676_command():
        os.system('cmd /k "winget install --id=Mojang.MinecraftLauncher  -e"')


    @staticmethod
    def GButton_205_command():
        os.system('cmd /k "winget install --id=RiotGames.Valorant.AP  -e"')


    @staticmethod
    def GButton_59_command():
        os.system('cmd /k "winget install --id=Zoom.Zoom  -e"')


    @staticmethod
    def GButton_516_command():
        os.system('cmd /k "winget install --id=Spotify.Spotify  -e"')


    @staticmethod
    def GButton_183_command():
        os.system('cmd /k "winget install --id=Moonsworth.LunarClient  -e"')


    @staticmethod
    def GButton_486_command():
        os.system('cmd /k "winget install --id=Python.Python.3  -e"')


    @staticmethod
    def GButton_261_command():
        os.system('cmd /k "winget install --id=Valve.Steam  -e"')


    @staticmethod
    def GButton_699_command():
        os.system('cmd /k "winget install --id=Google.Chrome  -e"')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
