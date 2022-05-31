"""
描述
将一个字符中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。

数据范围：字符串长度满足 1 ≤ n ≤ 100

输入描述：
输入一个字符串

输出描述：
字符中所有出现的数字前后加上符号“*”，其他字符保持不变
"""

# while True:
#     try:
#         s = input()
#         s_o = ''
#         char_pre = ''
#         for i in s: #遍历字符串
#             if i.isdigit() : #遇到数字，判断其前面是否非数字，是则表示数字的开始，先插入‘*’
#                 if char_pre.isdigit() != True:
#                     s_o +='*'
#             else: #非数字情况，判断其前是否为数字，是则表示数字结束，插入‘*’
#                 if char_pre.isdigit():
#                     s_o +='*'
#             s_o += i #把当前字符带出来
#             char_pre = i #当前字符更新到 前字符
#         if i.isdigit(): #结束的时候，判断是否数字结束，如果是的话，插入‘*’
#             s_o +='*'
#         print(s_o)
#     except:
#         break


import re

while True:
    try:
        print(re.sub("(\d+)", "*\g<1>*", input()))
    except:
        break
