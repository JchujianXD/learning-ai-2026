# CS50P 学习笔记

## Week 0：Functions, Variables

### 1. 核心主题
函数、变量、数据类型、输入输出、f-string 格式化、注释、伪代码。

### 2. 函数
- 用 `def` 定义函数。
- **参数**：函数接收的输入；**返回值**：用 `return` 返回。
- 没有 `return` 的函数默认返回 `None`。
- **副作用**：如 `print()` 会在屏幕输出，但不产生返回值。
- 推荐入口结构：

```python
def main():
    name = input("What's your name? ")
    print(f"hello, {name}")

if __name__ == "__main__":
    main()
```

### 3. 变量与类型

| 类型 | 含义 | 例子 |
| --- | --- | --- |
| `str` | 字符串 | `"hello"` |
| `int` | 整数 | `42` |
| `float` | 浮点数 | `3.14` |
| `bool` | 布尔值 | `True` / `False` |
| `NoneType` | 空值 | `None` |

- Python 是**动态类型**：变量本身不绑类型，值才有类型。
- 常用类型转换：

```python
int("123")      # 123
float("3.14")   # 3.14
str(123)        # "123"
```

### 4. 字符串与格式化
- 单引号、双引号都可。
- **f-string**：

```python
name = "Alice"
print(f"hello, {name}")
```

- 格式说明符：

```python
price = 1234.5
print(f"{price:.2f}")   # 1234.50，保留两位小数
print(f"{price:,}")     # 1,234.5，千分位
```

- 转义：`\n`、`\t`、`\"`；原始字符串 `r"C:\path"` 不转义。
- 常用字符串方法：

| 方法 | 作用 |
| --- | --- |
| `.strip()` | 去掉两端空白 |
| `.capitalize()` | 首字母大写 |
| `.title()` | 每个单词首字母大写 |
| `.split()` | 按空白切分成列表 |

### 5. 输入输出
- `input()` **永远返回字符串**，要数字需自己转：

```python
x = int(input("x: "))
y = float(input("y: "))
```

- `print()` 常用参数：

```python
print("a", "b", sep=", ")   # a, b
print("hello", end="")      # 不换行
```

### 6. 注释与伪代码
- 单行注释：`#`。
- 三引号字符串可以临时当注释用，但不是真正的注释。
- 写代码前先用伪代码把逻辑写出来，再翻译成 Python。

### 7. 常见错误
| 错误 | 触发场景 |
| --- | --- |
| `ValueError` | 类型对但值不对，如 `int("abc")` |
| `NameError` | 用了未定义的变量名 |
| `TypeError` | 类型不匹配，如 `"1" + 1` |

### 8. 示例

```python
def main():
    name = input("What's your name? ").strip().title()
    print(f"hello, {name}")

if __name__ == "__main__":
    main()
```

---

## Week 1：Conditionals

### 1. 核心主题
布尔值、比较运算、逻辑运算、`if / elif / else`、三元表达式、`match`。

### 2. 布尔与比较
- 布尔值：`True` / `False`。
- 比较运算符：

| 运算符 | 含义 |
| --- | --- |
| `==` | 等于 |
| `!=` | 不等于 |
| `>` `<` | 大于 / 小于 |
| `>=` `<=` | 大于等于 / 小于等于 |

> ⚠️ `=` 是赋值，`==` 才是比较。

### 3. 逻辑运算
- `and`：两边都为真才为真。
- `or`：一边为真就为真。
- `not`：取反。

```python
if x > 0 and x < 10:
    print("x 在 0 到 10 之间")
```

### 4. `if / elif / else`

```python
x = int(input("x: "))

if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

- 缩进是 Python 语法的一部分，4 个空格。
- `elif` 可以有多个；`else` 可选。
- 可以嵌套，但层级不要太深。

### 5. 三元表达式

```python
result = "positive" if x > 0 else "non-positive"
```

### 6. `match` 语句（Python 3.10+）

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

- `_` 表示默认分支；`|` 表示"或"。

### 7. 输入验证常用写法

```python
import sys

x = int(input("x: "))
if x < 0:
    sys.exit("x must be non-negative")
```

`sys.exit("msg")` 会打印消息并终止程序。

### 8. 常见错误
| 错误 | 说明 |
| --- | --- |
| `IndentationError` | 缩进不一致或混用 Tab/空格 |
| 写成 `=` 比较 | 应该用 `==` |
| 浮点数直接 `==` | 用 `math.isclose(a, b)` |

### 9. 总结
- 条件判断先想清楚布尔表达式，再写分支。
- `if/elif/else` 适合有限分支；`match` 适合按值匹配。
- 浮点数比较不要用 `==`。

---

## Week 2：Loops

### 1. 核心主题
`while`、`for`、`range`、`list`、`dict`、循环控制、迭代工具。

### 2. `while` 循环

```python
i = 0
while i < 3:
    print(i)
    i += 1
```

- 条件为真就一直循环，注意避免死循环。
- 常用 `while True + break` 做输入验证：

```python
while True:
    n = int(input("n: "))
    if n > 0:
        break
```

### 3. `for` 循环与 `range`

```python
for i in range(3):
    print(i)          # 0, 1, 2
```

| 写法 | 含义 |
| --- | --- |
| `range(stop)` | 0 ~ stop-1 |
| `range(start, stop)` | start ~ stop-1 |
| `range(start, stop, step)` | 带步长 |

```python
for i in range(1, 4):
    print(i)          # 1, 2, 3
