import re
import os
import pandas as pd
import numpy as np


def rename(old_names, standard_names, path):
    # print(old_names[0])\
    # 用正则表达式匹配连续的十二个数字（学号）
    pattern = re.compile(r"\d{12}")
    # 用正则表达式匹配文件类型（其实自己直接枚举出来的）
    pattern1 = re.compile(r".(.doc|.pdf|.docx)$")
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
    for name in m:
        j = 0
        for names in standard_names.学号.values:
            # i =
            if names == name:
                name1.append(
                    str(standard_names.学号[j])+standard_names.姓名[j]+n[i])
            j = j + 1
        i = i + 1
    i = 0
    # 替换文件名
    for name in name1:
        data = os.path.join(path, old_names[i])
        # print(data)
        new_name = os.path.join(path, name)
        # print(data, new_name)
        os.rename(data, new_name)
        i = i + 1
        # print(old_names[0])

    return print(name1)


def main():
    # 读取标准的名单
    standard_names = pd.read_excel(
        r"C:\Users\Administrator\Desktop\2022级应用气象名单(终).xlsx")
    # 读取需要修改的文件名
    filepath = r"C:\Users\Administrator\Desktop\英语作业练手"
    old_names = os.listdir(filepath)
    rename(old_names, standard_names, filepath)


if __name__ == '__main__':
    main()

    # print(name1)
    # for name in name1:
    #     print(pattern.findall(name))
    #     #     # data = os.path.join(filepath, old_names[0])
    #     #     # new_name = os.path.join(filepath, "test")
    #     #     # os.rename(data, new_name)
    #     #     # print(old_names[0])
    #     # main()
