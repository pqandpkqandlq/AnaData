'''
恭喜你，你找到了一个库
这个库存放了一个武林秘籍
里面有很多函数
你在包含AnaData.py、lib.py、Settings.py的文件夹下
import AnaData
来学习该秘籍
你将获得以下法术：
（自己看源码去，都写得这么规范（并非）了，少点注释怎么了，你的vscode又不是notepad）
这可以用来获取数据，分析数据，导出数据
没错，AnaData.py是这个库的第一个使用者
我相信你会成为下一个库的使用者
你也可以对这个库完善，让它变得更好（或者更屎）
请注意：
不要乱改！不要乱改！不要乱改！
不要删除！不要删除！不要删除！

last update:2025.7.30 Nahidog(lsy)
'''
from Settings import * 
import re
import requests
import os
from pandas import DataFrame
def get_on_Internet(url:str,user_agent:str=""):
    headers = {
        'User-Agent': user_agent
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    return [response.status_code,response.text]

def get_on_local(file_path:str):
    '''
    -1  file not found
    2  decode error
    114  path error
    2  unknown error
    '''
    
    if not os.path.exists(file_path):
        #print(f"路径 {file_path} 不合法。")
        return 114
    for i in range(len(ENCODINGS)):
        try:
            with open(file_path,'r',encoding=ENCODINGS[i]) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            return -1
        except Exception:
            return 1
    return 2

        
    

def analyse_data(types:list,text,REs:list):
    analysed_data=[]
    max_length = 0
    # 先收集所有匹配结果并记录最大长度
    for i in REs:
        matches = re.findall(i, text)
        analysed_data.append(matches)
        max_length = max(max_length, len(matches))
    
    # 统一结果长度，不足的填充空字符串
    for i in range(len(analysed_data)):
        if len(analysed_data[i]) < max_length:
            analysed_data[i] += [''] * (max_length - len(analysed_data[i]))
    
    # 生成字典
    result_dict = {t: d for t, d in zip(types, analysed_data)}
    return DataFrame(result_dict)

def save_file(text:str,path:str):
    with open(path,'w',encoding='utf-8') as file:
        file.write(text)
def export_data_as_excel(data_frame:DataFrame, file_path:str):
    data_frame.to_excel(file_path, index=False)
def export_data_as_txt(data_frame:DataFrame, file_path:str):
    data_frame.to_csv(file_path, index=False, sep='\t')
