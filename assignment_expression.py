"""
第1章 第10条 用赋值表达式减少重复代码
"""


fresh_fruit = {
    "apple": 10,
    "banana": 8,
    "lemon": 5,
}
count = fresh_fruit.get("lemon", 0)
if count:
    print(count)
else:
    pass

# count获取了字典中指定的键值
# 此时count变量只在if结构中使用，作为全局变量定义显得有点浪费空间

if count := fresh_fruit.get("lemon", 0):
    print(count)
else:
    pass

# :=为海象操作符，先把右边的值赋值给count变量，随后对自身求值，可以省去中间赋值的步骤
# 此时在if中使用，即可达到：先if判定count是否为空（是否还有柠檬的库存），如果不为空，则使用count获取柠檬对应的库存，用户后续代码块的执行
# 可以看出，海象操作符可以在条件判断和赋值操作符中组合使用，海象操作符的既可以用于条件判断也可以赋值后用于后续代码块的执行

if (count := fresh_fruit.get("apple", 0)) >= 4:
    print(count)
else:
    pass

# 此时count被fresh_fruit.get("apple", 0)赋值，与4进行判断，如果超过4，则可以继续使用count在代码块中操作

pieces = 0
count = fresh_fruit.get("lemon", 0)
if count >= 2:
    pieces = count / 2

# 仅在柠檬拥有2个的时候，才能制作1份柠檬水
# 此处首先初始化柠檬水0份，随后获取柠檬个数
# 柠檬大于等于2个的时候，获得柠檬水份数
# 此时在外部为pieces定义初始值

count = fresh_fruit.get("lemon", 0)

if count >= 2:
    pieces = count / 2
else:
    pieces = 0

# 此处首先获取柠檬个数，当柠檬个数满足最低要求时，获取柠檬水份数，否则柠檬水为0份
# 此处在if语句内为pieces定义初始值

if (count := fresh_fruit.get("lemon", 0)) >= 2:
    pieces = count / 2
else:
    pieces = 0

# 这种方法更为简洁，因为count仅为中间变量，不需要在外侧额外定义，在if语句内定义即可
# pieces才为主要变量，同时此时未在外部初始化，而是在if内部对pieces进行定义，减少了外部变量个数

if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = count / 2
elif (count := fresh_fruit.get("apple", 0)) >= 4:
    pieces = count / 4
elif (count := fresh_fruit.get("lemon", 0)):
    pieces = count
else:
    pass

# 此处实际上实现了python结构的switch-case语句
# 即count作为case的变量，首先对其进行表达式计算，随后复制后进行条件判断，判断可行后则使用count作为值继续执行
# 海象操作符实现了变量赋值和条件判断两个作用

def pick_fruit():
    pass

bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        print(fruit, count)
        bottles.extend(fruit)

# 此处实际上实现了python结构的do-while语句
# 此处while循环中使用 pick_fruit()相当于在每次循环开始的时候对fresh_fruit做了更新（第一次为初始化），相当于do，此时同时也完成了判断


