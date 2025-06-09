
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
'''
from lib import *
import time
import tkinter as tk
import tkinter.filedialog as tkfd


# 主程序初始化部分
######################################################################
######################################################################
######################################################################
######################################################################
if __name__ == "__main__":

    win = tk.Tk()

    #全局变量初始化
    GetWays_selection=tk.StringVar()
    GetWays_selection.set("从本地获取")
    Path=tk.StringVar()
    SaveAsOtherPath=tk.StringVar()
    GetDataCondition=tk.StringVar()
    GetDataCondition.set("状态:")
    GetDataCondition_color=tk.StringVar()
    GetDataCondition_color.set("black")
    AnalyseDataCondition=tk.StringVar()
    AnalyseDataCondition.set("状态:")
    AnalyseDataCondition_color=tk.StringVar()
    AnalyseDataCondition_color.set("black")
    ExportDataCondition=tk.StringVar()
    ExportDataCondition.set("状态:")
    ExportDataCondition_color=tk.StringVar()
    ExportDataCondition_color.set("black")
    global_data_frame=DataFrame()
    #这里是一些临时变量，不要动，不然会炸
    #要加的随便加，但是不要改，不要重复，不要删
    #最好在开头加上自己的名字，放置冲突，也方便找出凶手
    lsy_temp1=""

    # 窗口设置
    win.title("AnaData")
    win.geometry("500x600")
    win.resizable(False,False)



# 数据获取部分
######################################################################
######################################################################
######################################################################
######################################################################
    label_GetWays=tk.Label(win,text="数据获取:",font=FONT)
    label_GetWays.place(x=LABEL_GETWAYS_POS[0],y=LABEL_GETWAYS_POS[1])
    label_FilePath=tk.Label(win,text="文件路径:",font=FONT)
    entry_FilePath=tk.Entry(win)
    Path.set(entry_FilePath.get())
    
    def OpenFile():
        """打开文件对话框，选择文件并更新文件路径输入框"""
        Path.set(tkfd.askopenfilename(filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]))
        entry_FilePath.delete(0, tk.END)
        entry_FilePath.insert(0, Path.get())
        entry_FilePath.icursor(len(entry_FilePath.get()) - 1)
    
    button_FilePath = tk.Button(win, text="选择", command=OpenFile)
    label_GetDataCondition = tk.Label(win, font=FONT, textvariable=GetDataCondition, foreground=GetDataCondition_color.get())
    label_GetURL = tk.Label(win, font=FONT, text="URL:")
    entry_GetURL = tk.Entry(win)
    label_UserAgent = tk.Label(win, font=FONT, text="设置User-Agent:")
    entry_UserAgent = tk.Entry(win)
    
    def SetDefaultUserAgent():
        """设置默认的User-Agent"""
        entry_UserAgent.delete(0, tk.END)
        entry_UserAgent.insert(0, DEFAULT_USER_AGENT)
    
    button_DefalutUserAgent = tk.Button(win, text="设置默认值",command=SetDefaultUserAgent)
    label_SaveAsOtherPath=tk.Label(win,font=FONT,text="另存为:")
    entry_SaveAsOtherPath=tk.Entry(win)
    
    def SaveAsOther():
        """打开另存为对话框，选择保存路径并更新输入框"""
        SaveAsOtherPath.set(tkfd.asksaveasfilename())
        if SaveAsOtherPath.get()[-4:-1]!=".txt" and SaveAsOtherPath.get()[-4:-1]!=".TXT":
            SaveAsOtherPath.set(SaveAsOtherPath.get()+".txt")
        entry_SaveAsOtherPath.delete(0,tk.END)
        entry_SaveAsOtherPath.insert(0,SaveAsOtherPath.get())
        entry_SaveAsOtherPath.icursor(len(entry_SaveAsOtherPath.get())-1)
    
    def save_as_other(text):
        """将文本内容保存到指定路径的文件中"""
        file_path = entry_SaveAsOtherPath.get()
        if file_path=="":
            return
        if not file_path.endswith(('.txt', '.TXT')):
            file_path += '.txt'
        global lsy_temp1
        if file_path:                                   
            try:                                   
                with open(file_path, "w", encoding='utf-8') as file:
                    file.write(text)
            except PermissionError:
                #print("权限错误：无法写入文件，请检查文件是否被占用或是否有写权限")
                
                lsy_temp1="权限错误：无法写入文件，请检查文件是否被占用或是否有写权限"
            except FileNotFoundError:
                #print("文件路径错误：指定的目录不存在")
                lsy_temp1="文件路径错误：指定的目录不存在"
            except UnicodeEncodeError:
                #print("编码错误：无法将文本编码为UTF-8格式")
                lsy_temp1="编码错误：无法将文本编码为UTF-8格式"
            except Exception as e:
                #print(f"保存文件时发生未知错误: {e}")
                lsy_temp1=f"保存文件时发生未知错误: {e}"
    
    button_SaveAsOtherPath=tk.Button(win,text="选择",command=SaveAsOther)
    
    def SetTEMP():
        """设置临时文件路径"""
        entry_SaveAsOtherPath.delete(0,tk.END)
        entry_SaveAsOtherPath.insert(0,"C:/Users/ADMINI~1/AppData/Local/Temp/AnaData/{}.txt".format(time.time()))
    
    button_TEMP=tk.Button(win,text="设为临时文件",command=SetTEMP)
    
    def on_getways_selection(*args):
        """根据数据获取方式的选择，显示或隐藏相应的UI元素"""
        label_GetDataCondition.place(x=LABEL_GETDATACONDITION_POS[0], y=LABEL_GETDATACONDITION_POS[1])
        if GetWays_selection.get() == "从本地获取":
            # 显示本地文件相关UI，隐藏网络获取相关UI
            label_FilePath.place(x=LABEL_FILEPATH_POS[0], y=LABEL_FILEPATH_POS[1])
            entry_FilePath.place(x=ENTRY_FILEPATH_POS[0], y=ENTRY_FILEPATH_POS[1])
            button_FilePath.place(x=BUTTON_FILEPATH_POS[0], y=BUTTON_FILEPATH_POS[1])
            # 隐藏网络获取相关UI
            label_GetURL.place_forget()
            entry_GetURL.place_forget()
            label_UserAgent.place_forget()
            entry_UserAgent.place_forget()
            button_DefalutUserAgent.place_forget()
            label_SaveAsOtherPath.place_forget()
            entry_SaveAsOtherPath.place_forget()
            button_SaveAsOtherPath.place_forget()
            button_TEMP.place_forget()
        elif GetWays_selection.get() == "从网络获取":
            # 显示网络获取相关UI，隐藏本地文件相关UI
            label_GetURL.place(x=LABEL_GETURL_POS[0], y=LABEL_GETURL_POS[1])
            entry_GetURL.place(x=ENTRY_GETURL_POS[0], y=ENTRY_GETURL_POS[1])
            label_UserAgent.place(x=LABEL_USERAGENT_POS[0], y=LABEL_USERAGENT_POS[1])
            entry_UserAgent.place(x=ENTRY_USERAGENT_POS[0], y=ENTRY_USERAGENT_POS[1])
            button_DefalutUserAgent.place(x=BUTTON_USERAGENT_POS[0], y=BUTTON_USERAGENT_POS[1])
            label_SaveAsOtherPath.place(x=LABEL_SAVEASOTHERPATH_POS[0],y=LABEL_SAVEASOTHERPATH_POS[1])
            entry_SaveAsOtherPath.place(x=ENTRY_SAVEASOTHERPATH_POS[0],y=ENTRY_SAVEASOTHERPATH_POS[1])
            button_SaveAsOtherPath.place(x=BUTTON_SAVEASOTHERPATH_POS[0],y=BUTTON_SAVEASOTHERPATH_POS[1])
            button_TEMP.place(x=BUTTON_TEMP_POS[0],y=BUTTON_TEMP_POS[1])
            # 隐藏本地文件相关UI
            label_FilePath.place_forget()
            entry_FilePath.place_forget()
            button_FilePath.place_forget()
    
    optionmenu_GetWays=tk.OptionMenu(win,GetWays_selection,*["从本地获取","从网络获取"],command=on_getways_selection)
    optionmenu_GetWays.place(x=OPTIONMENU_GETWAYS_POS[0],y=OPTIONMENU_GETWAYS_POS[1])
    on_getways_selection()  # 初始化时调用一次，确保初始状态正确



# 数据分析部分
######################################################################
######################################################################
######################################################################
######################################################################
    label_DataAnalyse=tk.Label(win,text="数据分析:",font=FONT)
    label_TypeZone=tk.Label(win,text="类型区:",font=FONT)
    label_REZone=tk.Label(win,text="表达式区:",font=FONT)
    text_TypeZone=tk.Text(win,font=FONT)
    text_REZone=tk.Text(win,font=FONT)
    label_DataAnalyseCondition=tk.Label(win,textvariable=AnalyseDataCondition,foreground=AnalyseDataCondition_color.get(),font=FONT)
    
    def START():

        GetDataCondition.set("状态:")
        GetDataCondition_color.set("black")
        label_GetDataCondition.config(foreground=GetDataCondition_color.get())
        AnalyseDataCondition.set("状态:")
        AnalyseDataCondition_color.set("black")
        label_DataAnalyseCondition.config(foreground=AnalyseDataCondition_color.get())
        ExportDataCondition.set("状态:")
        ExportDataCondition_color.set("black")
        label_ExportCondition.config(foreground=ExportDataCondition_color.get())
        text = ""
        global global_data_frame
        global_data_frame = DataFrame()  # 清空之前的数据
        
        if GetWays_selection.get() == "从网络获取":
            if entry_GetURL.get() == "":
                GetDataCondition.set("状态:URL不能为空")
                GetDataCondition_color.set("red")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
                return
            if entry_GetURL.get()[:7] != 'http://' and entry_GetURL.get()[:8] != 'https://':
                GetDataCondition.set("状态:URL缺少协议,应开头加上'http://'或'https://'")
                GetDataCondition_color.set("red")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
                return
            res = get_on_Internet(entry_GetURL.get(), entry_UserAgent.get())
            if res[0] == 200:

                try:

                    text = res[1].encode('iso-8859-1').decode('utf-8')
                except:
                    try:
                        text = res[1].encode(res[1].encoding).decode(res[1].apparent_encoding)
                    except:
                        text = res[1]
                GetDataCondition.set("状态:成功获取网页内容")
                GetDataCondition_color.set("green")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
            else:

                GetDataCondition.set("状态:网络获取异常:{}".format(res[0]))
                GetDataCondition_color.set("red")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
                return
            save_as_other(text)
            if lsy_temp1!="":
                GetDataCondition.set(GetDataCondition.get()+",另存为出错:"+lsy_temp1)
                GetDataCondition_color.set(YELLOW)
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
        elif GetWays_selection.get() == "从本地获取":
            text = get_on_local(entry_FilePath.get())

            '''if isinstance(text, int):
                GetDataCondition.set("状态:本地文件获取异常")
                GetDataCondition_color.set("red")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
                return'''
            if text==114:
                GetDataCondition.set("状态:本地文件路径不合法")
                GetDataCondition_color.set("red")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
                return
            elif text==-1:
                GetDataCondition.set("状态:本地文件不存在")
                GetDataCondition_color.set("red")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
                return
            elif text==2:
                GetDataCondition.set("状态:本地文件解码失败")
                GetDataCondition_color.set("red")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
                return
            elif text==1:
                GetDataCondition.set("状态:本地文件获取出错")
                GetDataCondition_color.set("red")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
                return
            else:
                GetDataCondition.set("状态:成功获取本地文件内容")
                GetDataCondition_color.set("green")
                label_GetDataCondition.config(foreground=GetDataCondition_color.get())
        
        types = []
        for i in text_TypeZone.get("1.0", "end").split("\n"):
            if i != "":
                types.append(i)
        REs = []
        for i in text_REZone.get("1.0", "end").split("\n"):
            if i != "":
                try:
                    REs.append(re.compile(i, re.MULTILINE))
                except re.error as e:
                    AnalyseDataCondition.set(f"状态:正则表达式错误: {e}")
                    AnalyseDataCondition_color.set("red")
                    label_DataAnalyseCondition.config(foreground=AnalyseDataCondition_color.get())
                    return
        
        try:


            global_data_frame = analyse_data(types, text, REs)
        except Exception as e:
            AnalyseDataCondition.set("状态:分析数据时出错:{}".format(e))
            AnalyseDataCondition_color.set("red")
            label_DataAnalyseCondition.config(foreground=AnalyseDataCondition_color.get())
        else:
            AnalyseDataCondition.set("状态:分析数据成功,可被导出")
            AnalyseDataCondition_color.set("green")
            label_DataAnalyseCondition.config(foreground=AnalyseDataCondition_color.get())
            ExportDataCondition.set("状态:就绪")

            ExportDataCondition_color.set(YELLOW)
            label_ExportCondition.config(foreground=ExportDataCondition_color.get())



    
    button_Start=tk.Button(win,text="开始",command=START)

    text_TypeZone.place(x=TEXT_TYPEZONE_POS[0],y=TEXT_TYPEZONE_POS[1], width=140, height=200)
    text_REZone.place(x=TEXT_REZONE_POS[0], y=TEXT_REZONE_POS[1], width=290, height=200)

    button_Start.place(x=BUTTON_START_POS[0],y=BUTTON_START_POS[1])
    label_DataAnalyse.place(x=LABEL_DATAANALYSE_POS[0],y=LABEL_DATAANALYSE_POS[1])
    label_TypeZone.place(x=LABEL_TYPEZONE_POS[0],y=LABEL_TYPEZONE_POS[1])
    label_REZone.place(x=LABEL_REZONE_POS[0],y=LABEL_REZONE_POS[1])
    label_DataAnalyseCondition.place(x=LABEL_DATAANALYSECONDITION_POS[0],y=LABEL_DATAANALYSECONDITION_POS[1])





# 数据导出部分
######################################################################
######################################################################
######################################################################
######################################################################
    Save_Path=tk.StringVar()



    label_DataExport=tk.Label(win,text="数据导出:",font=FONT)
    label_SaveTo=tk.Label(win,text="保存至:",font=FONT)
    entry_SaveTo=tk.Entry(win)
    
    def choose_save_path():
        path=tkfd.asksaveasfilename()
        entry_SaveTo.delete(0,tk.END)
        entry_SaveTo.insert(0,path)
        entry_SaveTo.icursor(len(entry_SaveTo.get())-1)
        Save_Path.set(path)
    
    button_SaveTo=tk.Button(win,text="选择",command=choose_save_path)
    
    def save_as_excel():
        file_path=entry_SaveTo.get()
        if file_path.endswith(('.txt', '.TXT')):
            file_path=file_path[:-4]
            file_path+=".xlsx"
        elif not file_path.endswith(('.xlsx', '.XLSX')) and file_path!="":
            file_path += '.xlsx'
        elif file_path=="":
            ExportDataCondition.set("状态:路径不能为空")
            ExportDataCondition_color.set("red")
            label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            return
        if file_path:
            try:

                export_data_as_excel(global_data_frame,file_path)
            except PermissionError:
                ExportDataCondition.set("状态:权限错误,请检查文件是否被占用")
                ExportDataCondition_color.set("red")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            except FileNotFoundError:
                ExportDataCondition.set("状态:文件不存在,请检查路径是否正确")
                ExportDataCondition_color.set("red")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            except ValueError:
                ExportDataCondition.set("状态:数据格式错误")
                ExportDataCondition_color.set("red")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            except Exception as e:
                ExportDataCondition.set("状态:保存时出错:{}".format(e))
                ExportDataCondition_color.set("red")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            else:
                ExportDataCondition.set("状态:导出成功")
                ExportDataCondition_color.set("green")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
    
    button_SaveAsExcel=tk.Button(win,text="保存为Excel",command=save_as_excel)
    
    def save_as_txt():
        file_path=entry_SaveTo.get()
        if file_path.endswith(('.xlsx', '.XLSX')):
            file_path=file_path[:-5]
            file_path+=".txt"
        elif not file_path.endswith(('.txt', '.TXT')) and file_path!="":
            file_path += '.txt'
        elif file_path=="":
            ExportDataCondition.set("状态:路径不能为空")
            ExportDataCondition_color.set("red")
            label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            return
        if file_path:
            try:
                export_data_as_txt(global_data_frame,file_path)
            except PermissionError:
                ExportDataCondition.set("状态:权限错误,请检查文件是否被占用")
                ExportDataCondition_color.set("red")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            except FileNotFoundError:
                ExportDataCondition.set("状态:文件不存在,请检查路径是否正确")
                ExportDataCondition_color.set("red")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            except ValueError:
                ExportDataCondition.set("状态:数据格式错误")
                ExportDataCondition_color.set("red")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
            except Exception as e:
                ExportDataCondition.set("状态:保存时出错:{}".format(e))
            else:
                ExportDataCondition.set("状态:保存成功")
                ExportDataCondition_color.set("green")
                label_ExportCondition.config(foreground=ExportDataCondition_color.get())
    
    button_SaveAsTXT=tk.Button(win,text="保存为txt",command=save_as_txt)
    label_ExportCondition=tk.Label(win,textvariable=ExportDataCondition,foreground=ExportDataCondition_color.get(),font=FONT)
    label_ExportCondition.place(x=LABEL_EXPORTCONDITION_POS[0],y=LABEL_EXPORTCONDITION_POS[1])
    label_DataExport.place(x=LABEL_DATAEXPORT_POS[0],y=LABEL_DATAEXPORT_POS[1])
    label_SaveTo.place(x=LABEL_SAVETO_POS[0],y=LABEL_SAVETO_POS[1])
    entry_SaveTo.place(x=ENTRY_SAVETO_POS[0],y=ENTRY_SAVETO_POS[1])
    button_SaveTo.place(x=BUTTON_SAVETO_POS[0],y=BUTTON_SAVETO_POS[1])
    button_SaveAsExcel.place(x=BUTTON_SAVEASEXCEL_POS[0],y=BUTTON_SAVEASEXCEL_POS[1])
    button_SaveAsTXT.place(x=BUTTON_SAVEASTXT_POS[0],y=BUTTON_SAVEASTXT_POS[1])


    help_running = False  # 添加全局变量跟踪帮助窗口状态
    win2 = None  # 保存帮助窗口引用

    def help():
        """显示程序帮助信息"""
        global help_running, win2
        
        if help_running and win2:  # 如果帮助窗口已经存在
            try:
                win2.lift()  # 将现有窗口提到最前
                win2.focus_force()  # 强制获取焦点
            except tk.TclError:  # 如果窗口已被关闭
                help_running = False
                win2 = None
                help()  # 重新创建窗口
            return
            
        help_running = True
        win2 = tk.Toplevel()  # 使用Toplevel而不是Tk，避免创建多个主窗口
        win2.title("AnaData 帮助")
        win2.geometry("600x400")
        win2.resizable(False, False)
        
        # 添加窗口关闭时的处理
        def on_close():
            global help_running, win2
            help_running = False
            win2.destroy()
            win2 = None
            
        win2.protocol("WM_DELETE_WINDOW", on_close)
        
        # 帮助内容文本框
        help_text = tk.Text(win2, font=FONT, wrap=tk.WORD)
        help_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        help_text.insert(tk.END, HELP_TEXT)
        help_text.config(state=tk.DISABLED)  # 设置为只读
        


    button_help = tk.Button(win, text="帮助", command=help)
    button_help.place(x=BUTTON_HELP_POS[0], y=BUTTON_HELP_POS[1])

    
    win.mainloop()
