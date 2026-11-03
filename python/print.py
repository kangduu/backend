# https://docs.python.org/zh-cn/3/builtins/functions.html#print

import sys
print("error", file=sys.stderr)

with open("out.txt", "w", encoding="utf-8") as f:
    print("hello", file=f, flush=True)

print("Hello, world!")
print("a", "b", "c")                  
print("a", "b", sep=None)              
print(1, 2, 3) 
print("no newline", end="")
print([1, 2, 3], sep=", ")
print("error", file=None)
