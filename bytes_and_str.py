a = b'h\x65llo'
print(list(a))
# [104, 101, 108, 108, 111]

# list方法可以直接展示其原始的元素
# a为bytes形式，使用列表获取，此时为原始数据，即8位的ASCII码（此时为十进制），也叫码点，对应着文本字符
print(a)
# b'hello'

# 以字符串的形式打印，此时仍以二进制的形式进行了输出

a = "a\u0300 propos"
print(list(a))
# ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']

# a为str形式，使用列表获取，此时即为字符串的每个元素
print(a)
# à propos

# 以字符串的形式打印，此时以字符串的形式进行了输出


# 使用str类型来表示unicode数据，而不是二进制码，这样可以实现编码的统一
def to_str(byte_or_str):
    if isinstance(byte_or_str, bytes):  # 检查是否为bytes类型
        value = byte_or_str.decode('utf8')  # 使用bytes的解码decode方法，将其转换为utf-8形式
    else:
        value = byte_or_str  # 非bytes形式则不作转换
    return value

print(repr(to_str(b"foo")))
# 'foo'

# 输入bytes形式，进行了解码为unicode，输出则为常规的字符串
print(repr(to_str("bar")))
# 'bar'

# repr() 方法可以将读取到的格式字符，比如换行符、制表符，转化为其相应的转义字符。

# 将str元素编码为utf-8的二进制编码
def to_bytes(byte_or_str):
    if isinstance(byte_or_str, str):
        value = byte_or_str.encode('utf8')
    else:
        value = byte_or_str
    return value

print(to_bytes(b"foo"))
print(to_bytes("bar"))
# b'foo'
# b'bar'

# 两者均返回bytes元素

print(b"one" + b"two")
print("one" + "two")
# b'onetwo'
# onetwo

# bytes和str格式自身相互合并，但是不能互相合并

print(b"foo" == "foo")
# False

# 两者并不相等，因为其本身类型不同

print(b"red %s" % b"blue")
print("red %s" % "blue")
# b'red blue'
# red blue

# %为格式化操作符，用于将右侧的字符串格式化（按照%s）后替换左侧的格式字符串

# print(b"red %s" % "blue")
# 此处会报错，因为"blue"按照%s要求格式化为str，其不会转换为bytes形式，但是其处于一个bytes数据中，会出错
print(b"red %b" % b"blue")
# b'red blue'

print("red %s" % "blue")
# red blue

print("red %s" % b"blue")
# red b'blue'

# 这样做又可以，因为b"blue"按照%s要求格式化为str，此时会调用__repr__方法，此时会直接将二进制表示符号b转换为str形式
# 此时b"blue"就转换为str形式的b"blue"，可以和”red“同时存在

# with open("data.bin", "w") as f:
#     f.write(b"\xf1\xf2\xf3\xf4\xf5")

# 此时向文件对象写入二进制数据
# 但文件对象为w写入，即必须要以文本模式写入，则会出错

with open("data.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")

# 此时以二进制形式输入，同时文件对象为二进制

# with open("data.bin", "r") as f:
#     f.read()

# 此时data.bin为二进制编码的数据。此时以文本模式进行读取二进制数据
# 系统会使用bytes的decode方法把数据解码为str字符串（文件数据本质为二进制，需要解码），再使用str的encode方法将数据编码成二进制（字符串在内存中通过二进制读取，需要编码）
# 一般系统会使用默认的utf-8文本编码，此时会将b"\xf1\xf2\xf3\xf4\xf5"当作utf-8字符串解码，会报错


with open("data.bin", "rb") as f:
    f.read()

# 以二进制对象读取二进制数据

with open("data.bin", encoding="cp1252") as f:
    f.read()

# 直接指定解码的方案