
# 第一种字符串格式化方法：% 格式化操作符

a = 0b10111011  # 二进制
b = 0xc5f  # 十六进制
print("Binary is %d, hex is %d" % (a, b))
# Binary is 187, hex is 3167

# 此处使用了%d进行十进制的转换，这也是C语言风格的写法

key = "my_var"
value = 1.234
formated = "%-10s = %.2f" % (key, value)
print(formated)
# my_var     = 1.23
# %-10s 字符串右侧缩进10位
# %.2f 浮点数保留两位小数

# formated = "%-10s = %.2f" % (value, key)
# 缺点1：当后续元组发生了顺序调换，就会报错。该方法每次都需要手动检查，保证前后顺序一一准确对应


pantry = [
    ("avocados", 1.25),
    ("bananas", 2.5),
    ("cherries", 15),
]

for i, (item, count) in enumerate(pantry):  # enumerate：获得索引及其对应元素
    print("#%d: %-10s = %.2f" % (i, item, count))
# 0: avocados   = 1.25
# 1: bananas    = 2.50
# 2: cherries   = 15.00

# 如果相对数据作一些额外的格式化
for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %.2f" % (
        i+1,
        item.title(),
        round(count)))
# 1: Avocados   = 1.00
# 2: Bananas    = 2.00
# 3: Cherries   = 15.00

# 缺点2：由于%针对数据作的格式化操作十分有限，此处使用了外部方法在打印时进行了格式化，但是可读性变得很差

template = "%s loves food. See %s cook."
name = "Max"
formated = template % (name, name)
print(formated)
# Max loves food. See Max cook.

name = "brad"
formated = template % (name.title(), name.title())
print(formated)
# Brad loves food. See Brad cook.

# 缺点3：如果只是相对1个变量进行修改，但%操作符号后的元组拥有多个重复变量时，需要全部修改，十分耗时

# 如何不在%后的元组重复书写某一个相同变量，此时可以使用字典

key = "my_var"
value = 1.234
old_way = "%-10s = %.2f" % (key, value)
print(old_way)
new_way = "%(key)-10s = %(value).2f" % {"key": key, "value": value}
print(new_way)
reordered = "%(key)-10s = %(value).2f" % {"value": value, "key": key}
print(reordered)
# my_var     = 1.23

# 此处使用字典的键值来进行数据索引
# %后的字典内元素可随意调换顺序，解决了缺点1（不可随意调换顺序）
# 若字符串内的元素引用多次，%后的字典内元素格式化只需要对一个元素进行操作，解决了缺点3（多个元素需要重复多个操作）
# 三者的输出结果相同

name = "Max"

template = "%s loves food. See %s cook."
before = template % (name, name)
print(before)

template = "%(name)s loves food. See %(name)s cook."
after = template % {"name": name}
print(after)

# 使用字典作为%操作符的后续元素衍生出了缺点4，代码太过于复杂，仅仅打印元素如此复杂是得不偿失的
# 每个键至少写两次（一次在字符串内，一次在字典内），同时还可能有一次（即值对应的变量），这样最多可能达到3次
# 同时使用字典，将会使得代码变得非常长
# 因此，缺点2和缺点4是无法避免的

# 第二种字符串格式化方法：format函数或者方法
# 函数第一个输入为字符串，第二个输入为格式字符串
# 方法则为str的format方法

# 函数
a = 1234.5678
formatted = format(a, ',.2f') # 此处逗号表示显示千分位符号
print(formatted)
# 1,234.57

b = "my string"
formatted = format(b, '^20s') # 此处^表示居中对齐，20表示字符串缩进
print("*", formatted, "*")
# *      my string       *

# 方法
key = "my_var"
value = 1.234
formated = "{} = {}".format(key, value) # 使用.format代替%操作符，后续元组元素一一对应
print(formated)
# my_var = 1.234

