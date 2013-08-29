"""
Split an image per colors
"""



import sys
import subprocess as sub

from PIL import Image

xpm = sys.argv[1]
png = xpm + '.png'

sub.call(['convert',xpm,png])

source = Image.open(png)

try:
    prefix = sys.argv[2]
except Exception:
    prefix = 'OUT_'

w = source.size[0]
h = source.size[1]
data = source.load()

out = {}

rh = range(h)
rh.reverse()
for y in rh:
    dbg = []
    for x in range(w):
        px = source.getpixel((x,y))
        dbg.append(unichr(px))
        if px not in out:
            out[px] = Image.new('1', (w,h), 0)
            
        out[px].putpixel((x,y), 1)
    print dbg
        
for o in out:
    out[o].save(''.join([prefix, str(o), '.bmp']))
            

sub.call(['rm', png])
            