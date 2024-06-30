
# 第一种字符串格式化方法：% 格式化操作符

a = 0b10111011  # 二进制
b = 0xc5f  # 十六进制
print("Binary is %d, hex is %d" % (a, b))
# Binary is 187, hex is 3167

# 此处使用了%d进行十进制的转换，这也是C语言风格的写法

key = "my_var"
value = 1.234
formatted = "%-10s = %.2f" % (key, value)
print(formatted)
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
formatted = template % (name, name)
print(formatted)
# Max loves food. See Max cook.

name = "brad"
formatted = template % (name.title(), name.title())
print(formatted)
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
formatted = "{} = {}".format(key, value) # 使用.format代替%操作符，后续元组元素一一对应
print(formatted)
# my_var = 1.234

formatted = "{:<10} = {:.2f}".format(key, value)  # 此处为可变参数，格式内的冒号为占位，表示需要格式化
print(formatted)
# my_var     = 1.23

# 右缩进10位，同时保留两位小数

print("%.2f%%" % 12.5)  # %表示必须使用转义符
print("{} replaces {{}}".format(1.23))  # {}表示也必须使用转义
# 12.50%
# 1.23 replaces {}

formatted = "{1} = {0}".format(key, value)
print(formatted)
# 1.234 = my_var

# 可以在字符串内的中括号输入索引序号，这样就可以规避之前提到的缺点1：索引顺序的问题，不需要直接一一对应

formatted = "{0} loves food. See {0} cook.".format(name)
print(formatted)
# Max loves food. See Max cook.

# 存在同一个变量需要输入多次时，直接重复输入索引号即可，这样就规避了之前提到的缺点3：重复索引需要多次输入的问题
# format方法仍然存在之前讲的第二个缺点，即需要首先对变量作一些额外格式化（函数调用、类型转换等）的时候，代码会变得十分复杂

menu = {
    "oyster": ["k"]
}
formatted = "first letter is {menu[oyster][0]}".format(menu=menu)
print(formatted)
# first letter is k

# 此时查询了字典中的键值，注意键名不需要加双引号，其本身已经是字符串
# 此时不能直接解决此前提出的缺点4：对于字典，需要多次重复键名才能完成格式化
# format方法比%格式化方法稍微好一点，因为format方法可以直接在字符串的括号内对format后参数的字典或者列表进行索引，而不需要另外单独定义一个字典

# formatted = "first letter is {menu[oyster][0]}".format(menu)
# 以上写法是错误的，format方法只能在字符串内索引format后的形参

# 第3种字符串格式方法：f-string
# 在字符串前面加入“f”作为前缀
# 其克服了上述的缺点4（键名重复的问题），不需要像%格式化中专门定义字典用于索引，也不需要像format方法中专门把值传给某个参数再进行形参索引，
# 其可以直接索引当前python代码那范围内的所有名称，更加简单

key = "my_var"
value = 1.234

formatted = f"{key} = {value}"
print(formatted)
# my_var = 1.234

# 此时直接去除了%或者format函数带来的规则

formatted = f"{key!r:<10} = {value:.2f}"  # !符号用于将值转换为Unicode及repr形式的字符串
print(formatted)
# 'my_var'   = 1.23
# 此时可以直接在中括号内使用之前在format方法使用的:格式化方法

f_string = f"{key:<10} = {value:.2f}"   # 使用f_string方法，索引和格式化都在字符串内

c_tuple = "%-10s = %.2f" % (key, value)  # 使用%操作符，格式化在字符串内，索引在%操作符的参数内

str_args = "{:<10} = {:.2f}".format(key, value)   # 使用format方法，格式化在字符串内，索引在%操作符的参数内

str_kw = "{key:<10} = {value:.2f}".format(key=key, value=value)  # 使用format方法，索引和格式化都在字符串内，此时format后也要添加参数进行形参索引，只能使用形参索引

c_dict = "%(key)-10s = %(value).2f" % {"key": key, "value": value}   # 使用%操作符，索引和格式化都在字符串内，，索引在%操作符的参数内，只能使用字典索引

print(f_string)
print(c_tuple)
print(str_args)
print(str_kw)
print(c_dict)
# my_var     = 1.23

# 可以看出f_string方法最简洁，所有的格式化内容都在括号内进行，外部没有任何其他格式化操作
# 规避了缺点2：键名太多重复问题

a = 1
b = 2
c = 3
print(f"{a}"
      f"{b}"
      f"{c}")
# 123

# 最终结果仍会拼成一行，此处使用了相邻字符串拼接，适用于代码过长的情况

places = 3
numer = 1.23456

print(f"my number is {numer:.{places}f}")
# my number is 1.235

# 变量和表达式也可以出现在括号内的格式字符串内
# f-string可以在括号内任何位置应用表达式或者变量




