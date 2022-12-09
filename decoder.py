import os

def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] >> shift) & 0x1

bytereal = b'1'
current = 0

outfile = open("decoded.raw", "wb")

buffer_size = 1
with open('output.raw', 'rb') as f:
    while (chunk := f.read(buffer_size)) != b'':
        for i in range(8):
            if access_bit(chunk, i) == 0:
                current -= 1
            elif access_bit(chunk, i) == 1:
                current += 1
            try:
                outfile.write(int.to_bytes(current, 1, "big"))
            except:
                outfile.write(int.to_bytes(current + 1, 1, "big"))