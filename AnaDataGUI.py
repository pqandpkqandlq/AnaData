'''
这是一个GUI的一堆类
如果要新增UI的话
请按照UI这个基类进行设计，最好直接继承它

last update:2025.7.30 Nahidog(lsy)
'''
from lib import *
import time
import tkinter as tk
import tkinter.filedialog as tkfd
class UI(object):
    def __init__(self, window):  # 参数名改为window
        self.window=window
        self.variables()
        self.elements(window)
        self.display()
    def variables(self):
        pass
    def elements(self,window):
        pass
    def display(self):
        pass

class GetData_UI(UI):
    def variables(self):
        self.GetWays_selection=tk.StringVar()
        self.GetWays_selection.set("从本地获取")
        self.Path=tk.StringVar()
        self.SaveAsOtherPath=tk.StringVar()
        self.GetDataCondition=tk.StringVar()
        self.GetDataCondition.set("状态:")
        self.GetDataCondition_color=tk.StringVar()
        self.GetDataCondition_color.set("black")
        self.GetDataCondition_Add=""
    def elements(self,window):
        self.label_GetWays=tk.Label(window.win,text="数据获取:",font=FONT)
        self.label_FilePath=tk.Label(window.win,text="文件路径:",font=FONT)
        self.entry_FilePath=tk.Entry(window.win)
        def OpenFile():
            """打开文件对话框，选择文件并更新文件路径输入框"""
            self.Path.set(tkfd.askopenfilename(filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]))
            self.entry_FilePath.delete(0, tk.END)
            self.entry_FilePath.insert(0, self.Path.get())
            self.entry_FilePath.icursor(len(self.entry_FilePath.get()) - 1)
        self.button_FilePath = tk.Button(window.win, text="选择",command=OpenFile)
        self.label_GetDataCondition = tk.Label(window.win, font=FONT, textvariable=self.GetDataCondition,fg=self.GetDataCondition_color.get())
        self.label_GetURL = tk.Label(window.win, font=FONT, text="URL:")
        self.entry_GetURL = tk.Entry(window.win)
        self.label_UserAgent = tk.Label(window.win, font=FONT, text="设置User-Agent:")
        self.entry_UserAgent = tk.Entry(window.win)

        def SetDefaultUserAgent():
            """设置默认的User-Agent"""
            self.entry_UserAgent.delete(0, tk.END)
            self.entry_UserAgent.insert(0, DEFAULT_USER_AGENT)

        self.button_DefalutUserAgent = tk.Button(window.win, text="设置默认值",command=SetDefaultUserAgent)
        self.label_SaveAsOtherPath=tk.Label(window.win,font=FONT,text="另存为:")
        self.entry_SaveAsOtherPath=tk.Entry(window.win)


        def SaveAsOther():
            """打开另存为对话框，选择保存路径并更新输入框"""
            self.SaveAsOtherPath.set(tkfd.asksaveasfilename(filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]))

            if self.SaveAsOtherPath.get()[-4:]==".txt" or self.SaveAsOtherPath.get()[-4:]==".TXT":
                pass
            else:
                self.SaveAsOtherPath.set(self.SaveAsOtherPath.get()+".txt")
            self.entry_SaveAsOtherPath.delete(0,tk.END)
            self.entry_SaveAsOtherPath.insert(0,self.SaveAsOtherPath.get())
            self.entry_SaveAsOtherPath.icursor(len(self.entry_SaveAsOtherPath.get())-1)


        

        self.button_SaveAsOtherPath=tk.Button(window.win,text="选择",command=SaveAsOther)


        def SetTEMP():
            """设置临时文件路径"""
            self.entry_SaveAsOtherPath.delete(0,tk.END)
            self.entry_SaveAsOtherPath.insert(0,"C:/Users/ADMINI~1/AppData/Local/Temp/AnaData/{}.txt".format(time.time()))


        self.button_TEMP=tk.Button(window.win,text="设为临时文件",command=SetTEMP)
        def on_getways_selection(*args):
            """根据数据获取方式的选择，显示或隐藏相应的UI元素"""
            self.label_GetDataCondition.place(x=LABEL_GETDATACONDITION_POS[0], y=LABEL_GETDATACONDITION_POS[1])
            if self.GetWays_selection.get() == "从本地获取":
                # 显示本地文件相关UI，隐藏网络获取相关UI
                self.label_FilePath.place(x=LABEL_FILEPATH_POS[0], y=LABEL_FILEPATH_POS[1])
                self.entry_FilePath.place(x=ENTRY_FILEPATH_POS[0], y=ENTRY_FILEPATH_POS[1])
                self.button_FilePath.place(x=BUTTON_FILEPATH_POS[0], y=BUTTON_FILEPATH_POS[1])
                # 隐藏网络获取相关UI
                self.label_GetURL.place_forget()
                self.entry_GetURL.place_forget()
                self.label_UserAgent.place_forget()
                self.entry_UserAgent.place_forget()
                self.button_DefalutUserAgent.place_forget()
                self.label_SaveAsOtherPath.place_forget()
                self.entry_SaveAsOtherPath.place_forget()
                self.button_SaveAsOtherPath.place_forget()
                self.button_TEMP.place_forget()
            elif self.GetWays_selection.get() == "从网络获取":
                # 显示网络获取相关UI，隐藏本地文件相关UI
                self.label_GetURL.place(x=LABEL_GETURL_POS[0], y=LABEL_GETURL_POS[1])
                self.entry_GetURL.place(x=ENTRY_GETURL_POS[0], y=ENTRY_GETURL_POS[1])
                self.label_UserAgent.place(x=LABEL_USERAGENT_POS[0], y=LABEL_USERAGENT_POS[1])
                self.entry_UserAgent.place(x=ENTRY_USERAGENT_POS[0], y=ENTRY_USERAGENT_POS[1])
                self.button_DefalutUserAgent.place(x=BUTTON_USERAGENT_POS[0], y=BUTTON_USERAGENT_POS[1])
                self.label_SaveAsOtherPath.place(x=LABEL_SAVEASOTHERPATH_POS[0], y=LABEL_SAVEASOTHERPATH_POS[1])
                self.entry_SaveAsOtherPath.place(x=ENTRY_SAVEASOTHERPATH_POS[0], y=ENTRY_SAVEASOTHERPATH_POS[1])
                self.button_SaveAsOtherPath.place(x=BUTTON_SAVEASOTHERPATH_POS[0], y=BUTTON_SAVEASOTHERPATH_POS[1])
                self.button_TEMP.place(x=BUTTON_TEMP_POS[0], y=BUTTON_TEMP_POS[1])
                # 隐藏本地文件相关UI
                self.label_FilePath.place_forget()
                self.entry_FilePath.place_forget()
                self.button_FilePath.place_forget()
        on_getways_selection()
        self.optionmenu_GetWays = tk.OptionMenu(window.win, self.GetWays_selection, *["从本地获取","从网络获取"], command=on_getways_selection)
        
    def display(self):
        self.label_GetWays.place(x=LABEL_GETWAYS_POS[0],y=LABEL_GETWAYS_POS[1])
        self.label_GetDataCondition.place(x=LABEL_GETDATACONDITION_POS[0],y=LABEL_GETDATACONDITION_POS[1])
        self.optionmenu_GetWays.place(x=OPTIONMENU_GETWAYS_POS[0],y=OPTIONMENU_GETWAYS_POS[1])
        

