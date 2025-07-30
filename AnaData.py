'''
恭喜你找到了这里，这是启动文件AnaData.py
一切一切bug的开端，曾经的烈士在这里与屎山斗争
不知多少的日月与秃头
如果你看到了这里，说明你是一个有想法的人
如果你看到了这里，说明你是一个有能力的人
如果你看到了这里，说明你是一个有毅力的人
如果你看到了这里，说明你是一个傻逼，为什么要接手这个项目
但是这并不代表你无能
勇者啊！
你的旅途从未停止
你的梦想从未失败
在这里，你将缔造一个属于平阳县鳌江中学的传说
勇者啊！请不要忘记:
写注释！写注释！写注释！
不要乱动！不要乱动！不要乱动！
不要删除！不要删除！不要删除！

last update:2025.7.30 Nahidog(lsy)
'''
from AnaDataGUI import *
class Window:
    def __init__(self,title:str,resizable:list,geometry:str):
        self.title=title
        self.resizable=resizable
        self.geometry=geometry
    def WinMain(self):
        pass      
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
        program=ExportData_UI(self)#别问为啥，这个ExportData_UI里面包含了所有的功能，《论继承》
        help=Help_Button(self)
        self.win.mainloop()            

if __name__=="__main__":
    AnaData=MainWindow(TITLE,(False,False),GEOMETRY)
    AnaData.WinMain()