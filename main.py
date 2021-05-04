# -*- coding: utf-8 -*-
"""
@author: meslami
"""



import base64
import json
import os
import os.path as osp

from labelme import utils
from PIL import Image as im
import numpy as np




in_dir='./G1020'
out_dir='./G1020-segments'



if not osp.exists(out_dir):
    os.mkdir(out_dir)
    
    
for root, dirs, files in os.walk(in_dir):
    for filename in files:
        
        if (filename.find('.json') !=-1):
            
            
            print('===> filename', filename)
            json_file=filename
    
            data = json.load(open(os.path.join(in_dir,json_file)))
            imageData = data.get("imageData")
            img_filename=data.get("imagePath")
            
            if not imageData:
                imagePath = os.path.join(in_dir, data["imagePath"])
                with open(imagePath, "rb") as f:
                    imageData = f.read()
                    imageData = base64.b64encode(imageData).decode("utf-8")
            img = utils.img_b64_to_arr(imageData)
            
            label_name_to_value = {"_background_": 0}
            for shape in sorted(data["shapes"], key=lambda x: x["label"]):
                label_name = shape["label"]
                if label_name in label_name_to_value:
                    label_value = label_name_to_value[label_name]
                else:
                    label_value = len(label_name_to_value)
                    label_name_to_value[label_name] = label_value
            lbl, _ = utils.shapes_to_label(
                img.shape, data["shapes"], label_name_to_value
            )
            
            
            lbl=lbl.astype(np.uint8)
            lbl=np.where(lbl==1,128,lbl)
            lbl=np.where(lbl==2,255,lbl)
            mask = im.fromarray(lbl)
            mask.save(osp.join(out_dir, img_filename))


