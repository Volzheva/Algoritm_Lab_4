import time
import os, psutil


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def len(self):
        lenth = len(self.stack)
        return lenth


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("8_input.txt")
m = open("8_output.txt", "w")

a = int(f.readline())
string = f.readline()
elements = list(map(str, string.split()))
num = Stack()
res = 0
for i in elements:
    if i in "+*-":
        if i == "-":
            num1 = int(num.pop())
            num2 = int(num.pop())
            res = num2 - num1
            num.push(res)
        if i == "+":
            res = int(num.pop()) + int(num.pop())
            num.push(res)
        if i == "*":
            res = int(num.pop()) * int(num.pop())
            num.push(res)
    else:
        num.push(i)

m.write(str(res))
f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")