"""
第1章 第8条 用zip函数同时遍历两个迭代器
"""


names = ["cecilia", "lise", "marie"]
counts = [len(n) for n in names]
print(counts)
# [7, 4, 5]

# 通过列表推导式来将表达式运用在原始列表的每个元素中

longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count
print(longest_name)
# cecilia

# 以上代码实现了同同时遍历两个列表，names和count
# 从而获得count最大时对应的name
# 此时使用了下标，实际上可以直接使用enumerate

for i,name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)
# cecilia

# 看起来仍然不够简洁

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)
# cecilia

# 直接使用zip函数，其可以将多个可迭代对象封装为生成器
# 每次取用时可以同时从多个迭代器中各自取出一个一组并且组成元组，有点类似于多迭代器unpacking

names.append("rosalind")
for name, count in zip(names, counts):
    print(name, count)
# cecilia 7
# lise 4
# marie 5

# 此处新增的rosalind元素并未循环到
# 注意zip函数最好接受长度相同的迭代器，否则其会因为某个较短的迭代器而提前中止

import itertools

for name, count in itertools.zip_longest(names, counts):
    print(name, count)

# cecilia 7
# lise 4
# marie 5
# rosalind None

# 对于不等长但是又必须进行zip操作的，可以使用itertools.zip_longest
# 此时会强行遍历完成，无法遍历的迭代器则会赋值为默认值


