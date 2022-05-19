# 描述
# 某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
# 小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
# 数据范围：输入的正整数满足 1 ≤ n ≤ 100 

# 注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。
# 输入描述：
# 输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。n=0 表示输入结束，你的程序不应当处理这一行。

# 输出描述：
# 对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。

# while True:
#     n=int(input())
#     if n==0:break
#     print(n//2)

# import sys
# data = sys.stdin
# for x in data:
#     x = int(x.strip())
#     if x != 0:
#         print(int(x // 2))
import sys

def f(n):
    if n == 0: return 0
    if n == 1: return 0
    if n >=2: return f(n-2) + 1


if __name__ == '__main__':
    data = sys.stdin
    for x in data:
        x = int(x.strip())
        if x != 0:
            print(f(x))