class AnalyseData_UI(UI):
    def variables(self):
        self.AnalyseDataCondition = tk.StringVar()
        self.AnalyseDataCondition.set("状态:")
        self.AnalyseDataCondition_color = tk.StringVar()
        self.AnalyseDataCondition_color.set("black")
        self.text=""
        self.global_data_frame=None

    def __init__(self, window):  # 参数名改为window
        super().__init__(window)
        self.get_data_ui = GetData_UI(window)
        
    def elements(self, window):  # 参数名改为window
        self.label_DataAnalyseCondition = tk.Label(window.win, font=FONT, textvariable=self.AnalyseDataCondition)  # 改为window.win
        self.label_DataAnalyse=tk.Label(window.win,font=FONT,text="数据分析:")
        # 正则表达式输入区域
        self.label_REZone = tk.Label(window.win, font=FONT, text="表达式区")
        self.text_REZone = tk.Text(window.win, font=FONT)
        
        # 类型输入区域
        self.label_TypeZone = tk.Label(window.win, font=FONT, text="类型区")
        self.text_TypeZone = tk.Text(window.win, font=FONT)
        
        # 分析按钮
        self.button_Analyse = tk.Button(window.win, text="开始", command=self.START)
        
    def display(self):
        # 放置UI元素
        self.label_DataAnalyseCondition.place(x=LABEL_DATAANALYSECONDITION_POS[0], y=LABEL_DATAANALYSECONDITION_POS[1])
        self.label_REZone.place(x=LABEL_REZONE_POS[0], y=LABEL_REZONE_POS[1])
        self.text_REZone.place(x=TEXT_REZONE_POS[0], y=TEXT_REZONE_POS[1],height=TEXT_REZONE_HEIGHT,width=TEXT_REZONE_WIDTH)
        self.label_TypeZone.place(x=LABEL_TYPEZONE_POS[0], y=LABEL_TYPEZONE_POS[1])
        self.text_TypeZone.place(x=TEXT_TYPEZONE_POS[0], y=TEXT_TYPEZONE_POS[1],height=TEXT_TYPEZONE_HEIGHT,width=TEXT_TYPEZONE_WIDTH)
        self.button_Analyse.place(x=BUTTON_START_POS[0], y=BUTTON_START_POS[1],)
        self.label_DataAnalyse.place(x=LABEL_DATAANALYSE_POS[0],y=LABEL_DATAANALYSE_POS[1])
        
    def get_data(self):
        if self.get_data_ui.GetWays_selection.get()=="从本地获取":
            self.text=get_on_local(self.get_data_ui.entry_FilePath.get())
            self.get_data_ui.GetDataCondition_color.set("green")
            self.get_data_ui.GetDataCondition.set("状态:获取数据成功")
            self.get_data_ui.label_GetDataCondition.config(fg=self.get_data_ui.GetDataCondition_color.get())
        elif self.get_data_ui.GetWays_selection.get()=="从网络获取":
            response=get_on_Internet(self.get_data_ui.entry_GetURL.get(),self.get_data_ui.entry_UserAgent.get())
            if response[0]==200:
                self.text=response[1]
                if self.get_data_ui.SaveAsOtherPath.get()!="":
                    save_file(self.text,self.get_data_ui.SaveAsOtherPath.get())
            else:
                self.AnalyseDataCondition.set("状态:获取数据失败")
                self.AnalyseDataCondition_color.set("red")
                self.label_DataAnalyseCondition.config(foreground=self.AnalyseDataCondition_color.get())
                
    def analyse(self):
        """执行数据分析的逻辑"""
        types = []
        for i in self.text_TypeZone.get("1.0", "end").split("\n"):
            if i != "":
                types.append(i)
        
        REs = []
        for i in self.text_REZone.get("1.0", "end").split("\n"):
            if i != "":
                try:
                    REs.append(re.compile(i, re.MULTILINE))
                except re.error as e:
                    self.AnalyseDataCondition.set(f"状态:正则表达式错误: {e}")
                    self.AnalyseDataCondition_color.set("red")
                    self.label_DataAnalyseCondition.config(foreground=self.AnalyseDataCondition_color.get())
                    return
        
        try:
            
            self.global_data_frame = analyse_data(types, self.text, REs)
        except Exception as e:
            self.AnalyseDataCondition.set("状态:分析数据时出错:{}".format(e))
            self.AnalyseDataCondition_color.set("red")
            self.label_DataAnalyseCondition.config(foreground=self.AnalyseDataCondition_color.get())
        else:
            self.AnalyseDataCondition.set("状态:分析数据成功,可被导出")
            self.AnalyseDataCondition_color.set("green")
            self.label_DataAnalyseCondition.config(foreground=self.AnalyseDataCondition_color.get())
    def START(self):
        self.get_data()
        self.analyse()
    

