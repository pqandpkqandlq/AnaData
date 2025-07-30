'''
欧呀，你发现了一个配置文件
这个配置文件里面有很多常量
他可以用来设置AnaData的各种参数
你可以用
from Settings import *
来调用这个配置文件（谁会调用一堆没有的坐标啊）
lib.py表示这个文件是他的义父
我也不知道这个文件对他有什么用
但是我知道这个文件对AnaData.py有什么用
可是过往的勇士用实践和惨痛的教训告诉我们
AnaData.py调用会炸
但是lib.py不会
我不明白
但是我知道
你
不要乱改！不要乱改！不要乱改！
不要删除！不要删除！不要删除！
别像lsy这个大sb一样不写注释！
别像lsy这个大sb一样不写注释！
别像lsy这个大sb一样不写注释！

last update:2025.7.30 Nahidog(lsy)
'''
#PRODUCT INFORMATION
TITLE="AnaData"
VERSION="T1.2"    #R:release,T:test
#SYSTEM
GEOMETRY="500x600"
ENCODINGS=("utf-8","gbk","gb2312","iso-8859-1")
#GUI
FONT=("微软雅黑",10)
LABEL_GETWAYS_POS=(0,0)
OPTIONMENU_GETWAYS_POS=(100,0)
LABEL_FILEPATH_POS=(0,30)
ENTRY_FILEPATH_POS=(100,30)
BUTTON_FILEPATH_POS=(250,30)
LABEL_GETDATACONDITION_POS=(0,120)
LABEL_GETURL_POS=(0,30)
ENTRY_GETURL_POS=(100,30)
LABEL_USERAGENT_POS=(0,60)
ENTRY_USERAGENT_POS=(100,60)
BUTTON_USERAGENT_POS=(250,60)
DEFAULT_USER_AGENT="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36 Edg/132.0.0.0"
LABEL_SAVEASOTHERPATH_POS=(0,90)
ENTRY_SAVEASOTHERPATH_POS=(100,90)
BUTTON_SAVEASOTHERPATH_POS=(250,90)
BUTTON_TEMP_POS=(300,90)


LABEL_DATAANALYSE_POS=(0,150)
LABEL_TYPEZONE_POS=(100,150)
LABEL_REZONE_POS=(300,150)
TEXT_TYPEZONE_POS=(60,180)
TEXT_REZONE_POS=(210,180)
LABEL_DATAANALYSECONDITION_POS=(0,390)
BUTTON_START_POS=(0,200)
# 文本框尺寸设置
TEXT_TYPEZONE_WIDTH = 140
TEXT_TYPEZONE_HEIGHT = 200
TEXT_REZONE_WIDTH = 290
TEXT_REZONE_HEIGHT = 200

LABEL_DATAEXPORT_POS=(0,450)
LABEL_SAVETO_POS=(100,450)
ENTRY_SAVETO_POS=(150,450)
BUTTON_SAVETO_POS=(300,450)
BUTTON_SAVEASEXCEL_POS=(100,480)
BUTTON_SAVEASTXT_POS=(100,510)
LABEL_EXPORTCONDITION_POS=(0,540)

YELLOW="#9B870C"


LABEL_HELP_POS=(0,600)
BUTTON_HELP_POS = (0, 250)  # 帮助按钮位置
#TEXT
HELP_TEXT="""
        AnaData 使用指南
        
        1. 数据获取
        - 从本地获取: 选择本地文本文件进行分析
        - 从网络获取: 输入URL获取网页内容
        
        2. 数据分析
        - 类型区: 输入要提取的数据类型(每行一个类型)
        - 表达式区: 输入对应的正则表达式(每行一个)
        
        3. 数据导出
        - 保存为Excel: 将分析结果导出为Excel文件
        - 保存为TXT: 将分析结果导出为文本文件

        正则表达式:
        - 字符   数字：\\d    字母：[a-zA-Z]   汉字：[\\u4e00-\\u9fa5]  任意字符：.  
        - 量词   重复: *   一个及以上: +  范围: {m,n}    0或1个: ?
        - 匹配   捕获组: ()   尽可能少匹配: 量词后接?   非捕获组(?: )
        - 判定   或: |    边界: \\b  开头: ^  结尾: $
        - 转义   转义字符: \\  换行: \\n  制表符: \\t  反斜杠:\\
        
        示例:
        - 邮箱: [a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+
        - 手机号: 1\d{10}
        - 时间: \d{4}年\d{1,2}月\d{1,2}日
        - 结合上下文: 前面的内容(表达式)后面的内容
        """