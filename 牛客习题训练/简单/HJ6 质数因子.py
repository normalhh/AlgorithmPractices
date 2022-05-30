"""
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）


数据范围： 1 <= n <= 2 * 10**9 + 14

输入描述：
输入一个整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
"""

import math


n = int(input())
for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        print(i, end=" ")
        n = n // i
if n > 2:
    print(n)
