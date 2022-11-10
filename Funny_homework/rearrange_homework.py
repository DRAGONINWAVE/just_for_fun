import re
import os
import pandas as pd
import numpy as np


def rename(old_names, standard_names, path):
    # print(old_names[0])\
    # 用正则表达式匹配连续的十二个数字（学号）
    pattern = re.compile(r"\d{12}")
    # 用正则表达式匹配文件类型（其实自己直接枚举出来的）
    pattern1 = re.compile(r".(.doc|.pdf|.docx|.zip|.rar)$")
    # 匹配两种学号和文件类型
    m = []
    n = []
    print(old_names)
    for item in old_names:
        m.extend(pattern.findall(item))
        n.extend(pattern1.findall(item))
    # 将学号全部转化为int64格式
    m = np.array(m)
    m = m.astype(np.int64,
                 )
    # 匹配生成标准的命名格式
    i = 0
    j = 0
    name1 = []
    handled = []
    for name in m:
        j = 0
        for names in standard_names.学号.values:
            # i =
            if names == name:
                name1.append(
                    str(standard_names.学号[j])+"-"+standard_names.姓名[j]+"-" + "英语作业3"+n[i])
                handled.append(standard_names.姓名[j])
            j = j + 1
        i = i + 1
    i = 0
    # 替换文件名
    for name in name1:
        data = os.path.join(path, old_names[i])
        # print(data)
        new_name = os.path.join(path, name)
        print(data, new_name)
        os.rename(data, new_name)
        i = i + 1
        # print(old_names[0])

    return handled


def not_handled(new, standard_names):
    heihei = []
    for name in standard_names:
        if name not in new:
            heihei.append(name)
    return heihei


def main():
    # 读取标准的名单
    standard_names = pd.read_excel(
        r"C:\Users\Administrator\Desktop\2022级应用气象名单(终).xlsx")
    # 读取需要修改的文件名
    filepath = r"C:\Users\Administrator\Desktop\英语作业3test"
    old_names = os.listdir(filepath)
    new = rename(old_names, standard_names, filepath)
    print(len(new))
    heihei = not_handled(new, standard_names.姓名)
    print(heihei)


if __name__ == '__main__':
    main()
