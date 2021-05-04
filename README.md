# G1020 segmentation mask generator
 G1020 segmentation masks generator

This repository contains a file to read json files of G1020 dataset and generate the correspoding image masks including disc and cup.

G1020: fundus Glaucoma dataset 
https://arxiv.org/abs/2006.09158

Install the requirements (tested with python 3.6). </br>
Specify the _in_dir_ and _out_dir_ in the main.py file. consider the provided sample folders.</br>
and then </br>
> python main.py

<img src="./G1020/image_0.jpg" width="350" title="input">
<img src="./G1020-segments/image_0.jpg" width="350" title="input">


## Resource: 
This code is based on labelme package:
https://github.com/wkentaro/labelme
