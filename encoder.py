import matplotlib.pyplot as plt
import math

current = 0
target = 0
input = []
output = []

def getdeltabit(current, target):
    if current >= target:
        return False
    if current <= target:
        return True

with open('blank.raw', 'rb') as f:
        while (chunk := f.read(1)) != b'':
            input.append(int.from_bytes(chunk, "big"))

for i in input:
    target = input[i]
    # output.append(getdeltabit(current, target))
    if current >= target:
        current -= 1
    elif current <= target:
        current += 1

# code graveyard

# def makebyte(thebyte):
#     pass


# def loadsample():
#     global current
#     global target
#     global output
#     buffer_size = 1
#     with open('blank.raw', 'rb') as f:
#         thebyte = []
#         while (chunk := f.read(buffer_size)) != b'':
#             target = int.from_bytes(chunk, "big")
#             if current >= target:
#                 thebyte.append(False)
#             elif current <= target:
#                 thebyte.append(True)
#             print(current)
#             if len(thebyte) == 8:
#                 output.append()
                
#             print(int.from_bytes(chunk, "big"))


# loadsample()

# global current

# current = int(1)

# graph = []
# graphx = []

# target = 0

# for i in range(64):
#     target = int(math.sin(i / 0.2) * 10)
#     nowhat = [False, True, True, True, True, False, True, True]
#     current = stepper(current, target)
#     graph.append(current)

# for i in range(64):
#     graphx.append(i)

# plt.plot(graphx, graph)
# plt.show()
