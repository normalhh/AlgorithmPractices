"""
描述
公元五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
现要求你打印出所有花一百元买一百只鸡的方式。

输入描述：
输入任何一个整数，即可运行程序。

输出描述：
 输出有数行，每行三个整数，分别代表鸡翁，母鸡，鸡雏的数量
"""

"""
题目翻译之后的意思是，公鸡一只5元，母鸡一只3元，小鸡三只1元
用100元买100只鸡，给出所有的购买方案
"""

"""
解法1：暴力遍历
实现思路
直观的我们可以看出公鸡最多20只就超出了价格
母鸡最多34只就超出价格
小鸡100只超出了数量范围
因此在这个三个范围内进行暴力遍历尝试，输出符合题目要求的结果即可
时间复杂度为O(n^3)不推荐
"""

# while True:
#     try:
#         ppp = input()
#         for a in range(21):                                                # a 最多买20只
#             for b in range(34):                                            # b 最多买33只
#                 for c in range(101):                                       # c 最多买100只
#                     if a + b + c == 100 and 5*a + 3*b + 1*c/3 == 100:
#                         print(a,b,c)
#     except:
#         break

"""
解法2：数学推导
实现思路
我们假定公鸡、母鸡、小鸡数量为a,b,c
则有 a+b+c=100 , 5a+3b+c/3=100
消去c可知
b = 25-7a/4
因此我么可以知道a必须是4的倍数，而且b如果为正数的话要求a最大只能取3
根据这个结果进行循环遍历，得到输出即可
题解链接：https://blog.nowcoder.net/n/f7253737fb1c4b749c31edb770e457f5?f=comment
时间复杂度O(1)
"""
while True:
    try:
        ppp = input()
        for i in range(4):  # 数学推导，公鸡只能取0，4，8，12只
            a = 4 * i
            b = 25 - 7 * i
            c = 100 - a - b
            print(a, b, c)
    except:
        break
