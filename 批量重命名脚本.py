#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class ImageRename():
    def __init__(self):
        self.path = '/home/administrator/桌面/yu_train_Mask_RCNN/train_data'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 1
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')
                os.rename(src, dst)
                i = i + 1

if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()
