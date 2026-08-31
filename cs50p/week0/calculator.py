x = float(input("What's x?"))
y = float(input("What's y?"))

z = x / y
print(f"{z:,}")  # 格式化
print(round(z, 2))  # 四舍五入到点后n位 round(number[, n])
print(f"{z:.2f}")  # 作用同上

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")  # 整数除法结果自动变成浮点数
feat: 完成CS50P第0周练习
