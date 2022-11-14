import time
import os, psutil


def add_element(queue, val):
    queue.append(val)


def remove_element(queue):
    delete = queue.pop(0)
    return delete


def find_min_element(queue):
    return min(queue)


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("6_input.txt")
m = open("6_output.txt", "w")

queue = []
count = int(f.readline())
for i in range(count):
    string = f.readline()
    elements = list(map(str, string.split()))
    if elements[0] == "+":
        add_element(queue, int(elements[1]))
    if elements[0] == "-":
        remove_element(queue)
    if elements[0] == "?":
        m.write(str(find_min_element(queue))+"\n")


f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")