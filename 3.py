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

def pravilo(line: str):
    symbols = Stack()
    pravda = True
    for i in line:
        if i in "([":
            symbols.push(i)
        if i in ")]":
            if i == ")":
                if symbols.pop() != "(":
                    pravda = False
                    break
            if i == "]":
                if symbols.pop() != "[":
                    pravda = False
                    break

    if pravda and symbols.len():
        return "YES"
    else:
        return "NO"


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("3_input.txt")
m = open("3_output.txt", "w")

num = int(f.readline())
for i in range(num):
    line = f.readline()
    m.write(pravilo(line) + "\n")


f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")