"""
第1章 第5条 用辅助函数取代复杂的表达式
"""

from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=0&green=",
                     keep_blank_values=True)
print(repr(my_values))
# {'red': ['5'], 'blue': ['0'], 'green': ['']}

print("red： ", my_values.get("red"))
print("red： ", my_values.get("green"))
print("red： ", my_values.get("opacity"))

# red：  ['5']
# red：  ['']
# red：  None

red = int(my_values.get("red", [""])[0] or 0)   # get函数的第二个表示默认值
green = int(my_values.get("green", [""])[0] or 0)
opacity = int(my_values.get("opacity", [""])[0] or 0)

print(f"red: {red}, green: {green}, opacity: {opacity}")
# red: 5, green: 0, opacity: 0

# 此处使用了布尔表达式：x or y，当x为空白字符串、空白列表、0值时，会自动替换为默认值y

red_str = my_values.get("red", [""])[0]
red = int(red_str[0]) if red_str[0] else 0
print(red)
# 5

# 作用等同于x if condition else y，其相比于if或者函数表达式更加简洁，因为此处最后的接收结果为逻辑值，但是会减弱代码可读性

def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default

green = get_first_int(my_values, "green")
print(green)
# 0

# 如果发现表达式越写越复杂，那就应该拆分为多个部分，以提升代码的可读性
# 始终遵循一个原则，即不要重复自己写过的代码




