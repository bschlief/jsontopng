import sys
import png
import json

length = 16
width = 16

filename = sys.argv[1]
image_index = int(sys.argv[2])

with open(filename) as data_file:
    data = json.load(data_file)

target = data[image_index]['target']
print "Getting image #{0}, which is a {1}".format(image_index, target)

raw = data[image_index]['input']
pixels = [raw[i:i+width] for i in range(0, len(raw), length)]

outfile = open('image.png', 'wb')
w = png.Writer(len(pixels[0]), len(pixels), greyscale=True, bitdepth=1)
w.write(outfile, pixels)
outfile.close()


