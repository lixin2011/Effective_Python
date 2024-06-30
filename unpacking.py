snack_calories = {
    "chips": 140,
    "popcorn": 80,
    "nuts": 190,
}
items = tuple(snack_calories.items())  # items()返回key和value构成的元组
print(items)
# (('chips', 140), ('popcorn', 80), ('nuts', 190))

item = ("peanut butter", "jelly")
first = item[0]
second = item[1]
print(first, "and", second)
# peanut butter and jelly

# 可以使用数组下标来获取数组的某个值

pair = ("chocolate", "peanut butter")
# pair[0] = "honey"
# 此处会报错，因为元组并不支持索引来进行值的修改

item = ("peanut butter", "jelly")
first, second = item  # 此处进行unpacking
print(first, "and", second)
# peanut butter and jelly

# 元组不能直接被赋值，也即使用元组下标的方式来进行数值修改
# 但可以使用unpacking的方式将元组元素赋值给其他变量，此时再对其他变量数值修改
# 间接完成了数据的修改
# unpacking的赋值操作符左侧也可以是列表等可迭代对象

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                # 常规写法
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp
                # unpacking写法
                a[i-1], a[i] = a[i], a[i-1]

names = ["pretze", "carrots", "argula", "bacon"]
bubble_sort(names)
print(names)
# ['argula', 'bacon', 'carrots', 'pretze']

# 此处实际上为字符本身的升序排序，两值遍历对比，若为降序则交换顺序
# 对于常规写法，交换时，首先将右值赋值给临时变量，再将右值赋值给左值，随后再将临时变量代表的右值赋值给左值
# 复杂的主要原因是交换是依次进行的，如果直接赋值将会丢失原值，必须借助中间变量，否则无法完成交换
# 对于unpacking写法，此处对左侧两个变量赋值，python会首先计算右侧两个表达式的值并且将结果放在临时元组内，此时作用就类似于临时变量temp
# 完成左侧赋值后，该临时元组就会被丢弃

snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]

# 使用下标索引，由于此处列表元素为元组，需要进行两层索引，较为复杂
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f"{name}: {calories}")

# 使用enumerate和unpacking，此时直接使用多元素赋值，取出列表内的元组，更加简单
for rank, (name, calories) in enumerate(snacks):
    print(f"{name}: {calories}")

# bacon: 350
# donut: 240
# muffin: 190

# 使用unpacking方式来替代下标索引的方式，也就是当元素为指定长度的可迭代对象时，直接将其匹配相同长度的赋值变量进行unpacking，更加高效
# 而不是使用其长度和range函数来依次索引

