# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BinaryTree:
#
#     def __init__(self):
#         self.root = None
#
#     def levelOrder(self):
#         return self._levelOrder(self.root)
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# stack = [root]
#
#
# stack = [root]
# result = []
# while True:
#
#     cur = stack[-1]
#     if cur.left and cur.right:
#         stack.append(cur.right)
#         stack.append(cur.left)
#     else:
#         break
#
# for i in stack:
#     print(i.value)
# num1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
#         'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
# num2 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
# temp = []
#
#
# def n2w(n):
#     word = ''
#     if n // 100 > 0 and n%100!=0:
#         word += num1[n // 100] + ' '
#         word += 'hundred '
#
#         if (n % 100) < 20:
#
#             word += 'and '
#             word += num1[(n % 100)]
#         else:
#             word += 'and '
#             word += num2[(n % 100)//10] + ' '
#             if n %10 != 0:
#                 word += num1[n%10]
#         # elif (n % 100) // 10 == 1:
#         #     word += ' and '
#         #     word += num1[n % 100]
#     elif n // 100 > 0 and n%100==0:
#         word += num1[n // 100] + ' '
#         word += 'hundred '
#     else:
#         if n < 20:
#             word += num1[n]
#         else:
#             word += num2[n // 10] + ' '
#             if n % 10 != 0:
#                 word += num1[n % 10]
#     return word
# print(n2w(int('19')))
# s = '1001001'
# temp = []
# for i in range(0, len(s), 3):
#     temp.append("".join(s[i:i + 3][::-1]))
# print(len(num1))
#
#
# s = '1271919'[::-1]
#
# num1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
#         'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
# num2 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
# temp = []
# res = ''
#
#
# def n2w(n):
#     word = ''
#     if n // 100 > 0 and n % 100 != 0:
#         word += num1[n // 100] + ' '
#         word += 'hundred '
#
#         if (n % 100) < 20:
#
#             word += 'and '
#             word += num1[(n % 100)]
#         else:
#             word += 'and '
#             word += num2[(n % 100) // 10] + ' '
#             if n % 10 != 0:
#                 word += num1[n % 10]
#         # elif (n % 100) // 10 == 1:
#         #     word += ' and '
#         #     word += num1[n % 100]
#     elif n // 100 > 0 and n % 100 == 0:
#         word += num1[n // 100] + ' '
#         word += 'hundred '
#     else:
#         if n < 20:
#             word += num1[n]
#         else:
#             word += num2[n // 10]
#             if n % 10 != 0:
#                 word += " " + num1[n % 10]
#     return word
#
#
# for i in range(0, len(s), 3):
#     temp.append("".join(s[i:i + 3][::-1]))
# temp = temp[::-1]
# print(temp)
# if len(temp) == 3:
#     print(n2w(int(temp[0])) + ' million ' + n2w(int(temp[1])) + ' thousand ' + n2w(int(temp[2])))
# if len(temp) == 2:
#     print(n2w(int(temp[0])) + ' thousand ' + n2w(int(temp[1])))
# if len(temp) == 1:
#     print(n2w(int(temp[0])))
# n = int(input())
# trains = input().strip().split(' ')
#
# res = []
#
#
# def rec_trains(cur_idx, in_trains, out_trains):
#     # 如果原始火车列表的最后一个元素已经进站，此时只能出站，将入站列表中的火车倒序加入出站火车中
#     if trains[-1] in in_trains:
#         res.append(' '.join(out_trains + in_trains[::-1]));
#         print(*in_trains[::-1], '出站');
#         print('出站顺序：', res[-1])
#         # return
#     # 如果进站列表为空，此时只能进站，进站列表加上当前火车，出站列表不变
#     elif in_trains == []:
#         print(trains[cur_idx], '进站');
#         rec_trains(cur_idx + 1, in_trains + [trains[cur_idx]], out_trains)
#     # 否则，就既有可能进站也有可能出站
#     else:
#         # 出站，当前火车索引不变，进站火车列表减去最后一个元素，出站列表加上进站列表刚刚出站的火车
#         print('选A:', in_trains[-1], '出站');
#         rec_trains(cur_idx, in_trains[:-1], out_trains + [in_trains[-1]])
#         # 进站，当前火车索引加1，进站列表加上当前火车，出站列表不变
#         print('选B:', trains[cur_idx], '进站');
#         rec_trains(cur_idx + 1, in_trains + [trains[cur_idx]], out_trains)
#         ## 递归“遍历”本质：利用def下if条件句特点；如果有两个选项会一直循环至验证所有可能解
#
#
# rec_trains(0, [], [])
# res.sort()
# # print('\n'.join(res))
# c = ['reset']
# print(c)
# dic = {'reset':'reset what', 'reset board': 'board fault', 'board add':'where to add', 'board delete':'no board at all', 'reboot backplane':'impossible', 'backplane abort': 'install first'}
# if len(c) == 1:
#     for key in dic.keys():
#         temp = key.split()
#         if len(temp) == 1:
#             if temp[0][:len(c[0])] == c:
#                 print(dic[key])
#             else:
#                 print('unknown command')
# elif len(c) == 2:
#     count = 0
#     for key in dic.keys():
#         temp = key.split()
#         if len(temp) == 2:
#             if temp[0][:len(c[0])] == c[0] and temp[1][:len(c[1])] == c[1]:
#                 count +=1
#             if count == 1:
#                 print(dic[key])
#             else:
#                 print('unknown command')
# else:
#     print('unknown command')
#
# n, ops = int(input()), input()
#
# if n < 4:
#     t = n
# else:
#     t = 4
# u, l, c = 1, t, 1
# for i in ops:
#     if i == 'D':
#         if l == c:
#             l += 1
#             u += 1
#         c += 1
#         if l > n:
#             l = t
#             u = 1
#             c = 1
#     elif i == 'U':
#         if u == c:
#             u -= 1
#             l -= 1
#         c -= 1
#         if u < 1:
#             u = n-(l-u)
#             l = n
#             c = n
# lst = [str(i) for i in range(u, l+1)]
# print(' '.join(lst))
# print(c)
# dic = {0:1,1:2,2:3,3:4,4:5,5:6}
# print(dic)
# del dic[0]
# print(dic)
# from collections import Counter
# print(Counter('abc'))
# print(Counter())
# nums = [1, 2, 5]
# def canPartition(nums):
#     target = sum(nums)
#     if target % 2 == 1:
#         return False
#     target //= 2
#     dp = [0] * (target + 1)
#     for i in range(len(nums)):
#         for j in range(target, nums[i] - 1, -1):
#             dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
#     print(dp)
#     return dp[target] == target
# canPartition(nums)
# import os
# import shutil
#
# source_dir = '/Users/chonglu/PycharmProjects/LeetCode'
# destination_dir = '/Users/chonglu/PycharmProjects/LeetCode/Dynamic Programming'
# files_to_move = ['509.py', '70.py', '746.py', '62.py', '63.py','343.py', '96.py', '416.py', '1049.py', '494.py', '474.py','518.py', '377.py', '322.py', '279.py', '139.py','198.py', '213.py', '337.py', '121.py','122.py', '123.py','188.py', '309.py', '714.py','300.py', '674.py', '718.py','1143.py', '1035.py', '392.py','115.py', '583.py','72.py','647.py', '516.py']
# for file in files_to_move:
#
#     file_path = os.path.join(source_dir, file)
#     if os.path.exists(file_path):
#         shutil.move(file_path, destination_dir)
#     else:
#         continue



