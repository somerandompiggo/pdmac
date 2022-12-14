import matplotlib.pyplot as plt
import math

current = 0
target = 0

def getdeltabit(current, target):
    if current >= target:
        return False
    if current <= target:
        return True

# with open('blank.raw', 'rb') as f:
#         while (chunk := f.read(1)) != b'':
#             input.append(int.from_bytes(chunk, "big"))

outputfile = open('output.raw', "wb")

# for i in input:
#     target = input[i]
#     byteout = []
#     # output.append(getdeltabit(current, target))
#     for i in range(8):
#         if current >= target:
#             current -= 1
#             byteout.append(False)
#         elif current <= target:
#             current += 1
#             byteout.append(True)
#     outputfile.write(int.to_bytes(int(''.join(['1' if i else '0' for i in byteout]), 2), 1, "big"))
# outputfile.close()
    

# code graveyard

# def makebyte(thebyte):
#     pass

buffer_size = 1
with open('blank.raw', 'rb') as f:
    while (chunk := f.read(buffer_size)) != b'':
        target = int.from_bytes(chunk, "big")
        byteout = []
        # output.append(getdeltabit(current, target))
        for i in range(8):
            if current >= target:
                current -= 1
                byteout.append(False)
            elif current <= target:
                current += 1
                byteout.append(True)
        outputfile.write(int.to_bytes(int(''.join(['1' if i else '0' for i in byteout]), 2), 1, "big"))
    outputfile.close()

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
