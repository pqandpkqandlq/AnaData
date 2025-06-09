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

def get_on_local(file_path:str):#有人解决这个函数解码失败的问题吗-lsy 2025.6.8

    
    if not os.path.exists(file_path):
        #print(f"路径 {file_path} 不合法。")
        return 114
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:  # 比通用 Exception 更具体
        #print(f"文件 {file_path} 不存在。")
        return -1
    except UnicodeDecodeError as ude:
        #print(f"解码失败: {ude}")
        return 2
    except Exception as e:
        #print(f"未知错误: {e}")
        return 1

def analyse_data(types:list,text,REs:list):#最终合成的DF莫名其妙少掉最后一个数据，谁来-lsy 2025.6.8
    analysed_data=[]
    max_length = 0
    # 先收集所有匹配结果并记录最大长度
    for i in REs:
        matches = re.findall(i, text)
        analysed_data.append(matches)
        max_length = max(max_length, len(matches))
    
    # 统一结果长度，不足的填充空字符串
    for i in range(len(analysed_data)):
        analysed_data[i] += [''] * (max_length - len(analysed_data[i]))
    
    # 生成字典
    result_dict = {t: d for t, d in zip(types, analysed_data)}
    return DataFrame(result_dict)

def export_data_as_excel(data_frame:DataFrame, file_path:str):
    data_frame.to_excel(file_path, index=False)
def export_data_as_txt(data_frame:DataFrame, file_path:str):
    data_frame.to_csv(file_path, index=False, sep='\t')
