from ui_class import *


class HelpWindow(Window):
    def WinMain(self):
        self.win=tk.Toplevel()
        program=Help_UI(self.win)

class MainWindow(Window):
    def __init__(self,title:str,resizable:list,geometry:str):
        super().__init__(title,resizable,geometry)
        self.helpwin=HelpWindow("AnaData 帮助",(False, False),"600x400")
    
    def WinMain(self):
        self.win=tk.Tk()
        self.win.geometry(self.geometry)
        self.win.title(self.title)
        self.win.resizable(self.resizable[0],self.resizable[1])
        program=ExportData_UI(self)
        help=Help_Button(self)
        self.win.mainloop()