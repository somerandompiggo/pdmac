import matplotlib.pyplot as plt
import math

current = 0
target = 0
output = bytearray()

def getdeltabit(current, target):
    if current >= target:
        return False
    if current <= target:
        return True

def makebyte(thebyte):
    pass


def loadsample():
    global current
    global target
    global output
    buffer_size = 1
    with open('blank.raw', 'rb') as f:
        thebyte = []
        while (chunk := f.read(buffer_size)) != b'':
            target = int.from_bytes(chunk, "big")
            if current >= target:
                thebyte.append(False)
            elif current <= target:
                thebyte.append(True)
            print(current)
            if len(thebyte) == 8:
                output.append([int(b) for b in thebyte])
        print(output)
                
            # print(int.from_bytes(chunk, "big"))


loadsample()

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