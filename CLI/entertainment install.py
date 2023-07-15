import os
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("All-In-One Installer - Entertainment")
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

        GButton_676=tk.Button(root)
        GButton_676["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_676["font"] = ft
        GButton_676["fg"] = "#000000"
        GButton_676["justify"] = "center"
        GButton_676["text"] = "Install"
        GButton_676.place(x=70,y=220,width=150,height=40)
        GButton_676["command"] = self.GButton_676_command

        GLabel_176=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_176["font"] = ft
        GLabel_176["fg"] = "#FFFFFF"
        GLabel_176["bg"] = "#1d1c1c"
        GLabel_176["justify"] = "center"
        GLabel_176["text"] = "Minecraft Launcher"
        GLabel_176.place(x=30,y=180,width=237,height=30)

        GLabel_4=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_4["font"] = ft
        GLabel_4["fg"] = "#FFFFFF"
        GLabel_4["bg"] = "#1d1c1c"
        GLabel_4["justify"] = "center"
        GLabel_4["text"] = "Steam"
        GLabel_4.place(x=280,y=180,width=170,height=35)

        GButton_205=tk.Button(root)
        GButton_205["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_205["font"] = ft
        GButton_205["fg"] = "#000000"
        GButton_205["justify"] = "center"
        GButton_205["text"] = "Install"
        GButton_205.place(x=290,y=220,width=150,height=40)
        GButton_205["command"] = self.GButton_205_command

        GLabel_68=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_68["font"] = ft
        GLabel_68["fg"] = "#FFFFFF"
        GLabel_68["bg"] = "#1d1c1c"
        GLabel_68["justify"] = "center"
        GLabel_68["text"] = "Smart Game Booster"
        GLabel_68.place(x=470,y=180,width=242,height=30)

        GButton_59=tk.Button(root)
        GButton_59["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_59["font"] = ft
        GButton_59["fg"] = "#000000"
        GButton_59["justify"] = "center"
        GButton_59["text"] = "Install"
        GButton_59.place(x=510,y=220,width=150,height=40)
        GButton_59["command"] = self.GButton_59_command

        GLabel_585=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_585["font"] = ft
        GLabel_585["fg"] = "#FFFFFF"
        GLabel_585["bg"] = "#1d1c1c"
        GLabel_585["justify"] = "center"
        GLabel_585["text"] = "Epic Game"
        GLabel_585.place(x=720,y=180,width=176,height=30)

        GButton_516=tk.Button(root)
        GButton_516["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_516["font"] = ft
        GButton_516["fg"] = "#000000"
        GButton_516["justify"] = "center"
        GButton_516["text"] = "Install"
        GButton_516.place(x=740,y=220,width=150,height=40)
        GButton_516["command"] = self.GButton_516_command

        GLabel_543=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_543["font"] = ft
        GLabel_543["fg"] = "#FFFFFF"
        GLabel_543["bg"] = "#1d1c1c"
        GLabel_543["justify"] = "center"
        GLabel_543["text"] = "PvPLounge"
        GLabel_543.place(x=30,y=290,width=261,height=30)

        GButton_183=tk.Button(root)
        GButton_183["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_183["font"] = ft
        GButton_183["fg"] = "#000000"
        GButton_183["justify"] = "center"
        GButton_183["text"] = "Install"
        GButton_183.place(x=70,y=330,width=150,height=40)
        GButton_183["command"] = self.GButton_183_command

        GLabel_227=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_227["font"] = ft
        GLabel_227["fg"] = "#FFFFFF"
        GLabel_227["bg"] = "#1d1c1c"
        GLabel_227["justify"] = "center"
        GLabel_227["text"] = "Playnight"
        GLabel_227.place(x=300,y=290,width=144,height=30)

        GButton_486=tk.Button(root)
        GButton_486["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_486["font"] = ft
        GButton_486["fg"] = "#000000"
        GButton_486["justify"] = "center"
        GButton_486["text"] = "Install"
        GButton_486.place(x=290,y=330,width=150,height=40)
        GButton_486["command"] = self.GButton_486_command

        GButton_261=tk.Button(root)
        GButton_261["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_261["font"] = ft
        GButton_261["fg"] = "#000000"
        GButton_261["justify"] = "center"
        GButton_261["text"] = "Install"
        GButton_261.place(x=510,y=330,width=150,height=40)
        GButton_261["command"] = self.GButton_261_command

        GLabel_772=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_772["font"] = ft
        GLabel_772["fg"] = "#FFFFFF"
        GLabel_772["bg"] = "#1d1c1c"
        GLabel_772["justify"] = "center"
        GLabel_772["text"] = "Valorant"
        GLabel_772.place(x=500,y=290,width=168,height=30)

        GLabel_773=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_773["font"] = ft
        GLabel_773["fg"] = "#FFFFFF"
        GLabel_773["bg"] = "#1d1c1c"
        GLabel_773["justify"] = "center"
        GLabel_773["text"] = "BlueStacks"
        GLabel_773.place(x=750,y=290,width=155,height=30)

        GButton_699=tk.Button(root)
        GButton_699["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_699["font"] = ft
        GButton_699["fg"] = "#000000"
        GButton_699["justify"] = "center"
        GButton_699["text"] = "Install"
        GButton_699.place(x=740,y=330,width=150,height=40)
        GButton_699["command"] = self.GButton_699_command

        GLabel_637=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_637["font"] = ft
        GLabel_637["fg"] = "#FFFFFF"
        GLabel_637["bg"] = "#1d1c1c"
        GLabel_637["justify"] = "center"
        GLabel_637["text"] = "Ubisoft Connect"
        GLabel_637.place(x=50,y=400,width=211,height=30)

        GButton_290=tk.Button(root)
        GButton_290["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_290["font"] = ft
        GButton_290["fg"] = "#000000"
        GButton_290["justify"] = "center"
        GButton_290["text"] = "Install"
        GButton_290.place(x=70,y=440,width=150,height=40)
        GButton_290["command"] = self.GButton_290_command

        GButton_647=tk.Button(root)
        GButton_647["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_647["font"] = ft
        GButton_647["fg"] = "#000000"
        GButton_647["justify"] = "center"
        GButton_647["text"] = "Install"
        GButton_647.place(x=290,y=440,width=150,height=40)
        GButton_647["command"] = self.GButton_647_command

        GLabel_798=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_798["font"] = ft
        GLabel_798["fg"] = "#FFFFFF"
        GLabel_798["bg"] = "#1d1c1c"
        GLabel_798["justify"] = "center"
        GLabel_798["text"] = "Plex"
        GLabel_798.place(x=310,y=400,width=106,height=30)

        GLabel_746=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_746["font"] = ft
        GLabel_746["fg"] = "#FFFFFF"
        GLabel_746["bg"] = "#1d1c1c"
        GLabel_746["justify"] = "center"
        GLabel_746["text"] = "Gamecaster"
        GLabel_746.place(x=500,y=400,width=187,height=30)

        GButton_322=tk.Button(root)
        GButton_322["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_322["font"] = ft
        GButton_322["fg"] = "#000000"
        GButton_322["justify"] = "center"
        GButton_322["text"] = "Install"
        GButton_322.place(x=510,y=440,width=150,height=40)
        GButton_322["command"] = self.GButton_322_command

        GLabel_524=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_524["font"] = ft
        GLabel_524["fg"] = "#FFFFFF"
        GLabel_524["bg"] = "#1d1c1c"
        GLabel_524["justify"] = "center"
        GLabel_524["text"] = "Blitz"
        GLabel_524.place(x=750,y=400,width=120,height=30)

        GButton_735=tk.Button(root)
        GButton_735["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_735["font"] = ft
        GButton_735["fg"] = "#000000"
        GButton_735["justify"] = "center"
        GButton_735["text"] = "Install"
        GButton_735.place(x=740,y=440,width=150,height=40)
        GButton_735["command"] = self.GButton_735_command

        GLabel_750=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_750["font"] = ft
        GLabel_750["fg"] = "#FFFFFF"
        GLabel_750["bg"] = "#1d1c1c"
        GLabel_750["justify"] = "center"
        GLabel_750["text"] = "CORSAIR "
        GLabel_750.place(x=90,y=510,width=112,height=31)

        GButton_285=tk.Button(root)
        GButton_285["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_285["font"] = ft
        GButton_285["fg"] = "#000000"
        GButton_285["justify"] = "center"
        GButton_285["text"] = "install"
        GButton_285.place(x=70,y=550,width=150,height=40)
        GButton_285["command"] = self.GButton_285_command

        GLabel_866=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_866["font"] = ft
        GLabel_866["fg"] = "#FFFFFF"
        GLabel_866["bg"] = "#1d1c1c"
        GLabel_866["justify"] = "center"
        GLabel_866["text"] = "EA app"
        GLabel_866.place(x=310,y=510,width=106,height=30)

        GLabel_195=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_195["font"] = ft
        GLabel_195["fg"] = "#FFFFFF"
        GLabel_195["bg"] = "#1d1c1c"
        GLabel_195["justify"] = "center"
        GLabel_195["text"] = "Lunar Client"
        GLabel_195.place(x=510,y=510,width=160,height=30)

        GLabel_485=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_485["font"] = ft
        GLabel_485["fg"] = "#FFFFFF"
        GLabel_485["bg"] = "#1d1c1c"
        GLabel_485["justify"] = "center"
        GLabel_485["text"] = "Badlion Client"
        GLabel_485.place(x=740,y=510,width=154,height=30)

        GButton_527=tk.Button(root)
        GButton_527["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_527["font"] = ft
        GButton_527["fg"] = "#000000"
        GButton_527["justify"] = "center"
        GButton_527["text"] = "Install"
        GButton_527.place(x=290,y=550,width=150,height=40)
        GButton_527["command"] = self.GButton_527_command

        GButton_392=tk.Button(root)
        GButton_392["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_392["font"] = ft
        GButton_392["fg"] = "#000000"
        GButton_392["justify"] = "center"
        GButton_392["text"] = "Install"
        GButton_392.place(x=510,y=550,width=150,height=40)
        GButton_392["command"] = self.GButton_392_command

        GButton_278=tk.Button(root)
        GButton_278["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_278["font"] = ft
        GButton_278["fg"] = "#000000"
        GButton_278["justify"] = "center"
        GButton_278["text"] = "install"
        GButton_278.place(x=740,y=550,width=150,height=40)
        GButton_278["command"] = self.GButton_278_command

        GLabel_87=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_87["font"] = ft
        GLabel_87["fg"] = "#FFFFFF"
        GLabel_87["bg"] = "#1d1c1c"
        GLabel_87["justify"] = "center"
        GLabel_87["text"] = "Deezer"
        GLabel_87.place(x=80,y=620,width=142,height=30)

        GLabel_548=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_548["font"] = ft
        GLabel_548["fg"] = "#FFFFFF"
        GLabel_548["bg"] = "#1d1c1c"
        GLabel_548["justify"] = "center"
        GLabel_548["text"] = "Twitch"
        GLabel_548.place(x=290,y=620,width=143,height=30)

        GLabel_692=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_692["font"] = ft
        GLabel_692["fg"] = "#FFFFFF"
        GLabel_692["bg"] = "#1d1c1c"
        GLabel_692["justify"] = "center"
        GLabel_692["text"] = "Crossout Launcher"
        GLabel_692.place(x=480,y=620,width=230,height=32)

        GLabel_747=tk.Label(root)
        ft = tkFont.Font(family='sego ui',size=18)
        GLabel_747["font"] = ft
        GLabel_747["fg"] = "#FFFFFF"
        GLabel_747["bg"] = "#1d1c1c"
        GLabel_747["justify"] = "center"
        GLabel_747["text"] = "GDLauncher"
        GLabel_747.place(x=700,y=620,width=257,height=30)

        GButton_559=tk.Button(root)
        GButton_559["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_559["font"] = ft
        GButton_559["fg"] = "#000000"
        GButton_559["justify"] = "center"
        GButton_559["text"] = "Install"
        GButton_559.place(x=70,y=670,width=150,height=40)
        GButton_559["command"] = self.GButton_559_command

        GButton_636=tk.Button(root)
        GButton_636["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_636["font"] = ft
        GButton_636["fg"] = "#000000"
        GButton_636["justify"] = "center"
        GButton_636["text"] = "Install"
        GButton_636.place(x=290,y=670,width=150,height=40)
        GButton_636["command"] = self.GButton_636_command

        GButton_585=tk.Button(root)
        GButton_585["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Install"
        GButton_585.place(x=510,y=670,width=150,height=40)
        GButton_585["command"] = self.GButton_585_command

        GButton_813=tk.Button(root)
        GButton_813["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='sego ui',size=18)
        GButton_813["font"] = ft
        GButton_813["fg"] = "#000000"
        GButton_813["justify"] = "center"
        GButton_813["text"] = "install"
        GButton_813.place(x=740,y=670,width=150,height=40)
        GButton_813["command"] = self.GButton_813_command

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
        print("us")


    @staticmethod
    def GButton_362_command():
        print("ent")


    @staticmethod
    def GButton_676_command():
        os.system('cmd /k "winget install --id=Mojang.MinecraftLauncher  -e"')


    @staticmethod
    def GButton_205_command():
        os.system('cmd /k "winget install --id=Valve.Steam  -e"')


    @staticmethod
    def GButton_59_command():
        os.system('cmd /k "winget install --id=SmartGameBooster.SmartGameBooster  -e"')


    @staticmethod
    def GButton_516_command():
        os.system('cmd /k "winget install --id=EpicGames.EpicGamesLauncher  -e"')


    @staticmethod
    def GButton_183_command():
        os.system('cmd /k "winget install --id=PvPLounge.PvPLounge  -e"')


    @staticmethod
    def GButton_486_command():
        os.system('cmd /k "winget install --id=Playnite.Playnite  -e"')


    @staticmethod
    def GButton_261_command():
        os.system('cmd /k "winget install --id=RiotGames.Valorant.AP  -e"')


    @staticmethod
    def GButton_699_command():
        os.system('cmd /k "winget install --id=BlueStack.BlueStacks  -e"')


    @staticmethod
    def GButton_290_command():
        os.system('cmd /k "winget install --id=Ubisoft.Connect  -e"')


    @staticmethod
    def GButton_647_command():
        os.system('cmd /k "winget install --id=Plex.Plex  -e"')


    @staticmethod
    def GButton_322_command():
        os.system('cmd /k "winget install --id=Gamecaster.Gamecaster  -e"')


    @staticmethod
    def GButton_735_command():
        os.system('cmd /k "winget install --id=Blitz.Blitz  -e"')


    @staticmethod
    def GButton_285_command():
        os.system('cmd /k "winget install --id=Corsair.iCUE.4  -e"')


    @staticmethod
    def GButton_527_command():
        os.system('cmd /k "winget install --id=ElectronicArts.EADesktop  -e"')


    @staticmethod
    def GButton_392_command():
        os.system('cmd /k "winget install --id=Moonsworth.LunarClient  -e"')


    @staticmethod
    def GButton_278_command():
        os.system('cmd /k "winget install --id=Badlion.BadlionClient  -e"')


    @staticmethod
    def GButton_559_command():
        os.system('cmd /k "winget install --id=Deezer.Deezer  -e"')


    @staticmethod
    def GButton_636_command():
        os.system('cmd /k "winget install --id=Twitch.Twitch  -e"')


    @staticmethod
    def GButton_585_command():
        os.system('cmd /k "winget install --id=GaijinNetwork.Crossout  -e"')


    @staticmethod
    def GButton_813_command():
        os.system('cmd /k "winget install --id=GorillaDevs.GDLauncher  -e"')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
