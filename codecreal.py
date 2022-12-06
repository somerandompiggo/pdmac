import matplotlib.pyplot as plt
import math


def stepper(current, target):
    if current >= target:
        return False
    if current <= target:
        return True


global current

current = int(1)

graph = []
graphx = []

target = 0

for i in range(64):
    target = int(math.sin(i / 0.2) * 10)
    nowhat = [False, True, True, True, True, False, True, True]
    current = stepper(current, target)
    graph.append(current)

for i in range(64):
    graphx.append(i)

plt.plot(graphx, graph)
plt.show()
