import struct, sys

if len(sys.argv) != 3:
    sys.exit('usage: autobootpatch.py in.bin out.bin')

d = bytearray(open(sys.argv[1], 'rb').read())

# prologue of the function (0x801167ec in the 2019 build)
sig = struct.pack('<8I', 0x3c1c0003, 0x279ca554, 0x0399e021, 0x27bdffe0,
                  0xafbf001c, 0xafb00018, 0xafbc0010, 0x00808021)
offs = [i for i in range(0, len(d) - len(sig)) if d[i:i+len(sig)] == sig]
if len(offs) != 1:
    sys.exit('function signature found %d times (need exactly 1); wrong U-Boot build?' % len(offs))
f = offs[0]

# (offset from function start, expected old word, new word)
patches = [
    (0x44, 0x00000000, 0x00008021),   # nop > move s0,zero
    (0x58, 0x00000000, 0x24100001),   # nop > li   s0,1
    (0x9c, 0x24020001, 0x02001021),   # li v0,1 > move v0,s0
]
for off, old, new in patches:
    cur = struct.unpack_from('<I', d, f + off)[0]
    if cur != old:
        sys.exit('unexpected word %#010x at +%#x (expected %#010x); not patching' % (cur, off, old))
for off, old, new in patches:
    struct.pack_into('<I', d, f + off, new)

open(sys.argv[2], 'wb').write(d)
print('patched function at file offset %#x, wrote %s' % (f, sys.argv[2]))
