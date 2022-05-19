# 描述
# 实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

# 数据范围：输入的字符串长度满足 1 ≤ n ≤ 20  ，保证输入的字符串中仅出现小写字母
# 输入描述：
# 字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

# 输出描述：
# 删除字符串中出现次数最少的字符后的字符串。

# 思路：
# step1：输入一组字符串s，同时创建一个新的字典dic；
# step2：遍历字符串s，如果元素在字典里，dic[i]累加次数，否则，dic[i]为1；
# step3：使得MIN为出现最小次数的值；
# step4：重新遍历s，如果i在字典中记录的次数等于MIN，则在原字符串s中用空字符替换；
# step5：输出打印s
s = input()
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
MIN = min(dic.values())
for i in s:
    if dic[i] == MIN:
        s = s.replace(i,'')
print(s)