class ExportData_UI(UI):
    def __init__(self, window):  # 参数名改为window
        super().__init__(window)
        self.analyse_data_ui = AnalyseData_UI(window)
    def variables(self):
        self.ExportDataCondition = tk.StringVar()
        self.ExportDataCondition.set("状态:")
        self.ExportDataCondition_color = tk.StringVar()
        self.ExportDataCondition_color.set("black")
        self.Save_Path = tk.StringVar()    
    def elements(self, window):  # 参数名改为window
        self.label_DataExport = tk.Label(window.win, text="数据导出:", font=FONT)  # 改为window.win
        self.label_SaveTo = tk.Label(window.win, text="保存至:", font=FONT)
        self.entry_SaveTo = tk.Entry(window.win)
        
        def choose_save_path():
            path = tkfd.asksaveasfilename()
            self.entry_SaveTo.delete(0, tk.END)
            self.entry_SaveTo.insert(0, path)
            self.entry_SaveTo.icursor(len(self.entry_SaveTo.get())-1)
            self.Save_Path.set(path)
            
        self.button_SaveTo = tk.Button(window.win, text="选择", command=choose_save_path)
        
        def save_as_excel():
            file_path = self.entry_SaveTo.get()
            if file_path.endswith(('.txt', '.TXT')):
                file_path = file_path[:-4] + ".xlsx"
            elif not file_path.endswith(('.xlsx', '.XLSX')) and file_path != "":
                file_path += '.xlsx'
            elif file_path == "":
                self.ExportDataCondition.set("状态:路径不能为空")
                self.ExportDataCondition_color.set("red")
                self.label_ExportCondition.config(foreground=self.ExportDataCondition_color.get())
                return
                
            if file_path:
                try:
                    export_data_as_excel(self.analyse_data_ui.global_data_frame, file_path)
                except PermissionError:
                    self.ExportDataCondition.set("状态:权限错误,请检查文件是否被占用")
                    self.ExportDataCondition_color.set("red")
                except FileNotFoundError:
                    self.ExportDataCondition.set("状态:文件不存在,请检查路径是否正确")
                    self.ExportDataCondition_color.set("red")
                except ValueError:
                    self.ExportDataCondition.set("状态:数据格式错误")
                    self.ExportDataCondition_color.set("red")
                except Exception as e:
                    self.ExportDataCondition.set(f"状态:保存时出错:{e}")
                    self.ExportDataCondition_color.set("red")
                else:
                    self.ExportDataCondition.set("状态:导出成功")
                    self.ExportDataCondition_color.set("green")
                finally:
                    self.label_ExportCondition.config(foreground=self.ExportDataCondition_color.get())
                    
        self.button_SaveAsExcel = tk.Button(window.win, text="保存为Excel", command=save_as_excel)
        
        def save_as_txt():
            file_path = self.entry_SaveTo.get()
            if file_path.endswith(('.xlsx', '.XLSX')):
                file_path = file_path[:-5] + ".txt"
            elif not file_path.endswith(('.txt', '.TXT')) and file_path != "":
                file_path += '.txt'
            elif file_path == "":
                self.ExportDataCondition.set("状态:路径不能为空")
                self.ExportDataCondition_color.set("red")
                self.label_ExportCondition.config(foreground=self.ExportDataCondition_color.get())
                return
                
            if file_path:
                try:
                    export_data_as_txt(self.analyse_data_ui.global_data_frame, file_path)
                except PermissionError:
                    self.ExportDataCondition.set("状态:权限错误,请检查文件是否被占用")
                    self.ExportDataCondition_color.set("red")
                except FileNotFoundError:
                    self.ExportDataCondition.set("状态:文件不存在,请检查路径是否正确")
                    self.ExportDataCondition_color.set("red")
                except ValueError:
                    self.ExportDataCondition.set("状态:数据格式错误")
                    self.ExportDataCondition_color.set("red")
                except Exception as e:
                    self.ExportDataCondition.set(f"状态:保存时出错:{e}")
                else:
                    self.ExportDataCondition.set("状态:保存成功")
                    self.ExportDataCondition_color.set("green")
                finally:
                    self.label_ExportCondition.config(foreground=self.ExportDataCondition_color.get())
                    
        self.button_SaveAsTXT = tk.Button(window.win, text="保存为txt", command=save_as_txt)
        self.label_ExportCondition = tk.Label(window.win, textvariable=self.ExportDataCondition, foreground=self.ExportDataCondition_color.get(), font=FONT)
                                           
    def display(self):
        self.label_DataExport.place(x=LABEL_DATAEXPORT_POS[0], y=LABEL_DATAEXPORT_POS[1])
        self.label_SaveTo.place(x=LABEL_SAVETO_POS[0], y=LABEL_SAVETO_POS[1])
        self.entry_SaveTo.place(x=ENTRY_SAVETO_POS[0], y=ENTRY_SAVETO_POS[1])
        self.button_SaveTo.place(x=BUTTON_SAVETO_POS[0], y=BUTTON_SAVETO_POS[1])
        self.button_SaveAsExcel.place(x=BUTTON_SAVEASEXCEL_POS[0], y=BUTTON_SAVEASEXCEL_POS[1])
        self.button_SaveAsTXT.place(x=BUTTON_SAVEASTXT_POS[0], y=BUTTON_SAVEASTXT_POS[1])
        self.label_ExportCondition.place(x=LABEL_EXPORTCONDITION_POS[0], y=LABEL_EXPORTCONDITION_POS[1])

class Help_Button(UI):
    def elements(self, window):
        self.button_help = tk.Button(window.win, text="帮助", font=FONT, command=self.help)
    def display(self):
        self.button_help.place(x=BUTTON_HELP_POS[0], y=BUTTON_HELP_POS[1])
    def help(self):
        # 修改后的帮助方法，添加窗口存在性检查
        if not hasattr(self.window, 'helpwin') or not hasattr(self.window.helpwin, 'win') or not self.window.helpwin.win.winfo_exists():
            self.window.helpwin.WinMain()
        else:
            self.window.helpwin.win.lift()  # 如果窗口已存在则提到最前
            self.window.helpwin.win.focus_force()  # 强制获得焦点

class Help_UI(UI):#帮助UI，要在帮助窗口
    
    def variables(self):
        self.text=HELP_TEXT
    def elements(self,win2):
        self.text_help=tk.Text(win2,font=FONT,wrap=tk.WORD)

    def display(self):
        self.text_help.pack(fill=tk.BOTH,expand=True, padx=10, pady=10)
        self.text_help.insert(tk.END, self.text)
        self.text_help.config(state=tk.DISABLED)