#!/usr/bin/env bash
# update ubuntu 18.04 LTS
sudo apt-get update

# install nvidia ubuntu drivers
sudo apt-get install ubuntu-drivers-common
sudo ubuntu-drivers autoinstall

# install cuda
sudo apt install nvidia-cuda-toolkit

# install caffe for GPU
sudo apt-get install caffe-cuda

# restart and let cuda driver start
sudo reboot

# use python3 ,import caffe, caffe.set_device(0) to see is caffe already for use