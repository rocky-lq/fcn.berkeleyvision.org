#!/usr/bin/env bash
# pascal voc 2012
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
# tar
tar -xvf VOCtrainval_11-May-2012.tar

# rename
mv VOC2012/ VOC2011/

# benchmark release
wget http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/semantic_contours/benchmark.tgz
tar -xvf benchmark.tgz

#vgg16 pretrain use to train fcn32s
wget http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel

#wget fcn-32s pretrain
wget http://dl.caffe.berkeleyvision.org/fcn32s-heavy-pascal.caffemodel

#wget fcn-16s pretrain
wget http://dl.caffe.berkeleyvision.org/fcn16s-heavy-pascal.caffemodel

#wget fcn-8s pretrain
wget http://dl.caffe.berkeleyvision.org/fcn8s-heavy-pascal.caffemodel