```

### 4. 列表 `list`

```python
students = ["Alice", "Bob", "Charlie"]
students.append("David")

for student in students:
    print(student)
```

- 用 `[]` 创建，`.append()` 末尾追加，`len()` 取长度，索引从 0 开始。

### 5. 字典 `dict`

```python
ages = {"Alice": 20, "Bob": 21}

for name, age in ages.items():
    print(name, age)
```

- 用 `{k: v}` 创建。
- `.keys()` / `.values()` / `.items()` 分别遍历键、值、键值对。

### 6. 循环控制

| 语句 | 作用 |
| --- | --- |
| `break` | 立即跳出整个循环 |
| `continue` | 跳过本次，进入下一次 |
| `pass` | 占位，什么都不做 |

### 7. 常用迭代工具

```python
# enumerate：同时拿索引和值
for i, name in enumerate(students, start=1):
    print(i, name)

# zip：同时遍历多个序列
names = ["Alice", "Bob"]
ages = [20, 21]
for name, age in zip(names, ages):
    print(name, age)

# 列表推导式
squares = [x * x for x in range(5)]
```

> `zip` 以最短的序列为准；需要严格对齐时用 `zip(..., strict=True)`。

### 8. 常见模式
- **累加**：

```python
total = 0
for n in [1, 2, 3]:
    total += n
print(total)
```

- 计数、查找、输入验证。
- `for` 适合已知次数或可迭代对象；`while` 适合"条件不满足就一直跑"。

### 9. 总结
- 能用 `for` 就别用 `while`；`while` 留给条件循环。
- 列表装同类元素，字典装键值对。
- `break / continue / pass` 分工要清楚。

---

## Week 3：Error / Exceptions

### 1. 什么是异常
异常（Exception）是程序运行时发生的错误对象。没被捕获就会终止程序并打印 traceback。

Python 异常层级：大部分内置异常继承自 `Exception`，`Exception` 又继承自 `BaseException`。`KeyboardInterrupt`、`SystemExit` 属于 `BaseException`，一般不要随便捕获。

### 2. 常见内置异常

| 异常 | 含义 | 例子 |
| --- | --- | --- |
| `ValueError` | 类型正确，但值不合适 | `int("abc")` |
| `NameError` | 使用了未定义的名字 | `print(x)`，x 未定义 |
| `TypeError` | 类型不匹配 | `"1" + 1` |
| `IndexError` | 序列下标越界 | `[1, 2][5]` |
| `KeyError` | 字典键不存在 | `{"a": 1}["b"]` |
| `AttributeError` | 对象没有该属性 | `"abc".foo` |
| `ZeroDivisionError` | 除数为 0 | `1 / 0` |
| `FileNotFoundError` | 文件不存在 | `open("no.txt")` |
| `ImportError` / `ModuleNotFoundError` | 导入失败 | `import no_module` |
| `SyntaxError` / `IndentationError` | 语法 / 缩进错误 | 代码写错 |
| `StopIteration` | 迭代器没有更多元素 | `next(iter([]))` |
| `AssertionError` | `assert` 断言失败 | `assert False` |
| `KeyboardInterrupt` | 用户按 Ctrl+C 中断 | — |

简单区分：
- `NameError`：名字找不到。
- `ValueError`：名字找到了，但值不对。
- `TypeError`：类型不对。
- `IndexError` / `KeyError`：下标或键不存在。

> `SyntaxError` / `IndentationError` 在解析阶段就发生，普通 `try/except` 抓不到源码本身的语法错。

### 3. `try / except / else / finally`

```python
try:
    x = int(input("x: "))
except ValueError:
    print("不是整数")
else:
    print(f"x = {x}")
finally:
    print("结束")
```

执行流程：
- `try`：尝试执行代码。
- `except`：发生匹配的异常时进入对应分支。
- `else`：try 里没异常才执行。
- `finally`：无论是否异常都执行，常用于清理资源。

捕获具体异常并拿对象：

```python
try:
    n = int("abc")
except ValueError as e:
    print("值不合法：", e)
```

### 4. `raise`：主动抛出

```python
def get_positive():
    n = int(input("n: "))
    if n <= 0:
        raise ValueError("n 必须为正数")
    return n
```

`raise` 用于主动抛出，让上层去处理，或者让程序尽早、明确地报错。

### 5. `pass` 是什么
`pass` 是空语句，表示"什么都不做"，只用来占位。

```python
try:
    x = int("abc")
except ValueError:
    pass          # 捕获后不处理，继续往下走

def foo():
    pass          # 函数占位，以后再写

class Bar:
    pass          # 空类
```

但**不要**这样写：

```python
try:
    do_something()
except Exception:
    pass          # 把错误吞掉，调试噩梦
```

更推荐：

```python
import logging

try:
    do_something()
except Exception:
    logging.exception("do_something 执行失败")
    raise
```

### 6. 原则
- 能处理的异常才捕获。
- 优先捕获具体异常（如 `ValueError`），不要一上来就 `except Exception`。
- 不要用 `except Exception: pass` 隐藏错误。
- 处理不了就让它继续抛。
- `finally` 留给清理工作（关文件、释放连接）。
- `pass` 只是占位或明确"忽略"，不是真正的错误处理。

---
