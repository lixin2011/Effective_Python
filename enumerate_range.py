from random import randint

rand_bits = 0
for i in range(32):
    if randint(0, 1):
        rand_bits |= 1 << i
print(bin(rand_bits))
# 0b10110000110101110100110001011110

# range函数很适合迭代一系列整数
# 如果要迭代一个具体的数据结构，不需要设计一个range来获得下标进行迭代，这样代码会比较复杂
flavor_list = ["vanilla", "chocolate"]
for flavor in flavor_list:
    print(f"{flavor} is delicious")
# vanilla is delicious
# chocolate is delicious

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f"{i+1}: {flavor} is delicious")
# 1: vanilla is delicious
# 2: chocolate is delicious

# 如果想要为遍历的元素给出排名，此时就需要使用range获得各自的序号，显得比较复杂

it = enumerate(flavor_list)
print(next(it))
print(next(it))
# print(next(it)) # 无法再迭代
# (0, 'vanilla')
# (1, 'chocolate')

# 可以看出，enumerate函数生成了惰性生成器
# 其会在循环时给出每次对应的循环编号以及对应的值
# 此时实际上可以将其unpacking到两个新的变量中，具体如下

for i, flavor in enumerate(flavor_list):
    print(f"{i + 1}: {flavor} is delicious")
# 1: vanilla is delicious
# 2: chocolate is delicious

for i, flavor in enumerate(flavor_list, 1):
    print(f"{i}: {flavor} is delicious")
# 1: vanilla is delicious
# 2: chocolate is delicious

# 第二个参数可以指定序号开始的位置