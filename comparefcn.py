import numpy as np
from PIL import Image

import caffe
import vis
import os
import sys
import time

start = time.clock()


title_list = np.array(['origin','FCN-8s', 'Deeplab'])


caffe.set_device(int(sys.argv[1]))
caffe.set_mode_gpu()


origin = [];

for files in os.listdir('segmentation/Origin'):
    origin.append(files)



net = caffe.Net('voc-fcn32s/deploy.prototxt', 'voc-fcn32s/fcn32s-heavy-pascal.caffemodel', caffe.TEST)
for file in origin:
	im = Image.open('segmentation/Origin/' + file)
	in_ = np.array(im, dtype=np.float32)
	in_ = in_[:,:,::-1]
	in_ -= np.array((104.00698793,116.66876762,122.67891434))
	in_ = in_.transpose((2,0,1))
	# shape for input (data blob is N x C x H x W), set data
	net.blobs['data'].reshape(1, *in_.shape)
	net.blobs['data'].data[...] = in_
	# run net and take argmax for prediction
	net.forward()
	out = net.blobs['score'].data[0].argmax(axis=0)

	# visualize segmentation in PASCAL VOC colors
	voc_palette = vis.make_palette(21)
	out_im = Image.fromarray(vis.color_seg(out, voc_palette))
	out_im.save('segmentation/fcn32s/' + file)

end = time.clock()

print("time used: " , end -start)

