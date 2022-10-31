import re
import os
import pandas as pd
import numpy as np


def rename(old_names, new_names):
    standard_names = pd.read_excel(
        r"C:\Users\Administrator\Desktop\2022级应用气象名单(终).xlsx")
    pass


def main():
    return print("hehe")


if __name__ == '__main__':
    filepath = r"C:\Users\Administrator\Desktop\英语作业练手"
    old_names = os.listdir(filepath)
    # print(old_names[0])\
    # 用正则表达式匹配连续的十二个数字（学号）
    pattern = re.compile(r"\d{12}")
    # 用正则表达式匹配文件类型（其实自己直接枚举出来的）
    pattern1 = re.compile(r".(.doc|.pdf|.docx)$")
    m = []
    n = []
    print(old_names)
    for item in old_names:
        m.extend(pattern.findall(item))
        n.extend(pattern1.findall(item))
        # print(pattern.findall(item))
    # print(n)
    # print(len(m))
    # print(m[1]+n[1])
    m = np.array(m)
    # print(m)
    m = m.astype(np.int64,
                 #  suppress=True
                 )
    # print(m)
    standard_names = pd.read_excel(
        r"C:\Users\Administrator\Desktop\2022级应用气象名单(终).xlsx")
    # print(standard_names.学号)
    # print(standard_names)
    # print(m[0] == standard_names.学号[1])
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
    print(name1)
    # print(name1)
    # for name in name1:
    #     print(pattern.findall(name))
    #     #     # data = os.path.join(filepath, old_names[0])
    #     #     # new_name = os.path.join(filepath, "test")
    #     #     # os.rename(data, new_name)
    #     #     # print(old_names[0])
    #     # main()
