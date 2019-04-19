from PIL import Image
import os
import glob
os.chdir(r'./')
for file_names in glob.glob('*.bmp'):
    print(file_names)
    file_path = r'./'+'//'+ file_names
    print(file_path)
    out_path = os.path.splitext(file_path)[0]+'.jpg'
    Image.open(file_path).save(out_path)
    print('转换成功')
