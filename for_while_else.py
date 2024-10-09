"""
第1章 第9条 不要在for与while循环后面写else块
"""

# 在python中完成循环后会执行else
# 这比较反直觉，因为try-except-else中try-except执行完成了之后不会执行else
# 但此处执行else的部分
# 这仲写法可以，但是不推荐，因为容易产生歧义，可读性很差

for i in range(3):
    print("loop", i)
else:
    print("else block")

# loop 0
# loop 1
# loop 2
# else block

# 如果循环没有彻底完成（比如循环过程中出现了break），此处就不会执行else部分，

for i in range(3):
    print("loop", i)
    if i == 1:
        break
else:
    print("else block")

# loop 0
# loop 1

# 对空白序列做for循环，会执行else
# 此时循环内的内容并未执行，因为此时的遍历列表为空

for x in []:
    print("never runs")
else:
    print("for else block")

# for else block

# 使用while的时候可以同时使用else，这样循环完成之后仍会执行else

while False:
    print("never runs")
else:
    print("while else block")

# while else block

# 使用else可以喜欢实现搜索逻辑，即完成搜索结果

a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print("testing", i)
    if a % i == 0 and b % i == 0:
        print("not coprime")
        break
else:
    print("coprime")

# testing 2
# testing 3
# testing 4
# coprime

# 判定两个数是否互质
# 判定完成后，如果未发生break，说明未搜索成功，此时通过else给出结论，说明在整个搜索过程中都无结果

