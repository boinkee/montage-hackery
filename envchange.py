import argparse, re, sys

p = argparse.ArgumentParser()
p.add_argument('infile'); p.add_argument('outfile')
p.add_argument('--bootcmd', help='new value for bootcmd (must fit in the old one: ~600 bytes)')
a = p.parse_args()

d = bytearray(open(a.infile, 'rb').read())

def find_one(key):
    offs = [m.start() for m in re.finditer(re.escape(key), bytes(d))]
    return offs

if a.bootcmd is not None:
    offs = find_one(b'bootcmd=')
    if len(offs) != 1:
        sys.exit('expected exactly one "bootcmd=" in the image, found %d' % len(offs))
    o = offs[0]
    end = d.index(0, o)
    room = end - (o + len(b'bootcmd='))
    new = a.bootcmd.encode()
    if len(new) > room:
        sys.exit('bootcmd is %d bytes but only %d fit' % (len(new), room))
    d[o + 8:end] = new.ljust(room, b' ')
    print('bootcmd patched at %#x (%d of %d bytes used)' % (o, len(new), room))

open(a.outfile, 'wb').write(d)
print('wrote', a.outfile, len(d), 'bytes')
