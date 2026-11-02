"""
# Python 3.15 里 `print` 是内置函数，写法从 Python 3.0 起没变：
# print(*objects, sep=' ', end='\n', file=None, flush=False)

`sep`、`end`、`file`、`flush` 必须用关键字参数。位置参数会被转成字符串，用 `sep` 拼起来，最后加上 `end`。不传任何对象时，只输出 `end`。返回值是 `None`。

| 参数 | 默认值 | 作用 |
| --- | --- | --- |
| `*objects` | 无 | 要输出的任意个对象 |
| `sep` | `' '` | 对象之间的分隔符，必须是字符串；传 `None` 用默认值 |
| `end` | `'\n'` | 末尾追加的字符串；传 `None` 用默认值 |
| `file` | `None` | 带 `write(string)` 的文本流；`None` 时用 `sys.stdout` |
| `flush` | `False` | 为 `True` 时立刻刷新缓冲区（3.3 起加入） |

```python
print("Hello, world!")
print("a", "b", "c")                 # a b c
print("a", "b", sep="-")             # a-b
print("no newline", end="")
print(*[1, 2, 3], sep=", ")          # 1, 2, 3

import sys
print("error", file=sys.stderr)

with open("out.txt", "w", encoding="utf-8") as f:
    print("hello", file=f, flush=True)
```

二进制文件不能用 `print`，要改用 `file.write(...)`。
"""

