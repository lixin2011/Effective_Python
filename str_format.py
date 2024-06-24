
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
# 缺点1：当后续元组发生了顺序调换，就会报错。该方法每次都需要手动检查